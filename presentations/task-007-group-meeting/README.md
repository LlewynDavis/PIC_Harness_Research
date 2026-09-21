# 面向光子芯片智能设计的三方向技术调研

This workspace is the saved authoring source for the `deck-workspace` deck.

## Files

- `outline.json`: canonical structured slide source
- `content_plan.json`: thesis, audience, slide roles, and visual strategy
- `design_brief.json`: audience posture, cover concept, structure strategy, and grid policy
- `evidence_plan.json`: sourced claims, metrics, chart candidates, and gaps
- `style_contract.json`: stable style + layout contract for later slide additions
- `asset_plan.json`: source-backed imagery/background/chart staging plan
- `notes.md`: deck-specific data sources, decisions, and manual design notes
- `assets/`: local images, diagrams, logos, and tables used by the deck
- `build/`: generated `.pptx` output plus QA reports

## Commands

Build the deck:

```bash
python3 ../../scripts/build_workspace.py --workspace . --overwrite
```

Build and run strict QA:

```bash
python3 ../../scripts/build_workspace.py --workspace . --qa --overwrite
```

Use non-render QA when LibreOffice is unavailable:

```bash
python3 ../../scripts/build_workspace.py --workspace . --qa --skip-render --overwrite
```

Allow Wikimedia Commons fetches while staging assets:

```bash
python3 ../../scripts/build_workspace.py --workspace . --allow-network-assets --overwrite
```

## Iteration Pattern

1. Fill `content_plan.json` with thesis, audience, slide roles, and visual strategy.
2. Fill `design_brief.json` with audience posture, cover concept, and structure strategy.
3. Fill `evidence_plan.json` with sourced claims, metrics, and chart candidates.
4. Update `notes.md` with data rules and unresolved assumptions.
5. Add source-backed image/background/chart requests to `asset_plan.json`.
6. Stage local assets inside `assets/` when needed.
7. Edit `outline.json` to add, replace, or reorder slides.
8. Reference staged assets with aliases such as `asset:hero_name`, `image:crew_portrait`, or `generated:concept_visual`.
9. Re-run `build_workspace.py`.
10. Keep the source files. Do not rely on inline heredoc generation if you want to extend the deck later.
