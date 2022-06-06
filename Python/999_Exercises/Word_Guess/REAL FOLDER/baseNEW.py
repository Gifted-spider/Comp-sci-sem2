import random
list_words = []
with open('allow_words.txt') as f:
    for line in f:
        l = line.strip()
        list_words.append(l)

num =(random.randrange(12973))
ans = list_words[num]

for x in range (0,6):
    guess = input("Guess a five letter word: ")
    if guess == ans:
        print("You guessed it!")
        break
    else:
        print('Try again')

if guess == ans:
    f.close
else:
    print(ans)
        
f.close()
