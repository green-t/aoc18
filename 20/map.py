regex=[];
regex.append(["Test 1","^WNE$"]);
regex.append(["Test 2","^ENWWW(NEEE|SSE(EE|N))$"]);
regex.append(["Test 3","^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$"]);
regex.append(["Test 4","^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$"]);
regex.append(["Test 5","^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$"]);

with open('input.txt') as input_file:
	regex.append(["Puzzle",input_file.readline()]);

def antiDetour(strin):
	detours={"EW","NS","WE","SN"};
	running=True;
	while running:
		running=False;
		for detour in detours:
			if detour in strin:
				strin=strin.replace(detour,"");
				running=True;
	return strin;

def findFurthest(strin):
	directions={"N","W","S","E"};
	side=[0,0,0];
	i, furthest, sideIdx=0,0,0;

	running=True;
	while running:
		
		if strin[i] in directions:
		 	side[sideIdx]+=1;

		elif strin[i]=="^":
			pass;

		elif strin[i]=="(":
			temp=findFurthest(strin[i+1:]);
			side[sideIdx]+=temp[0];
			i+=temp[1]; 			
		elif strin[i]=="|":
			sideIdx+=1;
		elif strin[i]==")" or strin[i]=="$":
			running=False;
			furthest=max(side);
			return([furthest,i+1]);
		else: 
			print("ERROR! Unknown character!");
			break;
		
		
			
		#print(i, strin[i], strin, side);
		
		if i>=len(strin):
			running=False;
		i+=1;			
	
print("Part 1:")
for e in regex:
	print(e[0],"- Largest number of doors to reach a room:",findFurthest(antiDetour(e[1]))[0]);


