PLACEHOLDER = "[name]"

with open('./Input/Names/invited_names.txt') as names:
    new_name = names.readlines()
    print(new_name)


with open('./Input/Letters/starting_letter.txt') as letter:
    letter_content = letter.read()

    for name in new_name:
        strip_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER,strip_name)
        with open(f"./Output/ReadyToSend/letter_to_{strip_name}.txt",mode="w") as completed_letters:
            completed_letters.write(new_letter)

        # print(new_letter)
