class X(): 
    def __init__(self, size): 
        self.adj = [ [0] * size for i in range(size)]
        self.size = size 
    
    def add_friend(self, x, y): 
        if x > self.size or y > self.size or x < 0 or y < 0: 
            print("Error") 
        else: 
            self.adj[x-1][y-1] = 1 
            self.adj[y-1][x-1] = 1 
        
    def remove_friend(self, x, y): 
        if x > self.size or y > self.size or x < 0 or y < 0: 
            print("Error") 
        else: 
            self.adj[x-1][y-1] = 0 
            self.adj[y-1][x-1] = 0 
            

x = X(5)

x.add_friend(1, 3) 
x.add_friend(1, 5)
x.add_friend(2, 5)
x.add_friend(2, 4)
x.add_friend(4, 5)

n = int(input())
#your code goes here

a=0
for i in range(len(x.adj)):
	if i+1 == n:
		for j in x.adj[i]:
			if j==1:
				a+=1
print(a)
