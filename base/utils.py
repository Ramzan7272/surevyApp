def calculate_the_stats(queryset):
    list_of_answers = [i.answers for i in queryset]
    most_common = []

    for i in list_of_answers:
        i = list(i.values())
        if i.count('A') == len(i) / 2:
            most_common.append('L')
        else:
            most_common.append(max(i, key=i.count))

    if len(most_common) == 0:
        return None

    none_depressed = calculate_percentage(most_common, 'A')
    depressed = calculate_percentage(most_common, 'B')
    indefinite = calculate_percentage(most_common, 'L')

    return [none_depressed, depressed, indefinite]


def calculate_percentage(list, val):
    return int((list.count(val) / len(list)) * 100)
