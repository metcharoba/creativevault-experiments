# RFM Workflow v0.1 — Reference-first Mimic Workflow

Created: 2026-06-12
Status: **superseded by `reference_first_mimic_workflow_v0_2.md` (gated)** — kept
for history. v0.2 turns the screenshot-observation and lead-pick steps into hard
gates. Use v0.2 for new builds.

Background: the three-build validation
(`reference_first_mimic_test_v0_1` / `v0_2` / `v0_3`) clearly escaped the generic
AI-LP look across three different visual registers (dark/printerly, quiet/archival,
bright/pop). See `reference_first_mimic_validation_summary_v0_1.md`. This file defines
the method as a reusable workflow.

---

## 1. Workflow name

- **RFM Workflow**
- Reference-first Mimic Workflow
- 日本語名: **参照先行ミミック制作**

## 2. Trigger phrases

Start this workflow when the user says any of:

- 「RFMで1本作って」
- 「参照先行で1本作って」
- 「今までと違う絵でLP作って」
- 「AIっぽくないWebをまず1本作って」
- 「Reference-first mimicで作って」

## 3. When to use

- Making a new Web page / LP / top page.
- Wanting to avoid the generic AI mass-produced LP look.
- Trying out a design direction.
- Prototyping an alternative before putting it into an existing project.
- Running a visual experiment inside CreativeVault.

## 4. When NOT to use

- Small copy edits.
- Bug fixes.
- Minor tweaks to existing CSS.
- Medical work / MedicalVault.
- Anything involving secrets / API keys / raw responses.
- Final polish of an already-adopted design (no new direction needed).

## 5. Standard route

1. Find **3 references** (strong, non-SaaS, non-card-UI).
2. Choose **1 lead reference** (+ 1–2 support refs).
3. **Observe at least one real screenshot of the lead reference** (required).
4. Decompose: composition / whitespace / material / typography / information density /
   non-uniformity.
5. Write **borrow** vs **don't-borrow** elements.
6. Write an **avoid list** and an **aim list**.
7. **Decide materials first** (fonts + hero material).
8. Build **one** artifact in a **new directory**.
9. Take **screenshots**.
10. **Self-evaluate**.

## 6. Strong rules

- **Start from the visual language, not an existing concept name.** Lead with register +
  references + avoid/aim; let the (fictional) theme follow.
- **Never stop at candidates — always ship one built artifact.**
- **Do not fall back to**: centred hero / pill CTA / frosted glass card /
  even card grid / dark gradient + floating cards.
- **Even for same-kind elements, split treatment into at least 3 patterns** across
  frame, shadow, bleed/cut, texture, rotation, tone/density, and whitespace. (This is
  the recurring failure to attack: placement varies but processing goes uniform.)
- **Keep strength top-to-bottom** — the lower half must not collapse into a plain
  information-organising footer.
- **Real reference-screenshot observation is mandatory** (not "from memory" only).

## 7. Standard output

```
<new-dir>/
  index.html
  assets/                         (fonts, images, etc.)
  notes/reference_observation.md
  notes/materials_used.md
  notes/build_log.md
  notes/self_evaluation.md
  screenshots/01_desktop_firstview.png
  screenshots/02_desktop_full.png
  screenshots/03_mobile_full.png
```

## 8. Evaluation criteria

Score each honestly (and name one next change):

- Did it become a different picture than before?
- Was the lead reference's composition actually used?
- Did the generic-AI-LP feel decrease?
- Material feel.
- Non-uniformity.
- "Screen-as-artwork" feel.
- Is it strong top-to-bottom (not only the top)?
- Is the treatment of same-kind elements kept non-uniform (not templated)?

## 9. Boundaries

- **CreativeVault only.**
- **No MedicalVault / LocalOnlyProjects** referenced.
- **No secrets / .env / API key / token / webhook / raw response** used.
- External material must have its **license recorded** (OFL / CC0 / public domain /
  clearly-licensed free), in `notes/materials_used.md`.
- **No pasting external code.**
- **No wholesale copying of a reference site** (structure/observation only).

---

Constraint note: this is a **new single file**; no existing files were modified.
</content>
