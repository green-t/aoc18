list_of_boxes=[];
abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
twotimers,threetimers=0,0;

with open('input.txt') as input_file:
	for line in input_file:		
		list_of_boxes.append(list(line));


for box1 in list_of_boxes:
	
	#Part1
	counter=0;
	two,three=False,False;

	for letter in abc[:]:			
		counter=0;
		for char in box1[:]:
			if letter==char:
				counter+=1;
		if counter==2:				
			two=True;
		if counter==3:				
			three=True;				

	if three==True:
		threetimers+=1;
	if two==True:
		twotimers+=1;


	#Part2
	for box2 in list_of_boxes[list_of_boxes.index(box1):]:
		if box1 != box2:
			counter=0;
			matched_chars="";
			for char_idx in range(26):				
				if box1[char_idx]==box2[char_idx]:
					counter+=1;
					matched_chars=matched_chars+box1[char_idx];
				if counter==25:
					matched_line1=list_of_boxes.index(box1);
					matched_line2=list_of_boxes.index(box2);
					matched_chars_for_print=matched_chars;


print("\nPart1:")
print("Zeilen mit zwei übereinstimmenden Zeichen:",twotimers);
print("Zeilen mit drei übereinstimmenden Zeichen:",threetimers);
print("Checksumme:", twotimers*threetimers);
print("\nPart2:");
print("Zwei Zeilen gefunden, die bis auf ein Zeichen identisch sind:", matched_line1, "und", matched_line2, "\nÜbereinstimmende Zeichen:", matched_chars_for_print,"\n");
