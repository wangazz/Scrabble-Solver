## Dictionary from https://github.com/dwyl/english-words ####

import pandas as pd

def alphasort(input):
    output = ""
    for char in sorted(input):
        output += char
    return output

with open('words_alpha.txt') as dict_file:
    words = list(dict_file.read().split())
sorted_words = []
for i in range(len(words)):
    sorted_words.append(alphasort(words[i]))
    print(words[i], sorted_words[i])
print(sorted_words)



# Load dictionary

# words = pd.read_csv("words_alpha.csv")
# words.columns = ["words"]
# sorted_list = []
# for i in range(len(words)):
#     sorted_list.append(alphasort(words.iloc[i][0]))
# words["alphasort"] = sorted_list

# print(words)

    


# Main loop
while(True):
    letters = input("Enter letters: ")

    # Validation stage
    if letters.isalpha() == False:
        print("Invalid input.")
    else:
        print(words[10:15])