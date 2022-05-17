vac_nums = [0,0,0,0,0,
            1,1,1,1,1,1,1,1,
            2,2,2,2,
            3,3,3
            ]
#your code goes here
x = 0
for i in vac_nums:
    if i != 0: x += i
    else: continue
print(x/20)
