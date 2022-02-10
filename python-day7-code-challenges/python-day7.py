Challenge 1:
  
chosen_word = random.choice(word_list)

guess = input("guess a letter: ").lower()

for letter in chosen_word:
  if letter == guess:
    print("right")
  else:
    print("false")
