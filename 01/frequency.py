operations=[];
with open('input.txt') as input_file:
		for line in input_file:
			operations.append(int(line));

result=0;
resultList={0}; # als Set
#resultList=[0]; # als Liste

i=0;
running=True;

while running:
	i+=1;
	print('Iteration',i);
		
	for op in operations:
		result = result+op;
		
		if result in resultList:
			print("First double frequency: ", result);
			running=False;
			break;
		
		resultList.add(result); # Set
		#resultList.append(result); # Liste