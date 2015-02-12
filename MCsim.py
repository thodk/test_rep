import random, matplotlib.pyplot as plt

random.seed(10)
def exe(NumTrials):
	
	x=0
	y=0
	for n in range(NumTrials):
		if random.random() <= 0.05:
			x+=1
		else:
			y+=1

	return x
	

X=[]; Y=[]
for i in range(10000):
	#print i
	x = exe(100)
	n = round(x*52./100, 0)
	print n
	X.append(n)
	Y.append(x)


W = [1./len(X)]*len(X)

plt.figure(1)
plt.hist(X, cumulative = 0, bins=[1,2,3,4,5,6,7,8,9,10,11,12,13,14], weights=W, align="left", color="blue")
plt.title("Probability : P(Number of genes = N)", fontsize=24)
plt.xlim(0,14)
plt.xlabel("N: Number of randomly selected genes as significant", fontsize=20)
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
plt.ylabel("Probability", fontsize=20, rotation=90)
plt.show()


plt.figure(2)
plt.hist(X, cumulative = -1, bins=[1,2,3,4,5,6,7,8,9,10,11,12,13,14], weights=W, align="left", color="blue")
plt.title("Cumulative Probability : P(Number of genes >= N)", fontsize=24)
plt.xlim(0,14)
plt.xlabel("N: Number of randomly selected genes as significant", fontsize=20)
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
plt.ylabel("Probability", fontsize=20, rotation=90)
plt.show()








