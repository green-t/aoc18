points=[];

def draw(points, time):
	state=[];
	
	print("\nPattern found after",time,"seconds !\n");

	for point in points:
		state.append([(point[0]+point[2]*time),(point[1]+point[3]*time)]);

	minx=state[0][0];
	miny=state[0][1];
	maxx=minx;
	maxy=miny;
	xcorr, ycorr=0,0;

	for point in state:
		if point[0]<minx: minx=point[0];
		if point[1]<miny: miny=point[1];
		if point[0]>maxx: maxx=point[0];
		if point[1]>maxy: maxy=point[1];

	if minx<0:
		xcorr=abs(minx);		
	else:
		xcorr=(-minx);
	if miny<0:
		ycorr=abs(miny);
	else:
		ycorr=(-miny);
	maxx+=xcorr;
	maxy+=ycorr;

	canvas=[[" " for x in range(maxx+1)] for y in range(maxy+1)];

	for point in state:
		canvas[point[1]+ycorr][point[0]+xcorr]="#";

	for line in canvas:
		print(''.join(line));
	

with open("input.txt") as input_file:
	for line in input_file:
		strn=line.replace("<"," ").replace(">"," ").replace(","," ").split();

		x=int(strn[1]);
		y=int(strn[2]);
		vx=int(strn[4]);
		vy=int(strn[5]);

		points.append([x,y,vx,vy]);
		
running=True;
i=1;
neighbours=[];

while running:
	curState=[];
	i+=1;
	counter=0;

	for point in points:
		curState.append([(point[0]+point[2]*i),(point[1]+point[3]*i)]);
	for point in curState:
		if [point[0]-1,point[1]] in curState: counter+=1;
		if [point[0]+1,point[1]] in curState: counter+=1;
		if [point[0],point[1]-1] in curState: counter+=1;
		if [point[0],point[1]+1] in curState: counter+=1;
	neighbours.append(counter);
	print("Second",i,"-",counter,"neighbourhoods found",end="\r");

	if len(neighbours)>3:
		if 2*neighbours[-1]<neighbours[-3] and neighbours[-2]<neighbours[-3]:
			running=False;
			draw(points, i-2);
		if neighbours[-1]==neighbours[-2]:
			i+=7;
		