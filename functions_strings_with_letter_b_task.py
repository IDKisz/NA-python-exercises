# Create a function, which takes strings list and returns only those strings which start from letter "b".
# - Check this function on file three_rings.txt.


# put your code here

def word_with_b(text):
    for word in text:
        if word[0] == "b":
            print(word, end=' ')

with open('../exercises/three_rings.txt', 'r') as tr_file:
    list_of_all_words = [word for line in tr_file for word in line.split()]
    word_with_b(list_of_all_words)
    print()
    print(list_of_all_words)