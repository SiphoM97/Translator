def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "c":
            translation += "b"
        else:
            translation += letter
    return translation

print(translate(input("Enter a phrase: ")))
