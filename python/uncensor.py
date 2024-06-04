def uncensor(txt, vowels):
    text_list = list(txt)  # make a list to manipulate
    vowel_index = 0  # initiate counter

    for i in range(len(text_list)):  # for i in range length of the list
        if text_list[i] == "*":  # if i is a *
            text_list[i] = vowels[vowel_index]  # replace * with the vowel correlating to the index
            vowel_index += 1  # increment index after

    return "".join(text_list)  # return the list