from collections import deque;

nrOfPlayers=int(input("Number of players? "));
lastMarble=int(input("How many marbles? "));

running=True;
marbleNr=1;
board=[0];
curPlayer=1
scores=[0 for x in range(nrOfPlayers)];
pos=1;
boardSize=1;

circle=deque([0]);

while running:
	print("Turn",marbleNr,"of",lastMarble);
	if marbleNr%23!=0:
		#pos=pos+2;
		#while pos>boardSize:
		#	pos=pos-boardSize;
		#board.insert(pos,marbleNr);
		#boardSize+=1;
		circle.rotate(-1);
		circle.append(marbleNr);
	else:		
		#pos=pos-7;
		circle.rotate(7);
		#while pos<0:
		#	pos=boardSize+pos;
		scores[curPlayer-1]+=marbleNr+circle.pop();
		#del board[pos];
		#boardSize-=1;
		circle.rotate(-1);

	if marbleNr==lastMarble:
		running=False;
	marbleNr+=1;

	if curPlayer==nrOfPlayers:
		curPlayer=1;
	else:
		curPlayer+=1;

highscore=0;
curPlayer=1;
for score in scores:
	if score>highscore:
		highscore=score;
		winner=curPlayer;
	curPlayer+=1;

print("Winner: Player",winner,"with a score of",highscore);


# With list: 439 - 713070 = 33965633 - 1:00
# With deque: 439 - 713070 = 33965633 - 0:03