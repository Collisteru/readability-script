from readability import Readability
from tabulate import tabulate

import nltk
nltk.download('punkt') # My machine wants me to download this separately?

print("Paste the stories one-by-one into a file, with each story separated by a vertical bar (|) character.")

while True:
    filename = input("Input the name of a file to process, as in filename.txt\n")

    try:
        with open(filename, 'r') as f:
            content = f.read()
            break
    except:
        print("Error reading file. Did you choose the wrong filename?")
        continue

story_list = content.split('|')

# Input: The full text of the story as a single string.
def calculate_readability_scores(story_string):
    r = Readability(story_string)

    flesch_kincaid = r.flesch_kincaid()

    flesch_reading_ease = r.flesch()

    gunning_fog = r.gunning_fog()

    return [flesch_kincaid, flesch_reading_ease, gunning_fog]

# Set up return list

return_list = []
first_list_item = ["Story Number", "Flesch-Kincaid Readability Score", "Flesch Reading Ease", "Gunning Fog readability score"]
return_list.append(first_list_item)

story_num = 1
for story in story_list:
    r_scores_obj = calculate_readability_scores(story)
    
    list_item = [story_num, r_scores_obj[0].score, r_scores_obj[1].score, r_scores_obj[2].score]
    return_list.append(list_item)
    story_num += 1

print(tabulate(return_list))