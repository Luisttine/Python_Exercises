contacts = {
    "David": ["123-321-88", "david@test.com"],
    "James": ["241-879-093", "james@test.com"],
    "Bob": ["987-004-322", "bob@test.com"],
    "Amy": ["340-999-213", "a@test.com"]
}
#your code goes here
name = input()
if name in contacts:
    print(list(contacts.get(name, "Not found"))[1])
else:
    print("Not found")

#O CERTO SERIA O MESMO IF MAS COM PRINT DIFERENTE
#print(contacts[name][1])
