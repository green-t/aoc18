import os

## PART 1
#minutes=10;
## PART 2
minutes=560+(1000000000%28);

area=[];

with open("input.txt") as input_file:
	for line in input_file:
		area.append(list(line.strip()));
width=len(area[0]);

def getNeighbours(cone,ctwo):
	acreCount=0;
	treeCount=0;
	lumberCount=0;
	for i in range(3):
		for j in range(3):
			if i!=1 or j!=1:
				if cone+i-1>=0 and ctwo+j-1>=0:
					try:
					    gotdata = area[cone+i-1][ctwo+j-1];
					except IndexError:
					    gotdata = 'null'
					if gotdata==".": acreCount+=1;
					if gotdata=="|": treeCount+=1;
					if gotdata=="#": lumberCount+=1;
	return [acreCount,treeCount,lumberCount];

def draw(canvas):
	for line in canvas:
		strin="";
		for element in line:
			strin+=str(element);
		print(strin);
	return;

def getResValue(area):
	acreCount=0;
	treeCount=0;
	lumberCount=0;
	for x in range(width):
		for y in range(width):
			if area[x][y]==".":
				acreCount+=1;
			if area[x][y]=="|":
				treeCount+=1;
			if area[x][y]=="#":
				lumberCount+=1;
	return lumberCount*treeCount;

for minute in range(minutes):
	#print("Calculating minute",minute+1,"/",minutes)
	newState=[["." for y in range(width)] for x in range(width)];
	for x in range(width):
		for y in range(width):
			point=area[x][y];
			neighbours=getNeighbours(x,y);
			#print(x,y,point,neighbours);
			if point==".": 
				if neighbours[1]>=3: newState[x][y]="|";
				else: newState[x][y]=".";
			elif point=="|":
				if neighbours[2]>=3: newState[x][y]="#";
				else: newState[x][y]="|";
			elif point=="#":
				if neighbours[1]>0 and neighbours[2]>0: newState[x][y]="#";
				else: newState[x][y]=".";
			else: print("Error");
	area=newState;
	os.system('clear');
	print("Minute:",minute+1,"- Value:",getResValue(area));
	draw(area);
print("Done! Total resurce value after",minutes,"minutes is", getResValue(area));

