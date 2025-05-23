list1 = ["1221", "abab", "bcb", "989"]


def matching(counting):
    count = 0
    list2 = []
    for word in counting:
        if len(word) > 0 and word[0] == word[-1]:
            count = count + 1
            list2.append(word)
    print("the list with the characters with first and last character same is", list2)
    return count


same_character = matching(list1)
print("number of words with the same charaters are", same_character)
