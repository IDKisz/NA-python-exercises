# Create a function, which takes list of strings and exchanges any letter "o" into "."
# - Check this function on file three_rings.txt.

# put your code here


def change_o_function(list):
    for words in list:
        if str("o") in words:
            # print(word)
            print(words.replace("o", "."), end=' ')
        else:
            print(words, end=' ')


with open('../exercises/three_rings.txt', 'r') as tr_file:
    list_of_all_words = [word for line in tr_file for word in line.split()]
    change_o_function(list_of_all_words)
    print()
    print(list_of_all_words)
