import urllib.request
import urllib.error
import json
import string
from datetime import datetime, timezone

URL = "https://www.reddit.com/r/technology/top.json?limit=50"

STOPWORDS = {
    "the", "a", "an", "to", "of", "and", "in", "is", "it", "for",
    "on", "with", "at", "by", "from", "or", "as", "be", "this",
    "that", "are", "was", "has", "have", "not", "but", "its", "i",
    "you", "he", "she", "we", "they", "do", "did", "will", "what",
    "how", "after", "about", "up", "his", "her", "my", "your", "their",
    "been", "so", "if", "can", "just", "over", "more", "new", "s", "vs"
}


def fetch_posts():
    req = urllib.request.Request(URL, headers={"User-Agent": "reddit-analyser/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
        return [post["data"] for post in data["data"]["children"]]
    except urllib.error.HTTPError as e:
        raise SystemExit(f"HTTP error {e.code}: {e.reason}")
    except urllib.error.URLError as e:
        raise SystemExit(f"Network error: {e.reason}")
    except (KeyError, json.JSONDecodeError) as e:
        raise SystemExit(f"Failed to parse Reddit response: {e}")


def word_frequency(posts):
    freq = {}
    for post in posts:
        title = post["title"].lower()
        title = title.translate(str.maketrans("", "", string.punctuation))
        for word in title.split():
            if word not in STOPWORDS and len(word) > 1:
                freq[word] = freq.get(word, 0) + 1
    return freq


def is_today(utc_timestamp):
    post_date = datetime.fromtimestamp(utc_timestamp, tz=timezone.utc).date()
    today = datetime.now(tz=timezone.utc).date()
    return post_date == today


def analyse(posts):
    freq = word_frequency(posts)
    top_20 = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:20]
    most_upvoted = max(posts, key=lambda p: p["score"])
    avg_upvotes = sum(p["score"] for p in posts) / len(posts)
    today_posts = [p for p in posts if is_today(p["created_utc"])]
    older_posts = [p for p in posts if not is_today(p["created_utc"])]

    return {
        "top_20_words": [{"word": w, "count": c} for w, c in top_20],
        "most_upvoted": {
            "title": most_upvoted["title"],
            "score": most_upvoted["score"],
            "url": most_upvoted["url"],
        },
        "avg_upvotes": round(avg_upvotes, 2),
        "posts_today": len(today_posts),
        "posts_older": len(older_posts),
        "total_posts": len(posts),
        "generated_at": datetime.now(tz=timezone.utc).isoformat(),
    }


def save_report(report, path="report.json"):
    try:
        with open(path, "w") as f:
            json.dump(report, f, indent=2)
        print(f"Report saved to {path}")
    except IOError as e:
        print(f"Warning: could not save report {e}")


def print_report(report):
    print("=" * 55)
    print("   REDDIT /r/technology — TOP 50 ANALYSIS")
    print("=" * 55)
    print(f"\nTotal posts fetched : {report['total_posts']}")
    print(f"Average upvotes     : {report['avg_upvotes']:,.0f}")
    print(f"Posts from today    : {report['posts_today']}")
    print(f"Older posts         : {report['posts_older']}")

    print("\n── Most Upvoted Post ──────────────────────────────────")
    print(f"  Score : {report['most_upvoted']['score']:,}")
    print(f"  Title : {report['most_upvoted']['title']}")
    print(f"  URL   : {report['most_upvoted']['url']}")

    print("\n── Top 20 Words Across All Titles ─────────────────────")
    print(f"  {'#':<4} {'Word':<20} Count")
    print("  " + "-" * 30)
    for i, entry in enumerate(report["top_20_words"], 1):
        print(f"  {i:<4} {entry['word']:<20} {entry['count']}")
    print("\n" + "=" * 55)


if __name__ == "__main__":
    print("Fetching top 50 posts from r/technology\n")
    posts = fetch_posts()
    print(f"Fetched pots ss ::: ",posts)
    report = analyse(posts)
    print_report(report)
    save_report(report)
