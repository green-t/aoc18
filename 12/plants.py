pos, neg, gens=[],[],[];
nrOfGens=20;
nrOfGensSample=1000;
askedGen=50000000000;
lastsumm=0;

with open("input.txt") as input_file:
	for line in input_file:
		line=line.replace(".","0").replace("#","1").split();
		if line==[]:
			pass;
		elif line[0]=="initial":
			initState=list(line[2]);
		elif int(line[2])==1:
			pos.append(line[0]);
		elif int(line[2])==1:
			neg.append(line[0]);

lastGen=[int(e) for e in initState];
corr=0;
for i in range(nrOfGensSample):
	newGen=[];
	for p in range(10):
		if lastGen[p]==1:
			if p<5: 
				for q in range(5-p): lastGen.insert(0,0);
				corr-=(5-p);
				break;
			else:
				for q in range(p-5): del lastGen[0];
				corr+=(p-5);
				break;
	for p in range(10):
		r=p+1;
		if lastGen[-r]==1:
			if r<6: 
				for q in range(6-r): lastGen.append(0);
				break;
			else:
				for q in range(r-6): del lastGen[-1];
				break;				

	for j in range(len(lastGen)-4):
		position=j+2;
		curStr=''.join(str(e) for e in lastGen[position-2:position+3]);
		if curStr in pos: newGen.append(1);		
		else: newGen.append(0);	
	corr+=2;
	lastGen=newGen;

	q=0;
	summ=0;
	for p in newGen:
		summ+=int(p)*(q+corr);
		q+=1
	gens.append([summ,(summ-lastsumm)]);
	lastsumm=summ;

#for i in range(len(gens)):print((i+1),gens[i]);
	if i==nrOfGens-1: print("Sum of pots in (",nrOfGens,"):",summ,"\n0-point correction:",corr);
	if i==nrOfGensSample-2: summBefore=summ;

afterSample=summ;
growingRate=summ-summBefore;
result=afterSample+(askedGen-nrOfGensSample)*growingRate;

print("Sum after",askedGen,"Generations (guessed):",result)




