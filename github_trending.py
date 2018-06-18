import requests
import datetime as dt


def get_trending_repositories(top_size):
    search_date = str(dt.date.today() - dt.timedelta(weeks=1))
    print(search_date)
    search_params = {
        'q': 'created>{}'.format(search_date),
        'sort': 'stars'
    }
    top_repos = requests.get(
        'https://api.github.com/search/repositories',
        params=search_params
    ).json()['items']
    return top_repos


def get_open_issues_amount(repo_owner, repo_name):
    url = 'https://api.github.com/repos/{}/{}/issues'.format(
        repo_owner,
        repo_name
    )
    return requests.get(url).json


if __name__ == '__main__':
    top_size = 20
    top_repos = get_trending_repositories(top_size)
    for repo in top_repos:
        print(repo['full_name'])

