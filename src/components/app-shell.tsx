import { Link, useLocation } from "@tanstack/react-router";
import { useEffect, useState, type ReactNode } from "react";
import { BookOpen, LayoutDashboard, ListChecks, Monitor, Trophy, Layers, Bookmark, UserRound, GraduationCap, Menu, X, ChevronRight, Leaf, Sun, Moon } from "lucide-react";
import { Button } from "@/components/ui/button";
import { setState, useApp } from "@/lib/store";
import { cn } from "@/lib/utils";

const nav = [
  { to: "/", label: "Beranda", icon: LayoutDashboard },
  { to: "/materi", label: "Materi Belajar", icon: BookOpen },
  { to: "/latihan", label: "Latihan Soal", icon: ListChecks },
  { to: "/cat", label: "Simulasi CAT", icon: Monitor },
  { to: "/tryout", label: "Tryout", icon: Trophy },
  { to: "/flashcards", label: "Flashcards", icon: Layers },
  { to: "/review", label: "Review & Bookmark", icon: Bookmark },
  { to: "/profil", label: "Profil & Statistik", icon: UserRound },
] as const;
export function AppShell({ children }: { children: ReactNode }) {
  const app = useApp();
  const pathname = useLocation({ select: s => s.pathname });
  const [open, setOpen] = useState(false);
  useEffect(() => { document.documentElement.classList.toggle("dark", app.settings.theme === "dark"); }, [app.settings.theme]);
  useEffect(() => { setOpen(false); }, [pathname]);
  const title = nav.find(n => n.to === pathname)?.label ?? (pathname.startsWith("/hasil") ? "Hasil Latihan" : "Sesi Latihan");
  return <div className="min-h-screen bg-background">
    {open && <div className="fixed inset-0 z-30 bg-foreground/30 lg:hidden" onClick={() => setOpen(false)} />}
    <aside className={cn("fixed inset-y-0 left-0 z-40 flex w-60 flex-col border-r bg-card px-5 py-7 transition-transform lg:translate-x-0", open ? "translate-x-0" : "-translate-x-full")}>
      <Link to="/" className="flex items-center gap-3"><div className="flex size-10 items-center justify-center rounded-lg bg-primary text-primary-foreground"><GraduationCap className="size-6" /></div><div><div className="text-lg font-extrabold">Siap CPNS <span className="text-primary">2027</span></div><div className="mt-0.5 text-[10px] text-muted-foreground">Latihan Soal Gratis</div></div></Link>
      <div className="mb-3 mt-10 px-3 text-[10px] font-bold tracking-widest text-muted-foreground">MENU BELAJAR</div>
      <nav className="space-y-1.5">{nav.map(n => <Button key={n.to} asChild variant="ghost" className={cn("h-11 w-full justify-start gap-3 px-3 text-[13px]", pathname === n.to && "bg-accent font-bold text-primary")}><Link to={n.to}><n.icon className="size-[18px]" />{n.label}{pathname === n.to && <span className="ml-auto size-1.5 rounded-full bg-primary" />}</Link></Button>)}</nav>
      <div className="mt-auto border-t pt-6"><div className="flex items-center gap-2 text-xs font-semibold text-primary"><Leaf className="size-4" />Langkah kecil, mimpi besar.</div><p className="mt-2 text-[11px] leading-5 text-muted-foreground">Tetap konsisten. Masa depanmu<br />dimulai dari hari ini.</p><div className="mt-5 text-[10px] text-muted-foreground">Siap CPNS 2027 · v1.0.0</div></div>
    </aside>
    <div className="lg:ml-60"><header className="flex h-[76px] items-center justify-between border-b bg-card px-5 md:px-9"><div className="flex items-center gap-3"><Button variant="ghost" size="icon" onClick={() => setOpen(!open)} className="lg:hidden" aria-label={open ? "Tutup menu" : "Buka menu"}>{open ? <X /> : <Menu />}</Button><span className="text-sm font-semibold">{title}</span><ChevronRight className="size-3 text-muted-foreground" /><span className="hidden text-xs text-muted-foreground sm:inline">Persiapan CPNS 2027</span></div><div className="flex items-center gap-4"><span className="hidden rounded-md bg-secondary px-2.5 py-1.5 text-[10px] font-bold text-primary sm:block">GRATIS SELAMANYA</span><Button variant="ghost" size="icon" aria-label="Ganti tema" onClick={() => setState(s => ({ ...s, settings: { ...s.settings, theme: s.settings.theme === "light" ? "dark" : "light" } }))}>{app.settings.theme === "light" ? <Moon /> : <Sun />}</Button><Link to="/profil" className="flex size-9 items-center justify-center rounded-full bg-secondary text-sm font-bold text-primary">{app.profile.name.slice(0, 1).toUpperCase() || "S"}</Link></div></header><main className="page-enter mx-auto max-w-[1440px] px-5 py-7 md:px-9 md:py-8">{children}</main><footer className="mx-5 mt-8 flex flex-wrap justify-between gap-2 border-t py-5 text-[10px] text-muted-foreground md:mx-9"><span>© 2026 Siap CPNS 2027 Latihan Soal Gratis</span><span>Bukan aplikasi resmi BKN · Belajar tanpa biaya</span></footer></div>
  </div>;
}