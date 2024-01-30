import os
import random
import markovify

text = ""

for subdir, dirs, files in os.walk("datasets"):
  for file in files:
    filepath = subdir + os.sep + file

    if filepath.endswith(".txt"):
      # print(filepath)
      with open(filepath) as f:
          text += f.read() + "\n"

text_model = markovify.Text(text.rstrip('\r\n'))

datasets = [text_model.make_sentence() for i in range(100)] 
datasets = [i for i in datasets if i is not None]
dataset = random.choice(datasets)

print(dataset)
