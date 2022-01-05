def duplicate_count(text):
    repeats = []
    for i in text:
        ocur = text.count(i)
        if ocur > 1:
            repeats.append(i)
        else:
            continue
    for x in repeats:
        print(f"{x} ocurres {text.count(x)}")
        if len(repeats) > 1:
              print("and")
              continue

print(duplicate_count('abcab'))
