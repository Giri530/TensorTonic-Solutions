def ordinal_encoding(values, ordering):
    rank={category:i for i,category in enumerate(ordering)}
    return [rank[v] for v in values]