players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]
av = sum(players)/len(players)

obs = [(players[i] - av)**2 for i in range(0, len(players))]
obs = ((sum(obs))/len(players))**0.5

print(obs)
