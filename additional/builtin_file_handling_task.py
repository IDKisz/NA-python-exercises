# Write a program that prints sorted list of words from three_rings.txt
# 
# words should be unique (ignore case-sensitive)
# words should not have any dots
# words should not have any commas

# put your code here


def unique_words(text):
    unique_list = []
    for word in text:
        word = word.replace(".", "")
        word = word.replace(",", "")
        if word in unique_list:
            pass
        else:
            unique_list.append(word)
    return sorted(unique_list)


with open('../additional/three_rings.txt', 'r') as tr_file:
    list_of_all_words = [word for line in tr_file for word in line.split()]

print(unique_words(list_of_all_words))
