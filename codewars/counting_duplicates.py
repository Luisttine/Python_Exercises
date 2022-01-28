def duplicate_count(text):
    text = text.lower()
    if not text:
        return 0
    repeats = []
    r = 0
    for i in text:
        if text.count(i) > 1:
            repeats.append(i)
            r = r+1
        text = text.replace(i,"")
        continue
    if not repeats:
        return 0
    else:
        return r
        

print(duplicate_count('abcab'))
