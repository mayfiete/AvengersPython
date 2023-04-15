
text = input("Provide name of Superhero: ")

with open("app/hero_names.txt", "w") as file:
    file.write(text + "\n")

print("Superhero name saved to file.")
