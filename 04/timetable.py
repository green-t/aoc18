dataset, timetable, tablerow, guardinfo=[],[],[],[];
maxid, mostsleep_min1, mostsleep_min2=0,0,0;

with open('input.txt') as input_file:
	for line in input_file:
		line=line.split(" ",2);
		line[0]=line[0][1:];
		line[1]=line[1][:-1];

		if "Guard" in line[2]:
			string=line[2].split();
			string=int(string[1][1:]);
			line.append(string);
			line[2]=1;
		elif "falls" in line[2]:
			line[2]=2;
			line.append(0);
		elif "wakes" in line[2]:
			line[2]=3;
			line.append(0);
		dataset.append(line);

dataset=sorted(dataset);
 
for line in dataset:

	hour=int(line[1][:2]);
	minute=int(line[1][3:]);

	#WächterIn erscheint
	if line[2]==1:
		#letzte Reihe speichern
		if len(tablerow)!=0:
			timetable.append(tablerow);
		
		#neue Reihe generieren
		if hour==23:		
			tablerow=[0 for x in range(60)];
		elif hour==00:
			tablerow=[1 for x in range(60)];
			for x in range(60-minute):
				tablerow[x+minute]=0;			
		else: 
			print("ERROR - hour not 00 or 23 on Line", dataset.index(line), ":",line[1][:2] );

		#ID anhängen
		tablerow.append(int(line[3]));
		if line[3]>maxid: maxid=line[3];
		
	#WächterIn  schläft ein
	if line[2]==2:
		for x in range(60-minute):
			tablerow[x+minute]=1;
	#WächterIn wacht auf
	if line[2]==3:
		for x in range(60-minute):
			tablerow[x+minute]=0;
	
timetable.append(tablerow);

for i in range(maxid+1):
	sleeptime, bestmin=0,0;
	mincount=[0 for x in range(60)];
	for line in timetable:
		if line[60]==i:
			j=0;
			for minute in line[:60]:
				sleeptime+=minute;
				mincount[j]+=minute;
				j+=1;

	for minute in mincount:
		if minute>bestmin:
			bestmin=minute;
			minindex=mincount.index(minute);	

	if sleeptime!=0:		
		guardinfo.append([i,sleeptime,minindex,bestmin]);
		if sleeptime>mostsleep_min1:
			bestGuard1=[i,sleeptime,minindex,bestmin];
			mostsleep_min1=sleeptime;
		if bestmin>mostsleep_min2:
			bestGuard2=[i,sleeptime,minindex,bestmin];
			mostsleep_min2=bestmin;

print("Strategy 1: \nMost sleeping guard:", bestGuard1[0]);
print("Best time: 0:", bestGuard1[2]);
print("Result:", bestGuard1[2]*bestGuard1[0]);

print("\nStrategy 2: \nMost sleeping guard:", bestGuard2[0]);
print("Best time: 0:", bestGuard2[2]);
print("Result:", bestGuard2[2]*bestGuard2[0]);