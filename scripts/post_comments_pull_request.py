import requests
import json


def post_comment_pull_request(github_token: str, 
                              github_repository: str, 
                              pull_request_number: int,
                              git_commit_hash: str,
                              body: str,
                              path: str,
                              position: int,
                              list_comments: list):
    url = f'https://api.github.com/repos/{github_repository}/pulls/{pull_request_number}/comments'
    headers = {
        "Accept": "application/json",
        "authorization": f"Bearer {github_token}"
    }
    comment = get_comment_by_path_and_position(path, position, list_comments)
    if comment != None:
        data = {
            'body': body,
            'in_reply_to': comment.id
        }
    else:
        data = {
            'body': body,
            'commit_id': git_commit_hash,
            'path': path,
            'position': position
        }

    return requests.post(url, headers=headers, data=json.dumps(data))

def post_comment_by_hunk(github_token: str, 
                         github_repository: str, 
                         pull_request_number: int,
                         git_commit_hash: str,
                         body: str,
                         path: str,
                         position: int,
                         list_comments: list):
    response = post_comment_pull_request(github_token, 
                                         github_repository, 
                                         pull_request_number, 
                                         git_commit_hash, 
                                         body, 
                                         path, 
                                         position,
                                         list_comments)
    if response.status_code == 201:
        print('Comentário criado com sucesso.')
    else:
        print(f'Erro ao criar o comentário: {response.status_code}')
    
def get_comment_by_path_and_position(path: str, position: int, list_comments: list):
    for comment in list_comments:
        if path == comment['path'] and position == comment['position']:
            return comment
    return None