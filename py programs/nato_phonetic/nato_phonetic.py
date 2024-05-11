import pandas as pd

data = pd.read_csv("nato_phonetic.csv")

data_dict = {row.letter:row.code for (index,row) in data.iterrows()}


name = input("Enter your name").upper()
name_split = [letter for letter in name]
result = [data_dict[letter] for letter in name_split]

print(result)

