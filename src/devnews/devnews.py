from terminaltables import SingleTable

from devnews.use_cases import ListNewsUseCase


def print_table(news):
    data = [(entry.source_name, entry.title) for entry in news[:10]]
    data.insert(0, ("Feed", "Title"))
    table = SingleTable(data)
    print(table.table)


if __name__ == "__main__":
    use_case = ListNewsUseCase()
    news = use_case.execute()
    print_table(news)
