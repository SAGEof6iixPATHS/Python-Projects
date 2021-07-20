from random import choice

questions = ["Why is the sky is blue?","Why cannot we fly?","What colour is the water?"]

question = choice(questions)
print(question)
answer = input("--> ").strip().lower()

while answer != "just because":
    print("But Why?")
    answer = input("--> ").strip().lower()

print("Oh... Okay!")
