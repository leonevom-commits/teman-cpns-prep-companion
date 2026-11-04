import { createFileRoute } from "@tanstack/react-router";
import { ExamSetup } from "@/components/study-pages";
import { pageHead } from "@/lib/page-meta";
export const Route = createFileRoute("/cat")({ head:()=>pageHead("Simulasi CAT","Simulasi CAT SKD dengan timer 100 menit dan evaluasi ambang batas."), component:Page});
function Page(){return <ExamSetup mode="cat"/>;}
