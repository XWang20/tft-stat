You are running a scheduled TFT data science experiment. Follow these steps exactly:

1. Read wiki/content/index.md — understand the syllabus, experiment queue, and current progress.
2. Read wiki/content/lab-checklist.md — internalize the rules.
3. Pick the FIRST item from the Experiment Queue in index.md. If the queue is empty, generate a surprising question from an open question in a previous experiment.
4. Run the experiment:
   - Use python3 cli.py (comps/total/units/items/tftable) to gather data
   - Use Necessity as primary metric, NEVER raw AVP
   - Cross-validate with tftable when applicable (python3 cli.py tftable)
5. Write the experiment report to wiki/content/experiments/<name>.md with status 🧪 draft
6. Update wiki/content/index.md — add to experiments table, update syllabus if relevant
7. Append to wiki/content/log.md
8. Git commit and push:
   git add wiki/
   git commit -m "experiment: <title>

   via [HAPI](https://hapi.run)

   Co-Authored-By: HAPI <noreply@hapi.run>"
   git push
