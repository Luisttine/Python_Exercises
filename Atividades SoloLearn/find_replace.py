text = "Amy has 128 dollars, while David has 54 dollars. Amy is going to the zoo. David watches soccer."
def repl(find, raplace, text):
    count = text.count(find)
    while find in text:
        text = text.replace(find, replace)
    print(count)
    print(text)

find = input()
replace = input()

print(repl(find, replace, text))
