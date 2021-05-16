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


def split(dataset, index, value):
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
            left, right = split(dataset, col_index, dataset[row_index][col_index])
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

    split_dict = get_split(dataset)
    print('Split: [X%d < %.3f] with gini index %.3f' % (
        (split_dict['column_index'] + 1), split_dict['split_value'], split_dict['min_gini_index']
    ))


if __name__ == '__main__':
    main()
