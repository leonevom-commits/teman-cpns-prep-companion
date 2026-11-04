import { createFileRoute } from "@tanstack/react-router";
import { FlashcardsPage } from "@/components/study-pages";
import { pageHead } from "@/lib/page-meta";
export const Route = createFileRoute("/flashcards")({ head:()=>pageHead("Flashcards","Hafalkan konsep CPNS dengan kartu belajar interaktif."), component:Page});
function Page(){return <FlashcardsPage/>;}
