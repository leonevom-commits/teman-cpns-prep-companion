import twk from "@/data/twk-questions.json";
import tiu from "@/data/tiu-questions.json";
import tkp from "@/data/tkp-questions.json";
import skb from "@/data/skb-questions.json";
import modules from "@/data/learning-modules.json";
import flashcards from "@/data/flashcards.json";
import examConfig from "@/data/exam-config.json";

export type Category = "TWK" | "TIU" | "TKP" | "SKB";
export const CATEGORIES: Category[] = ["TWK", "TIU", "TKP", "SKB"];
export const CATEGORY_LABEL: Record<Category, string> = {
  TWK: "Tes Wawasan Kebangsaan",
  TIU: "Tes Intelegensia Umum",
  TKP: "Tes Karakteristik Pribadi",
  SKB: "Seleksi Kompetensi Bidang",
};

export interface Question {
  id: string;
  category: Category;
  sub: string;
  group?: string;
  question: string;
  figures?: string[];
  options: string[];
  optionType?: "svg" | "text";
  answer: number;
  scores?: number[];
  explanation: string;
  difficulty: "Mudah" | "Sedang" | "Sulit";
  reference: string;
  tags: string[];
}

export interface LearningModule {
  id: string;
  category: Category;
  sub: string;
  title: string;
  summary: string;
  sections: { heading: string; body: string }[];
  keyPoints: string[];
  example: string;
}

export interface Flashcard {
  id: string;
  deck: string;
  front: string;
  back: string;
}

export const ALL_QUESTIONS: Question[] = [
  ...(twk as Question[]),
  ...(tiu as Question[]),
  ...(tkp as Question[]),
  ...(skb as Question[]),
];
const BY_ID = new Map(ALL_QUESTIONS.map((q) => [q.id, q]));
export const getQuestion = (id: string) => BY_ID.get(id);

export const MODULES = modules as LearningModule[];
export const FLASHCARDS = flashcards as Flashcard[];
export const DECKS = [...new Set(FLASHCARDS.map((f) => f.deck))];
export const EXAM_CONFIG = examConfig;
export type ExamPreset = (typeof examConfig.presets)[number];

export function subsOf(cat: Category): string[] {
  return [...new Set(ALL_QUESTIONS.filter((q) => q.category === cat).map((q) => q.sub))];
}

export function shuffle<T>(arr: T[]): T[] {
  const a = [...arr];
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}

export interface Filter {
  category?: Category | "ALL";
  sub?: string;
  difficulty?: string;
  ids?: string[];
}

export function pickQuestions(f: Filter, count: number): string[] {
  let pool = f.ids ? f.ids.map(getQuestion).filter(Boolean) as Question[] : ALL_QUESTIONS;
  if (f.category && f.category !== "ALL") pool = pool.filter((q) => q.category === f.category);
  if (f.sub) pool = pool.filter((q) => q.sub === f.sub);
  if (f.difficulty && f.difficulty !== "ALL") pool = pool.filter((q) => q.difficulty === f.difficulty);
  return shuffle(pool).slice(0, count).map((q) => q.id);
}

/** Paket SKD: ambil jumlah soal per kategori; jika bank kurang, pakai semua yang ada. */
export function buildSkd(preset: ExamPreset, difficulty?: string): string[] {
  return preset.sections.flatMap((s) =>
    pickQuestions({ category: s.category as Category, difficulty }, s.count),
  );
}

/** Nilai satu soal. TKP: skor opsi 1–5; lainnya: benar = correctScore. */
export function scoreOf(q: Question, chosen: number | null, correctScore = 5): number {
  if (chosen === null || chosen === undefined) return 0;
  if (q.category === "TKP") return q.scores?.[chosen] ?? 0;
  return chosen === q.answer ? correctScore : 0;
}
export function maxScoreOf(q: Question, correctScore = 5) {
  return q.category === "TKP" ? 5 : correctScore;
}
/** "Benar" untuk statistik: TKP dihitung benar bila skor ≥ 4. */
export function isCorrect(q: Question, chosen: number | null): boolean {
  if (chosen === null || chosen === undefined) return false;
  if (q.category === "TKP") return (q.scores?.[chosen] ?? 0) >= 4;
  return chosen === q.answer;
}
