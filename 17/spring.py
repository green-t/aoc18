clay=[];
spring=[500,0];
minx,maxx,miny,maxy=spring[0],spring[0],float("inf"),spring[1];

with open('input.txt') as input_file:
	for line in input_file:
		line=line.replace("="," ").replace(","," ").replace("."," ").split();
		if line[0]=="x":
			x=int(line[1]);
			for y in range(int(line[3]),int(line[4])+1):
				clay.append([x,y]);
				if y<miny: miny=y;
				if y>maxy: maxy=y;
			if x<minx: minx=x;
			if x>maxx: maxx=x;
		elif line[0]=="y":
			y=int(line[1]);
			for x in range(int(line[3]),int(line[4])+1):
				clay.append([x,y]);
				if x<minx: minx=x;
				if x>maxx: maxx=x;
			if y<miny: miny=y;
			if y>maxy: maxy=y;
		else: 
			print ("ERROR! Line not valid:",line)

grid=[["." for y in range(maxy+1)] for x in range(maxx+10)];
print("Hight of the grid:",maxy);
grid[spring[0]][spring[1]]="+";



for element in clay:
	grid[element[0]][element[1]]="#";

water=[[spring[0],spring[1],0,0]];

running=True;
while running:

	running=False;

	for drop in water:

		# Überspringe Wasser am unteren Ende des Grids,
		# oft untersuchte Elemente (>1024 mal)
		# sowie ruhendes Wasser, dass von ruhendem Wasser umgeben ist
		if drop[1]==maxy or drop[2]>1024 or drop[3]>1:
			continue;

		# Prüge ob links und rechts vom fließenden Wasser eine Abgrenzung ist.
		# Falls ja, wandele es zu stehendem Wasser um.
		if grid[drop[0]][drop[1]]=="|":
			drop[2]+=1;
			left, right, stop=False,False,False;
			i=1;
			while not stop:
				if grid[drop[0]-i][drop[1]]=="#": left=True;
				elif grid[drop[0]-i][drop[1]]==".": stop=True;
				if grid[drop[0]+i][drop[1]]=="#": right=True;
				elif grid[drop[0]+i][drop[1]]==".": stop=True;

				if left and right: 
					grid[drop[0]][drop[1]]="~";
					stop=True;
					running=True;
				i+=1;

		# Prüfe ob neben stehendem Wasser noch fließendes existiert.
		# Falls ja, wandele es zu stehendem Wasser um.
		if grid[drop[0]][drop[1]]=="~":
			if grid[drop[0]-1][drop[1]]=="|":
				grid[drop[0]-1][drop[1]]="~";
				drop[3]+=1;
				running=True;
			if grid[drop[0]+1][drop[1]]=="|":
				grid[drop[0]+1][drop[1]]="~";
				drop[3]+=1;
				running=True;

		# Unter fließendem Wasser ist Sand
		if grid[drop[0]][drop[1]+1]==".":
			grid[drop[0]][drop[1]+1]="|"
			water.append([drop[0], drop[1]+1,0,0]);
			running=True;
		# Unter fließendem Wasser ist Fels oder stehendes Wasser
		elif grid[drop[0]][drop[1]+1]=="#" or grid[drop[0]][drop[1]+1]=="~":
			if grid[drop[0]-1][drop[1]]==".":
				grid[drop[0]-1][drop[1]]="|"
				water.append([drop[0]-1, drop[1],0,0]);
				running=True;
			if grid[drop[0]+1][drop[1]]==".":
				grid[drop[0]+1][drop[1]]="|"
				water.append([drop[0]+1, drop[1],0,0]);
				running=True;
	
	print("Current Y-Index:",water[-1][1],"     ", end="\r");	

counter1,counter2=0,0;
for y in range(maxy+1):
	strin="";
	for x in range(maxx+1):
		strin+=grid[x][y]
		if grid[x][y]=="|" and y>=miny: counter1+=1;
		if grid[x][y]=="~": counter2+=1;
	#print(strin);

print("Tiles that water can reach:",counter1+counter2);
print("Tiles where the water stays:", counter2);