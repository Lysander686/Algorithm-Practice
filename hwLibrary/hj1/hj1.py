def get_len():
    input_str = input()
    word = input_str.strip().split(' ')[-1]
    if len(word) > 5000 or ((len1:=len(word)) == 0):
        return 0
    print(len1)
    return len(word)

get_len()