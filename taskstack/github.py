from github3 import login, GitHub
from .config import Config

class GitHubFactory:

    @staticmethod
    def session() -> GitHub:
        return login(token=Config.get().github_token())

    @staticmethod
    def anonymous_session() -> GitHub:
        return GitHub()

github_session = GitHubFactory.session
gihub_anonymous_session = GitHubFactory.anonymous_session
