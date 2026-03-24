# Day 7 – Reddit Headline Analyser

## What it does

Fetches the top 50 posts from `r/technology` using the Reddit JSON API (no auth needed).

- Counts word frequency across all post titles (stopwords excluded)
- Prints the top 20 most common words
- Finds the most upvoted post
- Calculates average upvotes
- Splits posts into today vs older
- Saves a full report to `report.json`

## How to run

```
python reddit_analyser.py
```

No dependencies beyond the standard library.

## Example Output

```
Fetching top 50 posts from r/technology...

=======================================================
   REDDIT /r/technology — TOP 50 ANALYSIS
=======================================================

Total posts fetched : 34
Average upvotes     : 1,705
Posts from today    : 25
Older posts         : 9

── Most Upvoted Post ──────────────────────────────────
  Score : 17,613
  Title : Pilot Believes He Has Found Amelia Earhart's Long-Lost Airplane (Missing Since 1937) Via Google Earth.
  URL   : https://www.yahoo.com/news/...

── Top 20 Words Across All Titles ─────────────────────
  #    Word                 Count
  ------------------------------
  1    ai                   7
  2    us                   4
  3    data                 3
  4    system               3
  5    age                  2
  6    says                 2
  7    never                2
  8    targeted             2
  9    claims               2
  10   palantir             2
  ...

Report saved to report.json
```

## Output file

`report.json` contains: top 20 words, most upvoted post, avg upvotes, posts today vs older, and a timestamp.
