def select_columns(columns, labels):
    results = list()
    for position in range(len(columns)):
        if columns[position] in labels:
            results.append(position)
    return results
