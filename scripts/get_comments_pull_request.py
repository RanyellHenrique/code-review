import requests
from requests import Response
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

def format_and_populate_list_comments(response: Response, list_comments: list):
    comments = response.json()
    for comment in comments:
        list_comments.append({
            'id': comment['id'], 
            'body': comment['body'], 
            'position': comment['position'], 
            'path': comment['path']
            })

def get_list_comments_pull_request(github_token: str,
                                   github_repository: str, 
                                   pull_request_number: int):
    
    response = get_comments_pull_request(github_token, github_repository, pull_request_number)
    list_comments = []
    if response.status_code == 200:
        format_and_populate_list_comments(response, list_comments)
    else:
        print('Falha ao obter comentários:', response.content)
    return list_comments

