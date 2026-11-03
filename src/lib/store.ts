import { useSyncExternalStore } from "react";
import {
  type Category,
  type ExamPreset,
  EXAM_CONFIG,
  getQuestion,
  isCorrect,
  maxScoreOf,
  scoreOf,
} from "./bank";

const KEY = "siap-cpns-2027:v1";
export const APP_VERSION = "1.0.0";

export type SessionMode = "latihan" | "cat" | "tryout";

export interface ActiveSession {
  id: string;
  mode: SessionMode;
  title: string;
  questionIds: string[];
  answers: (number | null)[];
  flagged: boolean[];
  startedAt: number;
  endsAt: number | null; // ms timestamp; null = tanpa batas waktu
  feedback: "instant" | "end";
  presetId?: string;
  current: number;
}

export interface CatScore {
  score: number;
  max: number;
  correct: number;
  wrong: number;
  empty: number;
  passingGrade?: number;
}

export interface SessionResult {
  id: string;
  mode: SessionMode;
  title: string;
  date: number;
  durationSec: number;
  questionIds: string[];
  answers: (number | null)[];
  perCategory: Partial<Record<Category, CatScore>>;
  total: CatScore;
  passed?: boolean;
  presetId?: string;
}

export interface QStat {
  a: number; // attempts
  c: number; // correct
  w: number; // wrong count
  last: number | null;
  lastCorrect: boolean;
}

export interface AppState {
  version: number;
  profile: {
    name: string;
    formasi: string;
    targetScore: number;
    preference: string;
  };
  settings: {
    theme: "light" | "dark";
    presetId: string;
    feedback: "instant" | "end";
    timerVisible: boolean;
    reminderTime: string;
  };
  goals: { dailyQuestions: number; dailyMinutes: number };
  activity: Record<string, { q: number; s: number }>; // YYYY-MM-DD
  qstats: Record<string, QStat>;
  bookmarks: string[];
  history: SessionResult[];
  active: ActiveSession | null;
  flashcards: Record<string, "hafal" | "belajar">;
  modulesRead: string[];
}

export const DEFAULT_STATE: AppState = {
  version: 1,
  profile: { name: "", formasi: "Administrasi Pemerintahan", targetScore: 400, preference: "Campuran" },
  settings: { theme: "light", presetId: "skd-2024", feedback: "end", timerVisible: true, reminderTime: "19:00" },
  goals: { dailyQuestions: 30, dailyMinutes: 45 },
  activity: {},
  qstats: {},
  bookmarks: [],
  history: [],
  active: null,
  flashcards: {},
  modulesRead: [],
};

/** Validasi & gabungkan data mentah dengan default agar data rusak tidak membuat aplikasi crash. */
export function sanitize(raw: unknown): AppState {
  if (!raw || typeof raw !== "object") return structuredClone(DEFAULT_STATE);
  const r = raw as Partial<AppState>;
  const obj = (v: unknown) => (v && typeof v === "object" && !Array.isArray(v) ? v : {});
  const arr = <T>(v: unknown): T[] => (Array.isArray(v) ? (v as T[]) : []);
  return {
    version: 1,
    profile: { ...DEFAULT_STATE.profile, ...obj(r.profile) },
    settings: { ...DEFAULT_STATE.settings, ...obj(r.settings) },
    goals: { ...DEFAULT_STATE.goals, ...obj(r.goals) },
    activity: obj(r.activity) as AppState["activity"],
    qstats: obj(r.qstats) as AppState["qstats"],
    bookmarks: arr<string>(r.bookmarks).filter((x) => typeof x === "string"),
    history: arr<SessionResult>(r.history).filter((h) => h && typeof h.id === "string" && h.total),
    active:
      r.active && Array.isArray(r.active.questionIds) && Array.isArray(r.active.answers)
        ? r.active
        : null,
    flashcards: obj(r.flashcards) as AppState["flashcards"],
    modulesRead: arr<string>(r.modulesRead),
  };
}

let state: AppState = DEFAULT_STATE;
let loaded = false;
const listeners = new Set<() => void>();

function load() {
  if (loaded || typeof window === "undefined") return;
  loaded = true;
  try {
    const txt = localStorage.getItem(KEY);
    state = txt ? sanitize(JSON.parse(txt)) : structuredClone(DEFAULT_STATE);
  } catch {
    state = structuredClone(DEFAULT_STATE);
  }
}

function persist() {
  try {
    localStorage.setItem(KEY, JSON.stringify(state));
  } catch (e) {
    console.error("Gagal menyimpan data", e);
  }
}

export function setState(fn: (s: AppState) => AppState) {
  load();
  state = fn(state);
  persist();
  listeners.forEach((l) => l());
}

export function getState() {
  load();
  return state;
}

function subscribe(l: () => void) {
  listeners.add(l);
  return () => listeners.delete(l);
}

export function useApp(): AppState {
  return useSyncExternalStore(subscribe, getState, () => DEFAULT_STATE);
}

export const today = (d = new Date()) =>
  `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`;

export function getPreset(id: string): ExamPreset {
  return EXAM_CONFIG.presets.find((p) => p.id === id) ?? EXAM_CONFIG.presets[0];
}

export function streak(activity: AppState["activity"]): number {
  let n = 0;
  const d = new Date();
  if (!activity[today(d)]) d.setDate(d.getDate() - 1);
  while (activity[today(d)]?.q) {
    n++;
    d.setDate(d.getDate() - 1);
  }
  return n;
}

/* ------------------------------------------------------------- actions */

export function toggleBookmark(id: string) {
  setState((s) => ({
    ...s,
    bookmarks: s.bookmarks.includes(id) ? s.bookmarks.filter((b) => b !== id) : [...s.bookmarks, id],
  }));
}

export function startSession(p: Omit<ActiveSession, "id" | "answers" | "flagged" | "startedAt" | "current" | "endsAt"> & { minutes?: number }) {
  const now = Date.now();
  const session: ActiveSession = {
    id: `${p.mode}-${now}`,
    mode: p.mode,
    title: p.title,
    questionIds: p.questionIds,
    answers: p.questionIds.map(() => null),
    flagged: p.questionIds.map(() => false),
    startedAt: now,
    endsAt: p.minutes ? now + p.minutes * 60_000 : null,
    feedback: p.feedback,
    presetId: p.presetId,
    current: 0,
  };
  setState((s) => ({ ...s, active: session }));
}

export function updateActive(fn: (a: ActiveSession) => ActiveSession) {
  setState((s) => (s.active ? { ...s, active: fn(s.active) } : s));
}

export function computeResult(a: ActiveSession, endTime = Date.now()): SessionResult {
  const preset = a.presetId ? getPreset(a.presetId) : undefined;
  const per: Partial<Record<Category, CatScore>> = {};
  const total: CatScore = { score: 0, max: 0, correct: 0, wrong: 0, empty: 0 };
  a.questionIds.forEach((id, i) => {
    const q = getQuestion(id);
    if (!q) return;
    const ch = a.answers[i];
    const sec = preset?.sections.find((s) => s.category === q.category);
    const cs = sec?.correctScore ?? 5;
    const c = (per[q.category] ??= { score: 0, max: 0, correct: 0, wrong: 0, empty: 0, passingGrade: sec?.passingGrade });
    const sc = scoreOf(q, ch, cs);
    const mx = maxScoreOf(q, cs);
    const kind = ch === null ? "empty" : isCorrect(q, ch) ? "correct" : "wrong";
    for (const t of [c, total]) {
      t.score += sc;
      t.max += mx;
      t[kind]++;
    }
  });
  let passed: boolean | undefined;
  if (preset && a.mode !== "latihan") {
    passed = preset.sections.every((s) => (per[s.category as Category]?.score ?? 0) >= s.passingGrade);
  }
  return {
    id: a.id,
    mode: a.mode,
    title: a.title,
    date: endTime,
    durationSec: Math.round((Math.min(endTime, a.endsAt ?? endTime) - a.startedAt) / 1000),
    questionIds: a.questionIds,
    answers: a.answers,
    perCategory: per,
    total,
    passed,
    presetId: a.presetId,
  };
}

/** Akhiri sesi aktif: simpan hasil, perbarui statistik soal & aktivitas harian. */
export function finishActive(): string | null {
  const a = getState().active;
  if (!a) return null;
  const result = computeResult(a);
  setState((s) => {
    const qstats = { ...s.qstats };
    let answered = 0;
    a.questionIds.forEach((id, i) => {
      const ch = a.answers[i];
      const q = getQuestion(id);
      if (ch === null || !q) return;
      answered++;
      const ok = isCorrect(q, ch);
      const prev = qstats[id] ?? { a: 0, c: 0, w: 0, last: null, lastCorrect: false };
      qstats[id] = { a: prev.a + 1, c: prev.c + (ok ? 1 : 0), w: prev.w + (ok ? 0 : 1), last: ch, lastCorrect: ok };
    });
    const d = today();
    const act = s.activity[d] ?? { q: 0, s: 0 };
    return {
      ...s,
      qstats,
      active: null,
      activity: { ...s.activity, [d]: { q: act.q + answered, s: act.s + result.durationSec } },
      history: [result, ...s.history].slice(0, 200),
    };
  });
  return result.id;
}

export function wrongIds(s: AppState): string[] {
  return Object.entries(s.qstats)
    .filter(([id, st]) => !st.lastCorrect && getQuestion(id)?.category !== "TKP")
    .map(([id]) => id);
}

export function exportBackup(): string {
  return JSON.stringify({ app: "siap-cpns-2027", exportedAt: new Date().toISOString(), data: getState() }, null, 1);
}

export function importBackup(text: string) {
  const parsed = JSON.parse(text);
  const data = parsed?.data ?? parsed;
  if (!data || typeof data !== "object" || !("profile" in data)) throw new Error("Format backup tidak dikenali");
  setState(() => sanitize(data));
}

export function resetAll() {
  setState(() => structuredClone(DEFAULT_STATE));
}
