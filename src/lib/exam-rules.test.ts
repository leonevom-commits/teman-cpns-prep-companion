import { describe, expect, it } from "vitest";
import { EXAM_CONFIG, ALL_QUESTIONS, buildSkd, scoreOf } from "./bank";
import { computeResult, type ActiveSession } from "./store";
describe("SKD reference rules",()=>{
 it("uses 30 TWK, 35 TIU, 45 TKP and 100 minutes for 2024",()=>{const p=EXAM_CONFIG.presets.find(p=>p.id==="skd-2024");expect(p?.durationMinutes).toBe(100);expect(p?.sections.map(s=>[s.category,s.count])).toEqual([["TWK",30],["TIU",35],["TKP",45]]);if(!p)throw new Error("Missing preset");expect(buildSkd(p)).toHaveLength(110);});
 it("uses passing thresholds 65, 80, 166",()=>{expect(EXAM_CONFIG.presets[0]?.sections.map(s=>s.passingGrade)).toEqual([65,80,166]);});
 it("scores TKP answers 1–5 and blank as zero",()=>{const q=ALL_QUESTIONS.find(q=>q.category==="TKP");if(!q)throw new Error("Missing TKP");expect(q.scores?.slice().sort()).toEqual([1,2,3,4,5]);q.scores?.forEach((s,i)=>expect(scoreOf(q,i)).toBe(s));expect(scoreOf(q,null)).toBe(0);});
 it("scores correct SKB answers as four points",()=>{const q=ALL_QUESTIONS.find(q=>q.category==="SKB");if(!q)throw new Error("Missing SKB");const session:ActiveSession={id:"test",mode:"latihan",title:"SKB",questionIds:[q.id],answers:[q.answer],flagged:[false],startedAt:0,endsAt:null,feedback:"end",current:0};expect(computeResult(session,1000).total.score).toBe(4);});
});
