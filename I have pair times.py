def pair_times(array):
    if not array or len(array) < 3:
        return False

    length_arr = len(array)
    last = array[-1]
    has_pair = False

    for i in range(length_arr - 1):
        if array[i] * array[i + 1] == last:
            has_pair = True
            break

    return has_pair

arr = input()
eval_arr = eval(arr)
result = pair_times(eval_arr)
print(result)
