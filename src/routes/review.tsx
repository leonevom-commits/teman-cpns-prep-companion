import { createFileRoute } from "@tanstack/react-router";
import { ReviewPage } from "@/components/study-pages";
import { pageHead } from "@/lib/page-meta";
export const Route = createFileRoute("/review")({ head:()=>pageHead("Review & Bookmark","Ulangi jawaban salah dan soal CPNS yang disimpan."), component:Page});
function Page(){return <ReviewPage/>;}
