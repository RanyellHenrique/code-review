import os
from get_diff_github import get_diff_by_path

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
