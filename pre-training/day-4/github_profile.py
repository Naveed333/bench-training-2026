import sys
import urllib.request
import urllib.error
import json


def fetch_json(url):
    req = urllib.request.Request(url, headers={"User-Agent": "python-script"})
    with urllib.request.urlopen(req, timeout=10) as response:
        return json.loads(response.read().decode())


def fetch_github_profile(username):
    base = "https://api.github.com"

    try:
        profile = fetch_json(f"{base}/users/{username}")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"Error: User '{username}' not found.")
        elif e.code in (403, 429):
            print("Error: GitHub API rate limit hit. Try again later.")
        else:
            print(f"Error: HTTP {e.code} - {e.reason}")
        return
    except urllib.error.URLError as e:
        print(f"Network error: {e.reason}")
        return

    print("\n" + "=" * 45)
    print(f"  GitHub Profile: {profile.get('login')}")
    print("=" * 45)
    print(f"  Bio       : {profile.get('bio') or 'N/A'}")
    print(f"  Repos     : {profile.get('public_repos')}")
    print(f"  Followers : {profile.get('followers')}")
    print(f"  Following : {profile.get('following')}")

    try:
        repos = fetch_json(f"{base}/users/{username}/repos?per_page=100")
    except (urllib.error.HTTPError, urllib.error.URLError) as e:
        print(f"\nCould not fetch repos: {e}")
        return

    top_5 = sorted(repos, key=lambda r: r.get("stargazers_count", 0), reverse=True)[:5]

    print("\n  Top 5 Repos by Stars:")
    print(f"  {'Repo':<35} {'Stars':>6}  Language")
    print("  " + "-" * 55)
    for repo in top_5:
        name = repo.get("name", "")[:34]
        stars = repo.get("stargazers_count", 0)
        lang = repo.get("language") or "N/A"
        print(f"  {name:<35} {stars:>6}  {lang}")

    print()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python github_profile.py <username>")
        sys.exit(1)
    fetch_github_profile(sys.argv[1])
