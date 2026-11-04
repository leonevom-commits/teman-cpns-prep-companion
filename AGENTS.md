<!-- LOVABLE:BEGIN -->
> [!IMPORTANT]
> This project is connected to [Lovable](https://lovable.dev). Avoid rewriting
> published git history — force pushing, or rebasing/amending/squashing commits
> that are already pushed — as it rewrites history on Lovable's side and the
> user will likely lose their project history.
>
> Commits you push to the connected branch sync back to Lovable and show up in
> the editor, so keep the branch in a working state.
<!-- LOVABLE:END -->

## Application architecture
- Keep CPNS content in bundled JSON and device progress in the existing external store, because the requested experience has no login or cloud dependency.
- Use file-based content routes under the shared AppShell; keep page metadata in each leaf route so navigation and share previews remain distinct.
- Use exam-config.json as the scoring and preset source of truth, including SKB scoring, to avoid divergent rules across sessions and results.
