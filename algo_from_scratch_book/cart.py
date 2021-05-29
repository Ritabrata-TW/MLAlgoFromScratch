import sys


def gini_index(groups, target_classes):
    n_instances = sum(len(group) for group in groups)

    total_gini_index = 0
    for group in groups:

        if (len(group)) == 0:
            continue

        sum_proportion_class = 0
        for target_class in target_classes:
            count_class = 0
            for elem in group:
                if elem == target_class:
                    count_class += 1

            sum_proportion_class += (count_class / len(group)) ** 2

        gini_index_group = (1 - sum_proportion_class) * (len(group) / n_instances)
        total_gini_index += gini_index_group

    return total_gini_index


def test_split(dataset, index, value):
    left, right = [], []

    for row in dataset:
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)

    return left, right


def get_split(dataset):
    split_column_index, split_value, min_gini_index, groups = None, None, sys.maxsize, None

    for row_index in range(len(dataset)):
        for col_index in range(len(dataset[0]) - 1):
            left, right = test_split(dataset, col_index, dataset[row_index][col_index])
            # print(f"Splitting at {row_index} - {col_index}. Value of split - {dataset[row_index][col_index]}")
            # print("left -> ", left)
            # print("right ->", right)
            # print("\n")

            left_class_values = [row[-1] for row in left]
            right_class_values = [row[-1] for row in right]

            # print("Left classes -> ", left_class_values)
            # print("Right classes -> ", right_class_values)

            # TODO: Adjust for any number of classes by passing in unique class values
            gini_index_for_split = gini_index([left_class_values, right_class_values], [0, 1])
            # print("Corresponding gini index for split = ", gini_index_for_split)

            if gini_index_for_split < min_gini_index:
                split_column_index = col_index
                split_value = dataset[row_index][col_index]
                min_gini_index = gini_index_for_split
                groups = (left, right)

    return {
        'column_index': split_column_index,
        'split_value': split_value,
        'min_gini_index': min_gini_index,
        'groups': groups
    }


def to_terminal(group):
    outcomes = [row[-1] for row in group]

    return max(outcomes, key=outcomes.count)


def split(node, max_depth, min_size, depth):
    left, right = node['groups']
    del (node['groups'])

    if not left or not right:
        node['left'] = node['right'] = to_terminal(left + right)
        return

    if depth > max_depth:
        node['left'], node['right'] = to_terminal(left), to_terminal(right)
        return

    if len(left) < min_size:
        node['left'] = to_terminal(left)
    else:
        node['left'] = get_split(left)
        split(node['left'], max_depth, min_size, depth + 1)

    if len(right) < min_size:
        node['right'] = to_terminal(right)
    else:
        node['right'] = get_split(right)
        split(node['right'], max_depth, min_size, depth + 1)


def build_tree(train, max_depth, min_size):
    root_node = get_split(train)
    split(root_node, max_depth, min_size, 1)
    return root_node


def print_tree(node, depth=0):
    if isinstance(node, dict):
        print('%s[X%d < %.3f]' % (depth * ' ', (node['column_index'] + 1), node['split_value']))
        print_tree(node['left'], depth + 1)
        print_tree(node['right'], depth + 1)
    else:
        print('%s[%s]' % (depth * ' ', node))


def predict(node, row):
    if row[node['column_index']] < node['split_value']:
        if isinstance(node['left'], dict):
            return predict(node['left'], row)
        else:
            return node['left']
    else:
        if isinstance(node['right'], dict):
            return predict(node['right'], row)
        else:
            return node['right']


def main():
    dataset = [[2.771244718, 1.784783929, 0],
               [1.728571309, 1.169761413, 0],
               [3.678319846, 2.81281357, 0],
               [3.961043357, 2.61995032, 0],
               [2.999208922, 2.209014212, 0],
               [7.497545867, 3.162953546, 1],
               [9.00220326, 3.339047188, 1],
               [7.444542326, 0.476683375, 1],
               [10.12493903, 3.234550982, 1],
               [6.642287351, 3.319983761, 1]]

    tree = build_tree(dataset, 3, 3)
    print_tree(tree)
    predicted = [predict(tree, row) for row in dataset]
    print(predicted)


if __name__ == '__main__':
    main()
