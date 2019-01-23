fabric=[[0 for x in range(1000)] for y in range (1000)];
counter=0;

#Part1
with open('input.txt') as input_file:
	for line in input_file:

		claim=line.split();
		
		id=claim[0][1:];
		
		margin=claim[2][:-1];
		margin=margin.split(",");
		lmar=int(margin[0]);
		tmar=int(margin[1]);
		
		size=claim[3];
		size=size.split("x");
		wid=int(size[0]);
		hei=int(size[1]);
		
		for x in range(wid):
			for y in range(hei):
				fabric[lmar+x][tmar+y]+=1;

for x in range (1000):
	for y in range (1000):
		if fabric[x][y]>1:
			counter+=1;

print("Square inches of fabric within two or more claims:",counter);

#Part2
with open('input.txt') as input_file:
	for line in input_file:

		claim=line.split();
		
		id=claim[0][1:];
		
		margin=claim[2][:-1];
		margin=margin.split(",");
		lmar=int(margin[0]);
		tmar=int(margin[1]);
		
		size=claim[3];
		size=size.split("x");
		wid=int(size[0]);
		hei=int(size[1]);

		unique=True;
		
		for x in range(wid):
			for y in range(hei):
				if fabric[lmar+x][tmar+y]>1:
					unique=False;

		if unique==True:
			print("Not overlapping: ID",id);