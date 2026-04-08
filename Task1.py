import random

words = ["apple", "tiger", "chair", "table", "phone"]

word = random.choice(words)
guessed = ["_"] * len(word)

attempts = 6
guessed_letters = []

print("Welcome to Hangman Game!")

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print("Attempts left:", attempts)

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("Already guessed!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Correct guess 👍")
    else:
        attempts -= 1
        print("Wrong guess ❌")

# Final result
if "_" not in guessed:
    print("\n🎉 You Win! Word is:", word)
else:
    print("\n💀 You Lose! Word was:", word)