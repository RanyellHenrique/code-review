import requests
import json


def get_comments_pull_request(github_token: str, 
                              github_repository: str, 
                              pull_request_number: int):
    url = f'https://api.github.com/repos/{github_repository}/pulls/{pull_request_number}/comments'
    headers = {
        "Accept": "application/json",
        "authorization": f"Bearer {github_token}"
    }
    return requests.get(url=url, headers=headers)

def get_list_comments_pull_request(github_token: str,
                                   github_repository: str, 
                                   pull_request_number: int):
    
    response = get_comments_pull_request(github_token, 
                                         github_repository, 
                                         pull_request_number)
    if response.status_code == 200:
        comments = response.json()
        for comment in comments:
            print(comment['id'], comment['body'], comment['position'], comment['path'], comment['original_position'])
    else:
        print('Falha ao obter comentários:', response.content)