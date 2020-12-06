import os


def get_unique_answers(groups):
    sanitised_groups = [group.replace('\n', '') for group in groups]
    return sum([ len(set(group)) for group in sanitised_groups])


def get_duplicate_answers(groups):
    intersections = [
        len (
            set.intersection(*map(set, group.split("\n")))
        )
        for group in groups
    ]
    return sum(intersections)


def get_group_counts():
    path = os.path.join(os.path.dirname(__file__), 'inputs.txt')
    with open(path, 'r') as file_handle:
        groups = file_handle.read().split('\n\n')
        return [
            get_unique_answers(groups),
            get_duplicate_answers(groups)
        ]


if __name__ == "__main__":
    unique, duplicate = get_group_counts()

    print(f'Solution to part a: {unique}')
    print(f'Solution to part b: {duplicate}')
