instructions=[];
register=[1,0,0,0,0,0]

with open("input.txt") as input_file:
	for line in input_file:
		if line[0]=="#":
			ip_bind=int(line.split()[1]);
		else:
			row=[line.split()[0]]
			for e in line.split()[1:]:row.append(int(e));
			instructions.append(row);


def process(reg, todo):		
	if todo[0]=="addr": reg[todo[3]]=reg[todo[1]]+reg[todo[2]];
	elif todo[0]=="addi": reg[todo[3]]=reg[todo[1]]+todo[2];
	elif todo[0]=="mulr": reg[todo[3]]=reg[todo[1]]*reg[todo[2]];
	elif todo[0]=="muli": reg[todo[3]]=reg[todo[1]]*todo[2];
	elif todo[0]=="banr": reg[todo[3]]=reg[todo[1]]&reg[todo[2]];
	elif todo[0]=="bani": reg[todo[3]]=reg[todo[1]]&todo[2];
	elif todo[0]=="borr": reg[todo[3]]=reg[todo[1]]|reg[todo[2]];
	elif todo[0]=="bori": reg[todo[3]]=reg[todo[1]]|todo[2];
	elif todo[0]=="setr": reg[todo[3]]=reg[todo[1]];
	elif todo[0]=="seti": reg[todo[3]]=todo[1];
	elif todo[0]=="gtir":
		if todo[1]>reg[todo[2]]: reg[todo[3]]=1;
		else: reg[todo[3]]=0;
	elif todo[0]=="gtri":
		if reg[todo[1]]>todo[2]: reg[todo[3]]=1;
		else: reg[todo[3]]=0;
	elif todo[0]=="gtrr":
		if reg[todo[1]]>reg[todo[2]]: reg[todo[3]]=1;
		else: reg[todo[3]]=0;
	elif todo[0]=="eqir":
		if todo[1]==reg[todo[2]]: reg[todo[3]]=1;
		else: reg[todo[3]]=0;
	elif todo[0]=="eqri":
		if reg[todo[1]]==todo[2]: reg[todo[3]]=1;
		else: reg[todo[3]]=0;
	elif todo[0]=="eqrr": 
		if reg[todo[1]]==reg[todo[2]]: reg[todo[3]]=1;
		else: reg[todo[3]]=0;
	else: print("ERROR!");

	return reg;

running=True;
ip=0;
t=0;
while running:
	if ip==3 and register[2]<register[5]:
		modulo=register[5]%register[4];
		if register[4]*register[2]==register[5]:
			register[0]=register[0]+register[4];
			register[2]=register[2]+1;			
		elif modulo>0:
			register[2]=register[2]+modulo;
		else:
			register[2]=register[2]+1;
		register[1]=0;
	else:
		register=process(register,instructions[ip]);
		ip=register[ip_bind]+1

		if ip<len(instructions):
			register[ip_bind]=ip;
		else:
			running=False;
			print("Process halted after",t,"iterations. Value in register 0 is",register[0]);
			#print(register)
	t+=1;
	if t%1000000==0:
		print("Register after",t/1000000,"million iterations:",register)
