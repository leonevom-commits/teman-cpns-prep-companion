import { createFileRoute } from "@tanstack/react-router";
import { Materials } from "@/components/study-pages";
import { pageHead } from "@/lib/page-meta";
export const Route = createFileRoute("/materi")({validateSearch: (s: Record<string, unknown>): {category?: string} => ({category: typeof s['category'] === "string" ? s['category'] : "ALL"}), head:()=>pageHead("Materi Belajar","Pelajari materi TWK, TIU, TKP dan SKB untuk persiapan CPNS."), component:Page});
function Page(){const {category}=Route.useSearch(); return <Materials initialCategory={category}/>;}
