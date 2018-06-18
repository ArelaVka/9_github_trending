import requests
import datetime as dt


def get_trending_repositories(top_size):
    search_date = str(dt.date.today() - dt.timedelta(days=1))
    search_params = {
        'q': 'created: >' + search_date,
        'sort': 'star',
        'order': 'desc'
    }
    repos = requests.get(
        'https://api.github.com/search/repositories',
        params=search_params
    ).json()
    return repos


def get_open_issues_amount(repo_owner, repo_name):
    pass


if __name__ == '__main__':
    top_size = 20
    print(get_trending_repositories(top_size))
    print(str(dt.date.today() - dt.timedelta(weeks=1)))
