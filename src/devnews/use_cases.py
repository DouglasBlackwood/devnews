from threading import Thread

PARSER_TIMEOUT = 10


class ListNewsUseCase:
    def __init__(self, *repositories):
        self.repositories = repositories

    def execute(self):
        threads = []
        result = []

        for repo in self.repositories:
            thread = FeedParserThread(repo, result)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join(timeout=PARSER_TIMEOUT)

        return tuple(result)


class FeedParserThread(Thread):
    def __init__(self, repo, result):
        self.repo, self.result = repo, result

        super().__init__()

    def run(self):
        self.result.extend(self.repo.get_all())
