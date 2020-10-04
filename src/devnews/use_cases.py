from threading import Thread
from operator import attrgetter

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

        result.sort(key=attrgetter('updated_at'), reverse=True)

        return tuple(result)


class FeedParserThread(Thread):
    def __init__(self, repo, result):
        self.repo, self.result = repo, result

        super().__init__()

    def run(self):
        self.result.extend(self.repo.get_all())


class SearchNewsUseCase(ListNewsUseCase):
    def execute(self, query):
        result = super().execute()

        filtered_result = [a for a in result if a.contains(self.parse(query))]

        return tuple(filtered_result)

    def parse(self, query):
        if hasattr(query, "split"):
            return set(query.lower().split())
        else:
            return set(query)
