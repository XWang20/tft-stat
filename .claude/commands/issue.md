Create a GitHub issue on XWang20/tft-stat for the TFT data science experiment system.

Ask the user for:
1. **Type** — one of: feedback (实验反馈), conclusion (验证的结论), revision (实验需修改), topic (新实验题目)
2. **Title** — short description
3. **Body** — details

If the user already provided this info in their message (e.g. "/issue feedback: nova-trait-breakpoint 偏离问题 ..."), parse it directly without asking.

Then run:
```
gh issue create --repo XWang20/tft-stat --label <type> --title "<title>" --body "<body>"
```

Report the issue URL when done.

Examples:
- `/issue feedback: cross-validation 不应该对比数据源，应该验证结论`
- `/issue conclusion: Necessity 排名对 baseline 不敏感`
- `/issue revision: nova-trait-breakpoint 用 nova_yi 重做`
- `/issue topic: 在其他阵容测试 Necessity 排名一致性`
