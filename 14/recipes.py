nrOfTrainings=int(input("Enter puzzle input: "));
match=[];
for e in list(str(nrOfTrainings).strip()): match.append(int(e));
nrOfElfs=2;

scores=[3,7];
elfs=[i for i in range(nrOfElfs)];

running=True;
running2=True;
while running or running2:
	summ=0;
	for elf in elfs:
		summ+=scores[elf];
	for e in str(summ).strip():
		scores.append(int(e));
	for i in range(len(elfs)):
		elfs[i]=(elfs[i]+scores[elfs[i]]+1)%len(scores);

	if len(scores)>nrOfTrainings+10 and running==True:
		running=False;
		relScores="".join(str(e) for e in scores[nrOfTrainings:nrOfTrainings+10]);

	if match==scores[-(len(match)):] and running2==True:
		running2=False;
		relScores2=len(scores[:-(len(match))]);
	elif match==scores[-(len(match)+1):-1] and running2==True:
		running2=False;
		relScores2=len(scores[:-(len(match)+1)]);

print("Part 1: Relevant scores:",relScores);
print("Part 2: Recipes on the left:",relScores2);

