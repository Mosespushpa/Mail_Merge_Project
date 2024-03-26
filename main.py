PLACEHOLDER = "[name]"

with open("invited_names.txt") as f:
    names = f.readlines()


with open("starting_letter.txt") as l:
    letter_content = l.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER,stripped_name)
        with open(f"Letter_to_{stripped_name}.txt",mode="w") as file:
            file.write(new_letter)