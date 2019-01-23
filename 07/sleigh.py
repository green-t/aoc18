import string;

nr_of_workers=int(input("Wieviele Arbeiter? "));

# Input in Array übertragen
steps, allreqs, allsteps=[],[],[];
with open('input.txt') as input_file:
	for line in input_file: 
		strin=line.split();
		letter=strin[7];
		req=strin[1];

		steps.append([letter, req]);

		if req not in allreqs: allreqs.append(req);
		if letter not in allsteps: allsteps.append(letter);
		
# Requirements Register erstellen
requirements=[];
for letter in string.ascii_uppercase: 
	requirements.append([letter, False, False]);

# Arbeiter anlegen
workers=[]
for x in range(nr_of_workers):
	workers.append([0,0])

# Bau-Schleife
working=True;
time=0;
result="";
while working:
	working=False;
	# Alle Buchstaben durchgehen
	for letter in string.ascii_uppercase:
		fulfilled=True;
		# Arbeitschritte auf Machbarkeit prüfen
		for step in steps:
			if step[0]==letter:
				if [step[1], False, False] in requirements or [step[1], False, True] in requirements:
					fulfilled=False;
		# Wenn machbar und noch nicht in Arbeit dann weiter
		if fulfilled==True and [letter, False, False] in requirements:
			idx=requirements.index([letter, False, False]);
			#Freien Arbeiter suchen
			for worker in workers:
				if worker[0]==0 and [letter, False, False] in requirements:
					# Übergabe an Arbeiter
					worker[0]=61+idx
					worker[1]=letter;					
					requirements[idx][2]=True;
	# Arbeit verrichten und falls fertig entsprechend markieren 
	for worker in workers:
		if worker[0]>0:
			worker[0]-=1;
			working=True;
		if worker[0]==0 and worker[1]!=0:
			idx=requirements.index([worker[1], False, True]);
			requirements[idx][1]=True;
			result+=worker[1];
			worker[1]=0;
	time+=1;

print("The right order is:", result);
print("Time needed:",time-1,"seconds");
