def select_columns(columns, labels):
    """
    Return the positions of the elements in ``labels`` inside ``columns``
    """
    return [pos for pos in range(len(columns)) if columns[pos] in labels]
