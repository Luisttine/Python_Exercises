players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
av = sum(players)/len(players)

std = [(players[i] - av)**2 for i in range(0, len(players))]
std = ((sum(std))/len(players))**0.5

low, high = av-std, av+std
count = len([x for x in players if low < x < high])
print(count)

