def get_dictionary_lists():
    dictionary_list = []
    file = open("dictionary.txt")
    word = file.readlines()
    for l in range(len(word)):
        dictionary_list.append(word[l].split()[1])
    return dictionary_list    