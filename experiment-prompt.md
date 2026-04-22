You are running a scheduled TFT data science experiment. Follow these steps exactly:

## Step 0: Process GitHub Issues (FIRST PRIORITY)

Run: gh issue list --repo XWang20/tft-stat --state open --json number,title,labels,body

For each open issue:
- **feedback** label:
  1. Record in the experiment report's ## Review section (identify which experiment from the issue body)
  2. If it's a process lesson → append to wiki/content/lab-checklist.md Lessons Learned
  3. Update the experiment's status in wiki/content/index.md experiments table (e.g. 🔄 revision)
- **conclusion** label:
  1. Integrate into the relevant wiki/content/concepts/ or wiki/content/methods/ page
  2. Update that page's status in wiki/content/index.md knowledge base table if needed
- **revision** label:
  1. Revise the specified experiment report
  2. Update its status in wiki/content/index.md experiments table
  3. Update wiki/content/index.md syllabus status if the module status changed
- **topic** label:
  1. Add to the Experiment Queue in wiki/content/index.md
- After processing each issue, close it: gh issue close NUMBER --repo XWang20/tft-stat -c "Processed: [what was done, which files were updated]"
- Append all issue processing to wiki/content/log.md

If there are open issues, process ALL of them before starting a new experiment.

## Step 1: Bootstrap

Read wiki/content/index.md — understand the syllabus, experiment queue, and current progress.
Read wiki/content/lab-checklist.md — internalize the rules.

## Step 2: Pick an Experiment

Pick the FIRST item from the Experiment Queue in index.md.
If the queue is empty, generate a surprising question from an open question in a previous experiment.
Remove the item from the queue after picking it.

## Step 3: Run the Experiment

- Use python3 cli.py (comps/total/units/items/tftable) to gather data
- Use Necessity as primary metric, NEVER raw AVP
- Cross-validate with tftable when applicable (python3 cli.py tftable)
- Stay focused on the original question — don't drift into tangential analysis

## Step 4: Write the Report

Write the experiment report to wiki/content/experiments/<name>.md with status 🧪 draft.
Story format with chapters. Include "Questions for Xing" section.

## Step 5: Update ALL Relevant Wiki Files

Every run MUST update these files:
- **wiki/content/index.md** — experiments table (add new entry or update status), syllabus status if module progressed, experiment queue (remove completed item)
- **wiki/content/log.md** — append entry for each action taken. MUST include wikilinks to every file modified, e.g.:
  ```
  ## [2026-04-22] cron | Issue processing + experiment
  - Issue #1 (revision): revised [[experiments/nova-trait-breakpoint]] — switched to nova_yi
  - Issue #3 (conclusion): updated [[methods/filter-strategy]] — added "Trust compositions.py" section
  - New experiment: [[experiments/unit-eval-nova95]] — Module 4
  - Updated: [[lab-checklist]] (lesson #8), [[index]] (experiments table, syllabus)
  ```
- **wiki/content/lab-checklist.md** — append new lessons if any were learned
- **wiki/content/concepts/*.md or methods/*.md** — update if new knowledge was validated
- **wiki/content/schema.md** — only if workflow rules changed

Verify: after all edits, every experiment mentioned in a report must appear in index.md's experiments table. No orphan experiments.

## Step 6: Commit and Push

git add wiki/ .
git commit -m "cron: [summary of all actions taken]

via [HAPI](https://hapi.run)

Co-Authored-By: HAPI <noreply@hapi.run>"
git push
