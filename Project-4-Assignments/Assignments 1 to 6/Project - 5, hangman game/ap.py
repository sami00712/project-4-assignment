
 
import random

words = [
    "apple", "banana", "cherry", "grape", "orange", "peach", "pear", "plum", "mango", "melon",
    "apricot", "avocado", "blueberry", "blackberry", "strawberry", "raspberry", "pineapple", "coconut", "kiwi", "lemon",
    "lime", "nectarine", "papaya", "pomegranate", "watermelon", "fig", "guava", "jackfruit", "lychee", "passionfruit",
    "carrot", "broccoli", "cucumber", "spinach", "tomato", "potato", "pumpkin", "onion", "garlic", "lettuce",
    "cabbage", "celery", "eggplant", "pepper", "radish", "zucchini", "asparagus", "artichoke", "cauliflower", "beetroot",
    "kangaroo", "elephant", "giraffe", "rhinoceros", "hippopotamus", "crocodile", "alligator", "chameleon", "penguin", "flamingo",
    "ostrich", "parrot", "peacock", "squirrel", "hedgehog", "dolphin", "whale", "octopus", "shark", "seahorse",
    "mountain", "valley", "desert", "rainforest", "volcano", "island", "waterfall", "ocean", "river", "lake",
    "planet", "galaxy", "asteroid", "comet", "meteor", "blackhole", "nebula", "quasar", "supernova", "satellite",
    "robot", "android", "cyborg", "algorithm", "binary", "database", "programming", "software", "hardware", "encryption",
    "keyboard", "monitor", "mouse", "printer", "speaker", "laptop", "tablet", "internet", "website", "server"
]

# Select a random word
word = random.choice(words)
guess_letters = []
attempts = 6

print("🚦 Welcome To Hangman Game \n")
print("_ " * len(word))  

while attempts > 0:
    guess = input("Guess the letters: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Write one alphabet only!")
        continue
    if guess in guess_letters:
        print("🔁 You already guessed this letter!")
        continue
    
    guess_letters.append(guess)

    # Check if the letter is in the word
    if guess in word:
        print("✅ Correct guess!!")
    else:
        attempts -= 1
        print(f"❌ Wrong guess! {attempts} attempts left.")

    # Update display word
    display_word = " ".join([letter if letter in guess_letters else "_" for letter in word])
    print(display_word)

    # Check win condition
    if "_" not in display_word:
        print(f"🎉 Congratulations!! The correct word is '{word}'")
        break

# If loop exits without a win, print game over
if "_" in display_word:
    print(f"💀 Game over! The correct word was '{word}'.")
