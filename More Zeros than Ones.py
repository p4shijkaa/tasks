def more_zeros(s):
    total = []
    for i in s:
        if bin(ord(i))[2:].count("0") > bin(ord(i))[2:].count("1"):
            if i not in total:
                total.append(i)
            else:
                continue

    return total


print(more_zeros('thequickbrownfoxjumpsoverthelazydog'))