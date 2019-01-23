## EXAMPLE INPUT
mouth=[0,0,1];
target=[10,10,1];
depth=510;

## PUZZLE INPUT
mouth=[0,0,1];
target=[13,704,1];
depth=9465;

xRange=target[0]*4;
yRange=target[1]*4;

geoIdx=[[0 for y in range(yRange)] for x in range(xRange)];
eroLvl=[[0 for y in range(yRange)] for x in range(xRange)];
regType=[[0 for y in range(yRange)] for x in range(xRange)];

riskLvl=0;

for x in range(xRange):	
	for y in range(yRange):
		if x==0:
			geoIdx[x][y]=y*48271;
		elif y==0:
			geoIdx[x][y]=x*16807;
		else:
			geoIdx[x][y]=eroLvl[x-1][y]*eroLvl[x][y-1];
		if x==target[0] and y==target[1]: geoIdx[x][y]=0;

		eroLvl[x][y]=(geoIdx[x][y]+depth)%20183;
		regType[x][y]=eroLvl[x][y]%3; # 0-rocky, 1-wet, 2-narrow
		if x<=target[0] and y<=target[1]:
			riskLvl+=regType[x][y];

riskLvl=riskLvl-regType[mouth[0]][mouth[1]]-regType[target[0]][target[1]];
print("Part 1 - Risk level:",riskLvl);


### PART 2 ###

# 0-none, 1-torch, 2-climbing
diInfo=[[[[False,float("inf"),[]] for t in range(3)] for y in range(yRange)] for x in range(xRange)]; #visited, dist, pre
diInfo[mouth[0]][mouth[1]][mouth[2]]=[False,0,[]];

searchX=[mouth[0]];
searchY=[mouth[1]];

def getNextNode():
	minDist=float("inf");
	for x in searchX:	
		relevantX=False;
		for y in searchY:
			for t in range(3):
				if diInfo[x][y][t][0]==False and diInfo[x][y][t][1]!=float("inf"):
					relevantX=True;
					if diInfo[x][y][t][1]<minDist:
						minDist=diInfo[x][y][t][1];
						nextNode=[x,y,t];
		if relevantX==False: searchX.remove(x);

	y=min(searchY);
	relevantY=False;
	for x in searchX:
		for t in range(3):
			if diInfo[x][y][t][0]==False and diInfo[x][y][t][1]!=float("inf"):
				relevantY=True;
	if relevantY==False: searchY.remove(y);

	return nextNode;

def getNeighbours(x,y,t):
	liste=[];
	liste.append([x,y,(t+1)%3]);
	liste.append([x,y,(t+2)%3]);
	if x>0: liste.append([x-1,y,t]);
	if y>0: liste.append([x,y-1,t]); 
	if x<xRange-1: liste.append([x+1,y,t]);
	if y<yRange-1: liste.append([x,y+1,t]);
	return liste; 

def edgeWeight(p,q):
	regQ=regType[q[0]][q[1]]
	if p[2]==q[2]:
		if p[2]==0:
			if regQ==0: weight=float("inf");
			elif regQ==1: weight=1;
			elif regQ==2: weight=1;
		elif p[2]==1:
			if regQ==0: weight=1;
			elif regQ==1: weight=float("inf");
			elif regQ==2: weight=1;
		elif p[2]==2:
			if regQ==0: weight=1;
			elif regQ==1: weight=1;
			elif regQ==2: weight=float("inf");
		else: print("ERROR");		
	else:
		if regQ==0: 
			if q[2]==0: weight=float("inf");			
			if q[2]==1: weight=7;
			if q[2]==2: weight=7;
		elif regQ==1:
			if q[2]==0: weight=7;		
			if q[2]==1: weight=float("inf");
			if q[2]==2: weight=7;
		elif regQ==2:
			if q[2]==0: weight=7;			
			if q[2]==1: weight=7;
			if q[2]==2: weight=float("inf");
		else: print("ERROR");
	return weight;

running=True;
while running:
	curNode=getNextNode();
	if curNode==target: running=False;
	x=curNode[0];
	y=curNode[1];
	t=curNode[2];
	print("Calculation node",curNode,"X-Search:",min(searchX),"-",max(searchX),"Y-Search:",min(searchY),"-",max(searchY),"    ", end="\r");
	diInfo[x][y][t][0]=True;
	neighbours=getNeighbours(x,y,t);
	
	for neighbour in neighbours:
		if neighbour[0] not in searchX: searchX.append(neighbour[0]);
		if neighbour[1] not in searchY: searchY.append(neighbour[1]);
		if diInfo[neighbour[0]][neighbour[1]][neighbour[2]][0]==False:
			summ=diInfo[x][y][t][1]+edgeWeight(curNode,neighbour);
			if diInfo[neighbour[0]][neighbour[1]][neighbour[2]][1]>summ:
				diInfo[neighbour[0]][neighbour[1]][neighbour[2]][1]=summ;
				diInfo[neighbour[0]][neighbour[1]][neighbour[2]][2]=[x,y,t];
				

print("Part 2 - The fastest way to the target takes",diInfo[target[0]][target[1]][target[2]][1],"minutes.          ");