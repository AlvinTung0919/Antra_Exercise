speech = "All the world’s a stage, And all the men and women merely players.They have their exits and their entrances; And one man in his time plays many parts,His acts being seven ages. At first the infant,Mewling and puking in the nurse’s arms;And then the whining school-boy, with his satchel And shining morning face, creeping like snail Unwillingly to schoolAnd then the lover, Sighing like furnace, with a woeful ballad Made to his mistress’ eyebrow. Then a soldier,Full of strange oaths, and bearded like the pard, Jealous in honour, sudden and quick in quarrel,Seeking the bubble reputation Even in the cannon’s mouth. And then the justice, In fair round belly with good capon lin’d,With eyes severe and beard of formal cut,Full of wise saws and modern instances;And so he plays his part. The sixth age shifts Into the lean and slipper’d pantaloon, With spectacles on nose and pouch on side;His youthful hose, well sav’d, a world too wide For his shrunk shank; and his big manly voice, Turning again toward childish treble, pipes And whistles in his sound.Last scene of all, That ends this strange eventful history, Is second childishness and mere oblivion; Sans teeth, sans eyes, sans taste, sans everything."

word_speech=speech.split()

print(word_speech)

for i in word_speech:
    if 'x' in i:
        print (i)
        
for j in word_speech:
    if 'j' and 'J' in j:
        print(j)