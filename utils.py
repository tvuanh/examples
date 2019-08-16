def select_columns(columns, labels):
    return [pos for pos in range(len(columns)) if columns[pos] in labels]
