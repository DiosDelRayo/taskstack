from .github import github_session
from .config import Config

class TaskStack:

    def __init__(self):
        self.github = github_session()

    def switch(self, next_task: int) -> bool:
        next = self.github.issue(self.github.me().login, Config.get().repository(), next_task)
        if not next:
            return False
        wip: bool = False
        for issue in self.github.issues_on(
            self.github.me().login,
            Config.get().repository(),
            None,
            self.github.login,
            labels='WIP'
            ):
            wip = True
            issue.remove_label('WIP')
        for issue in self.github.issues_on(
            self.github.me().login,
            Config.get().repository(),
            None,
            self.github.login,
            labels='Active'
            ):
            issue.remove_label('Active')
        next.add_labels('Active')
        if wip:
            next.add_labels('WIP')
        return True

    def start(self) -> bool:
        for issue in self.github.issues_on(
            self.github.me().login,
            Config.get().repository(),
            None,
            self.github.login,
            labels='WIP'
            ):
            return False
        for issue in self.github.issues_on(
            self.github.me().login,
            Config.get().repository(),
            None,
            self.github.login,
            labels='Active'
            ):
            issue.add_labels('WIP')
            return True
        if self.next():
            return self.start()
        return False

    def stop(self) -> bool:
        for issue in self.github.issues_on(
            self.github.me().login,
            Config.get().repository(),
            None,
            self.github.login,
            labels='WIP'
            ):
            issue.remove_label('WIP')
            return True
        return False

    def stack(self, task: int) -> bool:
        issue = self.github.issue(self.github.me().login, Config.get().repository(), task)
        if not issue:
            return False
        issue.add_labels('Stacked')
        return True

    def unstack(self, task: int) -> bool:
        issue = self.github.issue(self.github.me().login, Config.get().repository(), task)
        if not issue:
            return False
        issue.remove_label('Stacked')
        return True

    def next(self) -> bool:
        for issue in self.github.issues_on(
            self.github.me().login,
            Config.get().repository(),
            None,
            self.github.login,
            labels='Active'
            ):
            issue.remove_label('Active')
        wip: bool = False
        for issue in self.github.issues_on(
            self.github.me().login,
            Config.get().repository(),
            None,
            self.github.login,
            labels='WIP'
            ):
            wip = True
            issue.remove_label('WIP')
        for issue in self.github.issues_on(
            self.github.me().login,
            Config.get().repository(),
            None,
            self.github.login,
            labels='Stacked'
            ):
            issue.add_labels('Active')
            issue.remove_label('Stacked')
            if wip:
                issue.add_labels('WIP')
            return True
        return False

        def list_tasks(self, filter_labels=None):
            """List tasks with optional label filtering"""
            issues = self.github.issues_on(
                self.github.me().login,
                Config.get().repository(),
                None,
                self.github.login,
                labels=filter_labels
            )
            return issues

        def add_task(self, title: str, body: str = "", labels: list = None) -> bool:
            """Create a new task (issue) in the repository"""
            try:
                repo = self.github.repository(self.github.me().login, Config.get().repository())
                if not repo:
                    return False
                    
                if labels is None:
                    labels = []
                    
                issue = repo.create_issue(
                    title=title,
                    body=body,
                    labels=labels
                )
                return bool(issue)
            except Exception:
                return False
