import requests 
import os


def get_diff_pull_request(github_token: str, github_repository: str, pull_request_number: int):
    headers = {
        "Accept": "application/vnd.github.diff",
        "authorization": f"Bearer {github_token}"
    }
    url = f'https://api.github.com/repos/{github_repository}/pulls/{pull_request_number}'
    response = requests.get(url=url, headers=headers)

    if response.status_code == 200:
        print(response.text)
    else:
        print(f'Error: {response.status_code}')


def main():
    github_token=os.getenv("GITHUB_TOKEN")
    github_repository=os.getenv("GITHUB_REPOSITORY")
    pull_request_number=int(os.getenv("GITHUB_PULL_REQUEST_NUMBER"))

    get_diff_pull_request(github_token, github_repository, pull_request_number)
    

if __name__ == "__main__":
    main()


