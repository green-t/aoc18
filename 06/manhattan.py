# Berrechnung der Manhattan Distance
manhattan = lambda p1,p2,q1,q2: abs(p1-q1)+abs(p2-q2);

coord=[];
pointid=0;

# Input in Array übertragen
with open("input.txt") as input_file:
	for line in input_file:
		pointid+=1;
		string=line.split();
		point=[pointid,int(string[0][:-1]),int(string[1]),0];
		coord.append(point);		

# Grid-Größe bestimmen
gridx, gridy=0,0;
for point in coord:
	if point[1]>gridx: gridx=point[1];
	if point[2]>gridy: gridy=point[2];
gridx+=1;
gridy+=1;

# Grid bauen
print("Building grid...")
grid=[[0 for y in range(gridy)] for x in range (gridx)];
print("Gridsize:",gridx,"x",gridy);

# Part1
# Grid befüllen
print("Calculating distances...")
for x in range(gridx):
	print(x,"of",gridx,"rows completed...", end="\r");
	for y in range (gridy):
		nearest=[0,(gridx+gridy)];
		for point in coord:
			dist=manhattan(x,y,point[1],point[2]);
			if dist==nearest[1]: nearest[0]=0;				
			elif dist<nearest[1]: nearest=[point[0],dist];			
		grid[x][y]=nearest[0];	

# Unendliche Flächen markieren
print("Finding infinite areas...")
for x in range(gridx):
	for y in range (gridy):
		if x==0 or x==gridx-1 or y==0 or y==gridy-1:
			if grid[x][y]!=0:
				pointidx=(grid[x][y])-1;
				coord[pointidx][3]=1;

# Fläche berechnen
print("Calculating areas...");
bestpoint=coord[0];
for point in coord:
	if point[3]==0:
		occ=0;
		for row in grid: occ+=row.count(point[0]);
		point.append(occ);
		if occ>bestpoint[4]: bestpoint=point;
	else: point.append(0);	

print("\nPart 1\nBiggest area (",bestpoint[4],") is around point",bestpoint[0]);


# Part2
# Grid befüllen
print("\nCalculating distances...")
counter=0;
for x in range(gridx):
	print(x,"of",gridx,"rows completed...", end="\r");
	for y in range (gridy):
		summe=0;
		for point in coord:
			dist=manhattan(x,y,point[1],point[2]);
			summe+=dist;			
		grid[x][y]=summe;
		if summe<10000: counter+=1;			

print("                             ");
print("Part 2\nSize of the region:", counter);