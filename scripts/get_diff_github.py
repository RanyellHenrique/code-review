import requests 
import os
from unidiff import PatchSet

def get_diff_pull_request(github_token: str, github_repository: str, pull_request_number: int):
    headers = {
        "Accept": "application/vnd.github.diff",
        "authorization": f"Bearer {github_token}"
    }
    url = f'https://api.github.com/repos/{github_repository}/pulls/{pull_request_number}'
    return requests.get(url=url, headers=headers)

    


def get_diff_by_path(github_token: str, github_repository: str, pull_request_number: int):
    response =  get_diff_pull_request(github_token, github_repository, pull_request_number)
    diff_by_path = []
    if response.status_code == 200:
        patch = PatchSet(response.text, encoding='utf-8')
        for diff in patch:
            diff_by_path.append(diff)
    else:
        print(f'Error: {response.status_code}')
    return diff_by_path

def main():
    github_token=os.getenv("GITHUB_TOKEN")
    github_repository=os.getenv("GITHUB_REPOSITORY")
    pull_request_number=int(os.getenv("GITHUB_PULL_REQUEST_NUMBER"))

    diffs = get_diff_by_path(github_token, github_repository, pull_request_number)
    for item in diffs:
        print("----------------------------------")
        print(item)
        print("----------------------------------")


    

if __name__ == "__main__":
    main()


