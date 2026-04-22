You are running an autonomous TFT data science cycle. Every cycle follows the same workflow regardless of input type.

## Step 1: Gather Inputs

Collect ALL pending inputs from these sources:

**Giscus comments** (primary):
```
gh api graphql -f query='{ repository(owner:"XWang20", name:"tft-stat") { discussions(first:20, orderBy:{field:CREATED_AT, direction:DESC}) { nodes { number, title, comments(first:10) { nodes { body, author { login }, createdAt } } } } } }'
```
Look for XWang20 comments. Discussion title maps to wiki page.

**GitHub Issues** (secondary):
```
gh issue list --repo XWang20/tft-stat --state open --json number,title,labels,body
```

**Experiment Queue** in wiki/content/index.md.

## Step 2: Bootstrap

Read wiki/content/index.md and wiki/content/lab-checklist.md.
Read relevant concepts/ and methods/ pages for the topics you'll work on.

## Step 3: Process Each Input (Same Standard For All)

For each input — whether it's Xing's feedback, a conclusion, a revision request, or a new experiment — apply the SAME workflow:

### 3a. Understand the Task
- Giscus "accept" → mark ✅, move to next input
- Giscus feedback → the task is: fix the report + deepen knowledge
- Giscus conclusion → the task is: integrate into wiki knowledge pages
- Issue (any label) → the task is: whatever the issue describes
- Experiment queue item → the task is: run the experiment

### 3b. Execute (Three Outputs)

Every task MUST produce at least two of three:

1. **Report/Fix**: Write new experiment report OR fix existing report. Read full report end-to-end after changes, verify all numbers and cross-references are consistent.

2. **Knowledge Deepening**: Substantively update the relevant concepts/ or methods/ page. NOT a status change or one-line lesson — real content that makes a new agent smarter.
   - Ask: "Does a new agent reading the wiki now understand this topic more deeply?"

3. **Code Improvement** (when applicable): If you discover a new method, pattern, or tool gap — implement it in tft_stat/ or cli.py.
   - Ask: "Can the system do something it couldn't before?"

### 3c. Update Global Wiki

After EACH task, update:
- **index.md** — experiment table status, syllabus progress, experiment queue
- **log.md** — what was done, with [[wikilinks]] to every file modified
- **lab-checklist.md** — new process lessons (with reasoning, not just rules)

## Step 4: Reply to Processed Inputs

For each Giscus comment processed:
```
gh api graphql -f query='mutation { addDiscussionComment(input: {discussionId: "DISCUSSION_NODE_ID", body: "Processed: [summary of what was done, which files updated]"}) { comment { id } } }'
```

For each Issue processed:
```
gh issue close NUMBER --repo XWang20/tft-stat -c "Processed: [summary]"
```

## Step 5: Commit and Push

```
git add wiki/ tft_stat/ cli.py .
git commit -m "cron: [summary of all tasks processed]

via [HAPI](https://hapi.run)

Co-Authored-By: HAPI <noreply@hapi.run>"
git push
```

## Rules

- Necessity as primary metric, NEVER raw AVP
- Stay focused on each task's original question
- Cross-validate with tftable when applicable (python3 cli.py tftable)
- After revising any report, read it end-to-end for consistency
- Experiment reports use date prefix: YYYY-MM-DD-<title>.md, status 🧪 draft
