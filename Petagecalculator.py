print("===================================")
print("      🐾 PET AGE CALCULATOR 🐾")
print("===================================")

name = input("Enter your pet's name: ")
pet = input("Enter your pet (dog/cat/rabbit/parrot/hamster): ")
age = int(input("Enter your pet's age: "))

if pet == "dog":
    human_age = age * 7
    thought = "Woof! I love going for walks and playing fetch! 🐶"

if pet == "cat":
    human_age = age * 6
    thought = "Meow! Time for a long nap in the sun. 🐱"

if pet == "rabbit":
    human_age = age * 8
    thought = "Hop! Hop! Carrots make my day! 🐰"

if pet == "parrot":
    human_age = age * 5
    thought = "Squawk! Can you teach me a new word? 🦜"

if pet == "hamster":
    human_age = age * 25
    thought = "Squeak! I love running on my tiny wheel! 🐹"

print("\n========== RESULT ==========")
print("Pet Name:", name)
print("Pet Type:", pet)
print("Pet Age:", age)
print("Equivalent Human Age:", human_age)
print("Pet Thought:", thought)
print("============================")

print("❤️ Thank you for using the Pet Age Calculator!")
print("🐾 Have a pawsome day!")