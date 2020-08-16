from terminaltables import SingleTable


def print_table(news):
    data = [(entry.source_name, entry.title) for entry in news[:10]]
    data.insert(0, ("Feed", "Title"))
    table = SingleTable(data)
    print(table.table)
