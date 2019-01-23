import string;

with open('input.txt') as input_file:
	for line in input_file: polymer=str(line);

match=[];
running=True;

for letter in string.ascii_lowercase: match.append(letter+letter.upper());
for letter in string.ascii_uppercase: match.append(letter+letter.lower());

while running:
	length=len(polymer);
	for pair in match: polymer=polymer.replace(pair,"");
	if len(polymer)==length: running=False;

print("Part1\nLength of the polymer:",length);

shortest=length;

for letter in string.ascii_lowercase:
	testpolymer=polymer.replace(letter,"").replace(letter.upper(),"");
	running=True;
	while running:
		length=len(testpolymer);
		for pair in match: testpolymer=testpolymer.replace(pair,"");
		if len(testpolymer)==length: running=False;

	if length < shortest:
		shortest=length;
		bestletter=letter;

print("\nPart2\nBest result: removing letter",bestletter,"brings the polymer down to a length of",shortest);