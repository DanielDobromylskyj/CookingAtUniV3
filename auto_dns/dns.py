from dotenv import load_dotenv
from threading import Thread
from github import Github
import requests
import time
import os

# Load variables from .env
load_dotenv()

ACCESS_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = "DanielDobromylskyj/server-ip"
FILE_PATH = "ip.txt"
COMMIT_MESSAGE = "Updated ip"


def get_public_ip():
    url = "https://api.ipify.org"
    response = requests.get(url)
    return response.content.decode("utf8")


def update():
    g = Github(ACCESS_TOKEN)
    repo = g.get_repo(REPO_NAME)
    content = str(get_public_ip())

    try:
        contents = repo.get_contents(FILE_PATH)
        repo.update_file(contents.path, COMMIT_MESSAGE, content, contents.sha)
    except Exception:
        repo.create_file(FILE_PATH, COMMIT_MESSAGE, content)


def start():
    def worker():
        while True:
            update()
            time.sleep(60)

    thread = Thread(target=worker)
    thread.start()


if __name__ == "__main__":
    start()
