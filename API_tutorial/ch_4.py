import requests
import pandas as pd

all_repos = []
page = 1

headers = {
    "User-Agent": "Tayyab-API-Practice"   # Required
}

while page <= 5:    # 5 pages = 50 results
    params = {
        "q": "pandas",     # search keyword
        "sort": "stars",
        "order": "desc",
        "page": page,
        "per_page": 10
    }

    url = "https://api.github.com/search/repositories"
    res = requests.get(url, headers=headers, params=params).json()

    items = res.get("items", [])
    if not items:
        break

    for repo in items:
        all_repos.append({
            "name": repo["name"],
            "stars": repo["stargazers_count"],
            "forks": repo["forks_count"],
            "language": repo["language"],
            "description": repo["description"]
        })

    page += 1

df = pd.DataFrame(all_repos)
df.to_csv("github_repos.csv", index=False)

print("Saved:", len(df), "repositories")
