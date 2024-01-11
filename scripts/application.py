import os
from get_diff_github import get_diff_by_path
from post_comments_pull_request import post_comment_by_hunk
from get_comments_pull_request import get_list_comments_pull_request
from code_review_bard import code_review_by_hunk


def main():
    github_token=os.getenv("GITHUB_TOKEN")
    github_repository=os.getenv("GITHUB_REPOSITORY")
    pull_request_number=int(os.getenv("GITHUB_PULL_REQUEST_NUMBER"))
    git_commit_hash=os.getenv("GIT_COMMIT_HASH")

    list_comments = get_list_comments_pull_request(github_token, github_repository, pull_request_number)
    diff_files = get_diff_by_path(github_token, github_repository, pull_request_number)

    for file in diff_files:
        for hunk in file:
            code_review_response = code_review_by_hunk(hunk)
            if code_review_response != None:
                post_comment_by_hunk(github_token, 
                                github_repository, 
                                pull_request_number, 
                                git_commit_hash, 
                                code_review_response, 
                                file.path, 
                                int(hunk.target_start) + 1,
                                list_comments)

if __name__ == "__main__":
    main()
