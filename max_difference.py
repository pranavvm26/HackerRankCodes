def max_difference(array_diff, len_array):
    diff_array = []
    for i_o in range(len_array):
        for i_i in range(i_o, len_array, 1):
            temp_array = array_diff[i_o:i_i+1]
            max_element = max(temp_array)
            min_element = min(temp_array)
            diff = max_element - min_element
            diff_array.append(diff)
    return sum(diff_array)


if __name__ == '__main__':
    len_array = input()
    array_diff = input()
    array_diff = array_diff.split(' ')
    for i, elem in enumerate(array_diff):
        if elem != '':
            array_diff[i] = int(elem)

    sum_res = max_difference(array_diff, int(len_array))
    print(sum_res)