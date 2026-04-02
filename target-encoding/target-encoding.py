def target_encoding(categories, targets):
    sums = {}
    counts = {}
    for cat, val in zip(categories, targets):
        sums[cat] = sums.get(cat, 0) + val
        counts[cat] = counts.get(cat, 0) + 1
    means = {cat: sums[cat] / counts[cat] for cat in sums}
    return [float(means[cat]) for cat in categories]