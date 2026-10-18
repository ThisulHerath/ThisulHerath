"""Refresh the profile's public GitHub stats using the REST API."""
from collections import Counter
from datetime import datetime, timezone
import json
import os
from urllib.request import Request, urlopen

from build_profile import save, text, rect, line, label, WHITE, MUTED, MINT, LIME

USER = "ThisulHerath"


def get(path):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": f"{USER}-profile", "X-GitHub-Api-Version": "2022-11-28"}
    if os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]
    with urlopen(Request("https://api.github.com/" + path, headers=headers), timeout=30) as response:
        return json.load(response)


def main():
    profile = get(f"users/{USER}")
    repos = []
    page = 1
    while True:
        batch = get(f"users/{USER}/repos?per_page=100&type=owner&page={page}")
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    original = [r for r in repos if not r["fork"]]
    languages = Counter(r["language"] for r in original if r["language"])
    b = label("05", "SIGNAL TELEMETRY", "PUBLIC GITHUB SNAPSHOT")
    metrics = [("PUBLIC REPOSITORIES", profile["public_repos"]), ("STARS / OWN REPOS", sum(r["stargazers_count"] for r in original)), ("FOLLOWERS", profile["followers"])]
    for i, (name, value) in enumerate(metrics):
        x = 32 + i*386
        b += rect(x,80,364,121) + text(x+22,111,name,11,MINT,mono=True,spacing=1)
        b += text(x+22,175,f"{value:,}",46,WHITE,700)
    b += text(32,242,"REPOSITORIES BY PRIMARY LANGUAGE",12,LIME,mono=True,spacing=1)
    b += text(32,270,"Original public repos with a detected language · repository count, not code share",13,MUTED)
    top = languages.most_common(6)
    max_count = max(languages.values(), default=1)
    for i,(language,count) in enumerate(top):
        col, row = i%2, i//2
        x, y = 32+col*580, 314+row*42
        b += text(x,y,language,14,WHITE) + rect(x+155,y-11,320,7,"#1c2c3b",3,"none")
        b += rect(x+155,y-11,max(4,320*count/max_count),7,MINT if col==0 else LIME,3,"none")
        b += text(x+494,y,str(count),13,MUTED,mono=True)
    b += line(32,427,1168,427)
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    b += text(32,458,f"LAST SYNC / {date}",11,MUTED,mono=True,spacing=1)
    b += text(850,458,"SOURCE / GITHUB REST API",11,MUTED,mono=True)
    save("05-telemetry",480,"Signal telemetry — Thisul's public GitHub activity",f"Snapshot {date}. " + "; ".join(f"{name}: {value}" for name,value in metrics) + ". Primary languages counted by repository: " + ", ".join(f"{lang}: {count}" for lang,count in top),b)
    print(f"Refreshed telemetry from {len(repos)} public repositories at {date}")


if __name__ == "__main__":
    main()
