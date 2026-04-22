You are running a scheduled TFT data science experiment. Follow these steps exactly:

## Step 0: Process GitHub Issues (FIRST PRIORITY)

Run: gh issue list --repo XWang20/tft-stat --state open --json number,title,labels,body

For each open issue:
- **feedback** label → record in the experiment report's ## Review section, update lab-checklist if it's a process lesson
- **conclusion** label → integrate into the relevant wiki concepts/ or methods/ page
- **revision** label → revise the specified experiment report
- **topic** label → add to the Experiment Queue in index.md
- After processing, close the issue: gh issue close NUMBER --repo XWang20/tft-stat -c "Processed: [what was done]"

If there are open issues, process ALL of them before starting a new experiment.

## Step 1: Bootstrap

Read wiki/content/index.md — understand the syllabus, experiment queue, and current progress.
Read wiki/content/lab-checklist.md — internalize the rules.

## Step 2: Pick an Experiment

Pick the FIRST item from the Experiment Queue in index.md.
If the queue is empty, generate a surprising question from an open question in a previous experiment.

## Step 3: Run the Experiment

- Use python3 cli.py (comps/total/units/items/tftable) to gather data
- Use Necessity as primary metric, NEVER raw AVP
- Cross-validate with tftable when applicable (python3 cli.py tftable)
- Stay focused on the original question — don't drift into tangential analysis

## Step 4: Write the Report

Write the experiment report to wiki/content/experiments/<name>.md with status 🧪 draft.
Story format with chapters. Include "Questions for Xing" section.

## Step 5: Update Wiki

- Update wiki/content/index.md — add to experiments table, update syllabus if relevant
- Append to wiki/content/log.md

## Step 6: Commit and Push

git add wiki/ .
git commit -m "experiment: <title>

via [HAPI](https://hapi.run)

Co-Authored-By: HAPI <noreply@hapi.run>"
git push
