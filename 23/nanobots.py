nanobots=[];

manhattan=lambda p,q: abs(p[0]-q[0])+abs(p[1]-q[1])+abs(p[2]-q[2]);

with open("testinput.txt") as input_file:
	for line in input_file:
		line=line.replace("<"," ").replace(">"," ").replace(","," ").replace("="," ");
		line=line.split();
		nanobots.append([int(line[1]),int(line[2]),int(line[3]),int(line[-1])]);

strongest=[0,0];
maxx, maxy, maxz, i=0,0,0,0;
for bot in nanobots:
	if bot[0]>maxx:maxx=bot[0];
	if bot[1]>maxy:maxy=bot[1];
	if bot[2]>maxz:maxz=bot[2];
	if bot[3]>strongest[1]:
		strongest=[i,bot[3]];
	i+=1;

print("Strongest nanobot is", strongest[0],"with a signal radius of",strongest[1]);

inRange,notInRange=0,0;
for bot in nanobots:
	distance=manhattan(nanobots[strongest[0]],bot);
	if distance<=strongest[1]:
		inRange+=1;
	else:
		notInRange+=1;

print(inRange,"of",len(nanobots),"are in its range.")
print(notInRange,"of",len(nanobots),"are not in its range.\n")

grid=[[[0 for z in range(maxz+1)] for y in range(maxy+1)] for x in range(maxx+1)];

bestPoint=[maxx,maxy,maxz,0]
for x in range(maxx+1):
	print("Calculating x",x,"of",maxx,end="\r");
	for y in range(maxy+1):
		for z in range(maxz+1):
			for bot in nanobots:
				distance=manhattan([x,y,z],bot);
				if distance<=bot[3]:
					grid[x][y][z]+=1;
			if grid[x][y][z]>bestPoint[3]:
				bestPoint=[x,y,z,grid[x][y][z]];
			if grid[x][y][z]==bestPoint[3]:
				if manhattan([0,0,0],[x,y,z])<manhattan([0,0,0],bestPoint):
					bestPoint=[x,y,z,grid[x][y][z]];

print("Best Point:",bestPoint[:3],"with a distance of",manhattan([0,0,0],bestPoint));