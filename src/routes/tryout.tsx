import { createFileRoute } from "@tanstack/react-router";
import { ExamSetup } from "@/components/study-pages";
import { pageHead } from "@/lib/page-meta";
export const Route = createFileRoute("/tryout")({ head:()=>pageHead("Tryout SKD","Uji kesiapan CPNS dengan paket tryout SKD."), component:Page});
function Page(){return <ExamSetup mode="tryout"/>;}
