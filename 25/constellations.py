fixPoints=[];

def manhattan(p,q):
	return(abs(p[0]-q[0])+abs(p[1]-q[1])+abs(p[2]-q[2])+abs(p[3]-q[3]));


with open("input.txt") as input_file:
	for line in input_file:
		line=line.replace(","," ");
		line=line.split();
		fixPoints.append([int(line[0]),int(line[1]),int(line[2]),int(line[3]),0]);

constNr=1;
running=True;
newConst=True;

while running:
	running=False;
	working=False;
	for point1 in fixPoints:
		if point1[4]==0:
			running=True;
			if newConst==True:
				point1[4]=constNr;
				maxConst=constNr;
				newConst=False;

		
		if point1[4]==constNr:
			for point2 in fixPoints:
				if manhattan(point1,point2)<=3 and point2[4]==0:
					point2[4]=point1[4];
					working=True;

	if working==False: 
		constNr+=1;
		newConst=True;

	print(maxConst,"constellations found yet.", end="\r");

#for point1 in fixPoints: print(point1);
print("Done. The fixed points are forming",maxConst,"constellations.");


