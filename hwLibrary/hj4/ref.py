while True:
    try:
        s = input()
        while len(s) > 8:
            print(s[:8])
            s = s[8:]
        print(s.ljust(8, "0"))
    except:
        break