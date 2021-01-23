import array
test_case_num = int(input())
arr = [0] * test_case_num

for i in range(test_case_num):
    one_line = input().split(' ')
    key = int(one_line[0])
    val = int(one_line[1])
    # if not arr[key]:
    arr[key] += val

for i in range(test_case_num):
    if arr[i] != 0:
        print(str(i)+' '+str(arr[i]))
