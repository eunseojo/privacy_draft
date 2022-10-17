

with open('data.tsv','r',encoding='utf-8') as f:
	actors=[]
	directors=[]

	for row in f.readlines():
		if 'actor' in row:
			name=row.split('	')[1]
			if name not in directors:
				actors.append(name)
		elif 'director' in row:
			name=row.split('	')[1]
			directors.append(name)



actors = [actors[i:i+1048576] for i in range(0, len(actors), 1048576)]
directors = [directors[i:i+1048576] for i in range(0, len(directors), 1048576)]

for index,actor_list in enumerate(actors):
	with open('actors'+str(index)+'.csv','w+',encoding='utf-8') as f:
		f.write('\n'.join(actor_list))

for index,director_list in enumerate(directors):
	with open('directors'+str(index)+'.csv','w+',encoding='utf-8') as f:
		f.write('\n'.join(director_list))