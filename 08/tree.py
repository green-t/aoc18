with open('input.txt') as input_file:
	for line in input_file: mainlist=list(map(int, line.split()));
	
def get_meta(liste):
	summe=0;
	childs=liste[0];
	metaentries=liste[1];

	if childs==0:
		for x in range(metaentries):
			summe+=liste[2+x];
		laenge=2+metaentries;
		i=1;		
		return [summe, laenge, summe, i];		
	if childs>0:
		laenge, summe, value, i=0,0,0,0;
		childvalues=[];
		for x in range(childs):
			erg=get_meta(liste[2+laenge:]);
			summe+=erg[0];
			laenge+=erg[1];
			childvalues.append(erg[2]);
			i+=erg[3];
		for x in range(metaentries):
			metadata=liste[2+laenge+x];
			summe+=metadata;
			if metadata<=childs:
				value+=childvalues[metadata-1];
		laenge=2+laenge+metaentries;
		return [summe, laenge, value, i+1];

erg=get_meta(mainlist);
print(erg[1], "elements checked.",erg[3],"nodes found.\nSum of all metadata is:", erg[0],"\nValue of the root node is:", erg[2]);