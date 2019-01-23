## PART 1
instr=["addr","addi","mulr","muli","banr","bani","borr","bori","setr","seti","gtir","gtri","gtrr","eqir","eqri","eqrr"];
samples=[];
sample=[];

# Daten (Part 1) einlesen und in Array überühren
with open("input.txt") as input_file:
	for line in input_file:
		if len(line)<=1:
			samples.append(sample);
			sample=[];
		elif "Before" in str(line) or "After" in str(line):
			row=[];
			strin=line.split();
			row=[int(strin[1][1]),int(strin[2][0]),int(strin[3][0]),int(strin[4][0])];
			sample.append(row);
		else: 
			row=[];
			for e in line.split(): row.append(int(e));
			sample.append(row);
	samples.append(sample);


# Daten gegen InstructionSet prüfen
instrSet=[];
for i in range(len(instr)):
	row=[];
	for e in instr:
		row.append(e);
	instrSet.append(row);

threeOrMore=0;
for sample in samples:
	before=sample[0];
	todo=sample[1];
	after=sample[2];

	i=0;
	counter=0;
	strin="";

	for i in range(len(instr)):
		check=False;

		#addr
		if i==0 and after[todo[3]]==before[todo[1]]+before[todo[2]]: check=True;
		#addi
		if i==1 and after[todo[3]]==before[todo[1]]+todo[2]: check=True;
		#mulr
		if i==2 and after[todo[3]]==before[todo[1]]*before[todo[2]]: check=True;
		#muli
		if i==3 and after[todo[3]]==before[todo[1]]*todo[2]: check=True;
		#banr
		if i==4 and after[todo[3]]==before[todo[1]]&before[todo[2]]: check=True;
		#bani
		if i==5 and after[todo[3]]==before[todo[1]]&todo[2]: check=True;
		#borr
		if i==6 and after[todo[3]]==before[todo[1]]|before[todo[2]]: check=True;
		#bori
		if i==7 and after[todo[3]]==before[todo[1]]|todo[2]: check=True;
		#setr
		if i==8 and after[todo[3]]==before[todo[1]]: check=True;
		#seti
		if i==9 and after[todo[3]]==todo[1]: check=True;
		#gtir
		if i==10 and after[todo[3]]==1 and todo[1]>before[todo[2]]: check=True;
		if i==10 and after[todo[3]]==0 and todo[1]<=before[todo[2]]: check=True;
		#gtri
		if i==11 and after[todo[3]]==1 and before[todo[1]]>todo[2]: check=True;
		if i==11 and after[todo[3]]==0 and before[todo[1]]<=todo[2]: check=True;
		#gtrr
		if i==12 and after[todo[3]]==1 and before[todo[1]]>before[todo[2]]: check=True;
		if i==12 and after[todo[3]]==0 and before[todo[1]]<=before[todo[2]]: check=True;
		#eqir
		if i==13 and after[todo[3]]==1 and todo[1]==before[todo[2]]: check=True;
		if i==13 and after[todo[3]]==0 and todo[1]!=before[todo[2]]: check=True;
		#eqri
		if i==14 and after[todo[3]]==1 and before[todo[1]]==todo[2]: check=True;
		if i==14 and after[todo[3]]==0 and before[todo[1]]!=todo[2]: check=True;
		#eqrr
		if i==15 and after[todo[3]]==1 and before[todo[1]]==before[todo[2]]: check=True;
		if i==15 and after[todo[3]]==0 and before[todo[1]]!=before[todo[2]]: check=True;

		if check:
			counter+=1;
			strin+=instr[i];
			strin+=" ";
		else:
			if instr[i] in instrSet[todo[0]]:
				idx=instrSet[todo[0]].index(instr[i]);
				del instrSet[todo[0]][idx];
	if counter>=3: threeOrMore+=1; 

print("Three or more (Part 1):",threeOrMore);

## PART 2
#Anhand der gesammelten Informationen die Opcodes zuordnen
running=True;
while running:
	running=False;
	for instr in instrSet:
		if len(instr)==1:
			j=0;
			for i in instrSet:
				if len(i)>1:
					if instr[0] in i:
						instrSet[j].remove(instr[0]);
						running=True;
				j+=1;

print("\nCalculated opcodes:");	
for i in range(len(instrSet)): print(i,instrSet[i]);

# Funktion zur berechnung schreiben		
def process(reg, todo):		
	if instrSet[todo[0]][0]=="addr": reg[todo[3]]=reg[todo[1]]+reg[todo[2]];
	elif instrSet[todo[0]][0]=="addi": reg[todo[3]]=reg[todo[1]]+todo[2];
	elif instrSet[todo[0]][0]=="mulr": reg[todo[3]]=reg[todo[1]]*reg[todo[2]];
	elif instrSet[todo[0]][0]=="muli": reg[todo[3]]=reg[todo[1]]*todo[2];
	elif instrSet[todo[0]][0]=="banr": reg[todo[3]]=reg[todo[1]]&reg[todo[2]];
	elif instrSet[todo[0]][0]=="bani": reg[todo[3]]=reg[todo[1]]&todo[2];
	elif instrSet[todo[0]][0]=="borr": reg[todo[3]]=reg[todo[1]]|reg[todo[2]];
	elif instrSet[todo[0]][0]=="bori": reg[todo[3]]=reg[todo[1]]|todo[2];
	elif instrSet[todo[0]][0]=="setr": reg[todo[3]]=reg[todo[1]];
	elif instrSet[todo[0]][0]=="seti": reg[todo[3]]=todo[1];
	elif instrSet[todo[0]][0]=="gtir":
		if todo[1]>reg[todo[2]]: reg[todo[3]]=1;
		else: reg[todo[3]]=0;
	elif instrSet[todo[0]][0]=="gtri":
		if reg[todo[1]]>todo[2]: reg[todo[3]]=1;
		else: reg[todo[3]]=0;
	elif instrSet[todo[0]][0]=="gtrr":
		if reg[todo[1]]>reg[todo[2]]: reg[todo[3]]=1;
		else: reg[todo[3]]=0;
	elif instrSet[todo[0]][0]=="eqir":
		if todo[1]==reg[todo[2]]: reg[todo[3]]=1;
		else: reg[todo[3]]=0;
	elif instrSet[todo[0]][0]=="eqri":
		if reg[todo[1]]==todo[2]: reg[todo[3]]=1;
		else: reg[todo[3]]=0;
	elif instrSet[todo[0]][0]=="eqrr": 
		if reg[todo[1]]==reg[todo[2]]: reg[todo[3]]=1;
		else: reg[todo[3]]=0;
	else: print("ERROR!");

	return reg;

# Funtion mit Trainingsdaten aus Part 1 testen
for sample in samples:
	erg=process(sample[0],sample[1]);
	if erg!=sample[2]:
		print("Error - In:",sample[0],"Instr.:",sample[1],instrSet[sample[1][0]][0],"Out:",erg,"Expected:",sample[2]);
	before=sample[0];
	todo=sample[1];
	after=sample[2];

# Daten aus Part 2 mit Funktion berechnen
register=[0,0,0,0]
with open("input2.txt") as input_file:
	for line in input_file:
		instructions=[];
		for e in line.split(): instructions.append(int(e));
		register=process(register, instructions);

print("\nThe register after executiong the test program:",register);
print("Solution for Part 2:",register[0]);