import { createFileRoute } from "@tanstack/react-router";
import { Practice } from "@/components/study-pages";
import { pageHead } from "@/lib/page-meta";
export const Route = createFileRoute("/latihan")({ head:()=>pageHead("Latihan Soal","Bank soal CPNS gratis dengan pembahasan dan latihan sesuai topik."), component:Page});
function Page(){return <Practice/>;}
