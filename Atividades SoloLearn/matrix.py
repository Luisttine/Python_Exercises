data = [
  [23, 11, 5, 14],
  [8, 32, 20, 5]
]
color = input()
#your code goes here
tot = 23+11+5+14+8+32+20+5

x = data[0][0] + data[1][0]
if color == "brown":
    perc = int((x/tot)*100)
elif color == "blue":
    x = data[0][1] + data[1][1]
    perc = int((x/tot)*100)
elif color == "green":
    x = data[0][2] + data[1][2]
    perc = int((x/tot)*100)
elif color == "black":
    x = data[0][3] + data[1][3]
    perc = int((x/tot)*100)
    
print(perc)
