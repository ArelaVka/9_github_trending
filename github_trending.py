import requests
import datetime as dt
import sys


def get_trending_repositories(top_size):
    search_date = str(dt.date.today() - dt.timedelta(weeks=1))
    search_params = {
        'q': 'created:>' + search_date,
        'sort': 'stars'
    }
    top_repos = requests.get(
        'https://api.github.com/search/repositories',
        params=search_params
    ).json()['items'][:top_size]
    return top_repos


def get_open_issues_amount(repo):
    repo_owner = repo['owner']['login']
    repo_name = repo['name']
    url = 'https://api.github.com/repos/{}/{}/issues'.format(
        repo_owner,
        repo_name
    )
    open_issues = requests.get(url).json()
    if not(open_issues == []):
        return open_issues


def print_repos_info(repo):
    repo_owner = repo['owner']['login']
    repo_url = repo['html_url']
    print('\n--Author: {}\n--Repo: {}'.format(repo_owner, repo_url))


def print_repos_issue(issues):
    if issues:
        print('-Issues url of repo:')
        for issue in issues:
            if issue == 'message':
                sys.exit('Aborted: You have API rate limit exceeded!')
            print('issue-html:', issue['html_url'])
    else:
        print('No issue was found!')


if __name__ == '__main__':
    top_size = 20
    top_repos = get_trending_repositories(top_size)
    for repo in top_repos:
        print_repos_info(repo)
        issues = get_open_issues_amount(repo)
        print_repos_issue(issues)
