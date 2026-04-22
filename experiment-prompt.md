You are running a scheduled TFT data science experiment. Follow these steps exactly:

## Step 0: Process Giscus Reviews (FIRST PRIORITY)

Xing reviews experiments via Giscus comments on wiki pages (backed by GitHub Discussions).

Run this to find Xing's comments:
```
gh api graphql -f query='{ repository(owner:"XWang20", name:"tft-stat") { discussions(first:20, orderBy:{field:CREATED_AT, direction:DESC}) { nodes { number, title, comments(first:10) { nodes { body, author { login }, createdAt } } } } } }'
```

Look for comments by XWang20. The discussion title maps to the wiki page (e.g. "tft-stat/experiments/2026-04-22-nova-trait-breakpoint" → `wiki/content/experiments/2026-04-22-nova-trait-breakpoint.md`).

For each comment from Xing:
- **"accept"** → update status to ✅ in report and index.md
- **feedback/revision text** → Treat this as a FULL task with the same three-output standard:
  1. **Fix the report**: Read the full report end-to-end, fix all issues Xing described, verify internal consistency (numbers, conclusions, cross-references all match)
  2. **Deepen knowledge**: What does this feedback teach? Update the relevant concepts/ or methods/ page with substantive content — not just a checklist line, but deeper understanding. Ask: "Does a new agent reading the wiki now understand this better?"
  3. **Improve code** (if applicable): If the feedback reveals a tool gap or method limitation, implement it in tft_stat/ or cli.py
  4. Update status to 🧪 draft in report and index.md
  DO NOT just record the feedback and add a lesson. Execute the revision AND compound the learning.
- **conclusion** → integrate into concepts/ or methods/ pages with substantive content

After processing, reply to the discussion:
```
gh api graphql -f query='mutation { addDiscussionComment(input: {discussionId: "DISCUSSION_NODE_ID", body: "Processed: [summary]"}) { comment { id } } }'
```

Also check GitHub Issues: `gh issue list --repo XWang20/tft-stat --state open --json number,title,labels,body`

## Step 1: Bootstrap

Read wiki/content/index.md — syllabus, experiment queue, current progress.
Read wiki/content/lab-checklist.md — rules.
Read relevant concepts/ and methods/ pages for the topic you'll work on.

## Step 2: Pick an Experiment

Pick the FIRST item from the Experiment Queue in index.md.
If empty, generate a question from open questions in previous experiments.
Remove it from the queue after picking.

## Step 3: Run the Experiment

- Use python3 cli.py (comps/total/units/items/tftable) to gather data
- Use Necessity as primary metric, NEVER raw AVP
- Cross-validate with tftable when applicable
- Stay focused on the original question

## Step 4: Produce Three Outputs (NOT JUST A REPORT)

Every experiment MUST produce improvements in at least two of these three:

### Output 1: Report (always)
Write to wiki/content/experiments/YYYY-MM-DD-<title>.md with status 🧪 draft.
Story format. Include "Questions for Xing" section.

### Output 2: Code Improvement (when applicable)
If the experiment reveals a new analysis method, a better debiasing approach,
or a reusable pattern — implement it in tft_stat/ or cli.py.

Examples of code improvements from experiments:
- Discovered build-level Necessity → add `cli.py builds` command
- Found that play-rate weighting matters → improve metrics.py
- Identified a filter pattern → add it to filter_params.py

Ask: "After this experiment, can the system do something it couldn't before?"

### Output 3: Wiki Knowledge Deepening (always)
DO NOT just add a status change or a one-line lesson. Substantively deepen
the relevant concepts/ or methods/ page with what you learned.

Bad update: "Added lesson #9 to lab-checklist: don't do X"
Good update: Rewrote the "Selection Bias" section of concepts/biases.md with
  specific examples from this experiment, quantified effect sizes, and a
  decision framework for when selection bias matters vs when it's negligible.

Ask: "After this experiment, does a new agent reading the wiki understand
this topic more deeply than before?"

## Step 5: Update ALL Relevant Wiki Files

Every run MUST update:
- **wiki/content/index.md** — experiments table, syllabus status, experiment queue
- **wiki/content/log.md** — wikilinks to every file modified:
  ```
  ## [YYYY-MM-DD] cron | [title]
  - Giscus #N: [action] [[experiments/YYYY-MM-DD-name]]
  - New experiment: [[experiments/YYYY-MM-DD-name]] — [summary]
  - Deepened: [[concepts/biases]] — added quantified selection bias examples
  - New code: cli.py builds command (from build-necessity experiment)
  - Updated: [[lab-checklist]], [[index]]
  ```
- **wiki/content/concepts/*.md or methods/*.md** — substantive updates, not just status changes
- **wiki/content/lab-checklist.md** — new lessons WITH reasoning from data

Verify: no orphan experiments. Every report in experiments/ appears in index.md.

## Step 6: Commit and Push

git add wiki/ tft_stat/ cli.py .
git commit -m "cron: [summary of all actions taken]

via [HAPI](https://hapi.run)

Co-Authored-By: HAPI <noreply@hapi.run>"
git push
