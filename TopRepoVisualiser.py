import argparse

from requests import Session
from random import choice
from plotly import offline
from repo import Repo
from textwrap import dedent


def get_git_repos(keyword, per_page=50):
    url = f'https://api.github.com/search/repositories?q={keyword}&sort=stars&per_page={per_page}'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    s = Session()
    r = s.get(url, headers=headers)
    if r.status_code != 200:
        print(f"Returned bad status code - {r.status_code}")
        return False
    return r.json()


def parse_repos(repo_dicts):
    repos = list()
    for repo_dict in repo_dicts:
        repo = Repo(repo_dict['name'],
                    repo_dict['owner']['login'],
                    repo_dict['stargazers_count'],
                    repo_dict['html_url'],
                    repo_dict['created_at'],
                    repo_dict['updated_at'],
                    repo_dict['description'],)
        repos.append(repo)
    return repos


def show_popular_git_repos(repos, keyword):
    colors = ['#9DC7A0', '#FF6039', '#FFE4DB', '#84BDA1', '#FF3910', '#FFE7D0', '#569D84', '#FF4E42', '#FEFEFE', '#5B8264', '#C51D17', '#FFFFA0', '#FFFF9F', ]
    repo_names, stars, labels = [], [], []
    for repo in repos:
        repo_names.append(repo.name)
        stars.append(repo.stars)

        label = f'Owner: {repo.owner}<br />Description: {repo.description}<br />URL: {repo.repository}<br />Created: {repo.created}<br />Updated: {repo.updated}'
        labels.append(label)

    data = [{
        'type': 'bar',
        'x': repo_names,
        'y': stars,
        'hovertext': labels,
        'marker': {
            'color': choice(colors),
            'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'},
        },
        'opacity': 0.6,

    }]
    my_layout = {
        'title': f'Most-starred {keyword.title()} Projects on GitHub',
        'titlefont': {'size': 28},
        'xaxis': {'title': 'Repositories',
                  'titlefont': {'size': 24},
                  'tickfont': {'size': 14},
                  'tickangle': 45,
                  },
        'yaxis': {'title': 'Stars',
                  'titlefont': {'size': 24},
                  'tickfont': {'size': 14},
                  },
    }
    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename=f'{keyword}_repos.html')
    return True


if __name__ == "__main__":
    hello_logo = dedent(""" 

 ______          ___              _   ___               ___            
/_  __/__  ___  / _ \___ ___  ___| | / (_)__ __ _____ _/ (_)__ ___ ____
 / / / _ \/ _ \/ , _/ -_) _ \/ _ \ |/ / (_-</ // / _ `/ / (_-</ -_) __/
/_/  \___/ .__/_/|_|\__/ .__/\___/___/_/___/\_,_/\_,_/_/_/___/\__/_/   
        /_/           /_/                                              
                                                  
""")
    print(hello_logo)
    parser = argparse.ArgumentParser(description='This script creating barchart with the most popular Git repositories found by keyword')
    parser.add_argument("-k", "--keyword", help="Keyword that you would like to search", required=True)
    parser.add_argument("-s", "--show", action='store_true', help="show list with repositories info")
    parser.add_argument("-l", "--limit", type=int, default="30", help="Searching result limit (default: 30)")
    parser.add_argument("-o", "--output", help="output list with repo and urls into provided file")
    args = parser.parse_args()
	
    response_git = get_git_repos(args.keyword, per_page=args.limit)
    repo_dicts = response_git['items']
    repos = parse_repos(repo_dicts)
    show_popular_git_repos(repos, args.keyword)
    if args.show:
        for num,repo in enumerate(repos):
            print(f"{num + 1})", end=" ")
            repo.print_summary()
            print()
    if args.output:
        content = ''
        for num,repo in enumerate(repos):
            attributes_list = [f'{key}: {value}' for key,value in repo.get_attributes().items()]
            string = f'{num + 1}) ' + '\n'.join(attributes_list) + '\n\n'
            content += string
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(content)
    print('Execution completed')