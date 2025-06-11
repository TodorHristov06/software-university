def even_odd_filter(**kwargs):
    result = {}

    for key, values in kwargs.items():
        if key == "even":
            result[key] = [n for n in values if n % 2 == 0]
        elif key == "odd":
            result[key] = [n for n in values if n % 2 != 0]

    sorted_result = dict(sorted(result.items(), key=lambda x: len(x[1]), reverse=True))

    return sorted_result
