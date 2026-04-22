You are running a scheduled TFT data science experiment. Follow these steps exactly:

## Step 0: Process Giscus Comments (FIRST PRIORITY)

Xing leaves feedback as Giscus comments on wiki experiment pages. These appear as GitHub Discussions.

Run this to find Xing's unprocessed comments:
```
gh api graphql -f query='{ repository(owner:"XWang20", name:"tft-stat") { discussions(first:20, orderBy:{field:CREATED_AT, direction:DESC}) { nodes { number, title, comments(first:10) { nodes { body, author { login }, createdAt } } } } } }'
```

Look for comments by XWang20. The discussion title maps to the wiki page (e.g. "tft-stat/experiments/2026-04-22-nova-trait-breakpoint" → `wiki/content/experiments/2026-04-22-nova-trait-breakpoint.md`).

For each comment from Xing:
- **"accept"** → update experiment status to ✅ in the report and in index.md
- **feedback/revision request** → record in the report's ## Review section, update status to 🔄 in index.md, add to lab-checklist if it's a process lesson
- **conclusion** → integrate into relevant concepts/ or methods/ page
- **new topic** → add to Experiment Queue in index.md

After processing, reply to the discussion acknowledging what was done:
```
gh api graphql -f query='mutation { addDiscussionComment(input: {discussionId: "DISCUSSION_NODE_ID", body: "Processed: [summary of actions taken, files updated]"}) { comment { id } } }'
```

Also check GitHub Issues (may still have open ones):
```
gh issue list --repo XWang20/tft-stat --state open --json number,title,labels,body
```

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

Write the experiment report to wiki/content/experiments/YYYY-MM-DD-<title>.md with status 🧪 draft.
Story format with chapters. Include "Questions for Xing" section.

## Step 5: Update ALL Relevant Wiki Files

Every run MUST update these files:
- **wiki/content/index.md** — experiments table (add new entry or update status), syllabus status if module progressed, experiment queue (remove completed item)
- **wiki/content/log.md** — append entry for each action taken. MUST include wikilinks to every file modified, e.g.:
  ```
  ## [2026-04-22] cron | Issue processing + experiment
  - Issue #1 (revision): revised [[experiments/2026-04-22-nova-trait-breakpoint]] — switched to nova_yi
  - Issue #3 (conclusion): updated [[methods/filter-strategy]] — added "Trust compositions.py" section
  - New experiment: [[experiments/2026-04-23-unit-eval-nova95]] — Module 4
  - Updated: [[lab-checklist]] (lesson #8), [[index]] (experiments table, syllabus)
  ```
- **wiki/content/lab-checklist.md** — append new lessons if any were learned
- **wiki/content/concepts/*.md or methods/*.md** — update if new knowledge was validated

Verify: after all edits, every experiment mentioned in a report must appear in index.md's experiments table. No orphan experiments.

## Step 6: Commit and Push

git add wiki/ .
git commit -m "cron: [summary of all actions taken]

via [HAPI](https://hapi.run)

Co-Authored-By: HAPI <noreply@hapi.run>"
git push
