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


def get_open_issues_amount(repo_owner, repo_name):
    url = 'https://api.github.com/repos/{}/{}/issues'.format(
        repo_owner,
        repo_name
    )
    return requests.get(url).json()


if __name__ == '__main__':
    top_size = 20
    top_repos = get_trending_repositories(top_size)
    for repo in top_repos:
        repo_owner = repo['owner']['login']
        repo_name = repo['name']
        repo_url = repo['html_url']
        print(
            '\n--Author: {}\n--Repo: {}'.format(
                repo_owner,
                repo_url)
        )
        issues = get_open_issues_amount(repo_owner, repo_name)
        print('-Issues url of repo:')
        for issue in issues:
            if issue == 'message':
                sys.exit('Aborted: You have API rate limit exceeded!')
            else:
                if bool(issue):
                #print('issue:', issue)
                    print('type:', type(issue))
                    print('issue-html:', issue['html_url'])
                    print('type html:', type(issue['html_url']))
                else:
                    print('NICHEGO!!!!!!!')
            # if str(issue).count('API rate limit excSeeded') > 0:
            #     print('You have API rate limit exceeded')
            #     break
            # else:
            #     if bool(issue != []):
            #         print(issue['html_url'])
            #     else:
            #         print('Not found any issues')
            #         break

