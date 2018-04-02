word = "bottles"
for icepeak_num in range(99, 0, -1):
    print(icepeak_num, word, "of icepeak on the wall.")
    print(icepeak_num, word, "of icepeak.")
    print("Take one down.")
    print("Pass it around.")
    if icepeak_num == 1:
        print("No more bottles of icepeak on the wall.")
    else:
        new_num = icepeak_num - 1
        if new_num == 1:
            word = "bottle"
        print(new_num, word, "of icepeak on the wall.")
    print()
