gridSN=int(input("Please enter grid serial number: "));
gridSize=300;
grid=[[0 for y in range(gridSize)] for x in range(gridSize)];

for x in range(gridSize):
	for y in range(gridSize):
		rackID=x+11;
		cellPowerLevel=int(str((rackID*(y+1)+gridSN)*rackID)[-3])-5;
		grid[x][y]=cellPowerLevel;

topTotalPower=[0,0,0,0];
for s in range(gridSize):
	squareSize=s+1;
	print("Checking square size of",squareSize,"x",squareSize)
	for x in range(gridSize-s):
		for y in range(gridSize-s):
			summ=0;
			for zx in range(squareSize):
				for zy in range(squareSize):
					summ+=grid[x+zx][y+zy];
			if summ>topTotalPower[2]: topTotalPower=[x,y,summ,squareSize];

	print("Best square of fuel cells so far:\nX:",topTotalPower[0]+1,"- Y:",topTotalPower[1]+1,"with a total power of", topTotalPower[2],"at a square size of",topTotalPower[3],"\n")

print("Done!");