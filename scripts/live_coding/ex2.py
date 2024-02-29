def check_anagram(word1, word2):
    if(sorted(word1)== sorted(word2)):
        print("The strings are anagrams.") 
    else:
        print("The strings aren't anagrams.")         





def check_anagram_dict(word1, word2):

    if len(word1) == len(word2):

        w1_dict = {}
        w2_dict = {}

        for index, char in enumerate(word1):
            w1_dict[index] = char

        for index, char in enumerate(word2):
            w2_dict[index] = char

        for value in w1_dict.values():
            if value not in w2_dict.values():
                return False
            w2_dict.pop()

        return True
    return False

    # print(w1_dict.values())
    # print(w2_dict.values())

    # return w1_dict.values() == w2_dict.values()

    


if __name__ == '__main__':
         
    w1 ="pots"
    w2 ="tpso"
    check_anagram(w1, w2)

    print(check_anagram_dict(w1, w2))