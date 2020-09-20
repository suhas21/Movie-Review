import tmdbsimple as tmdb
import json

tmdb.API_KEY = 'c1bd16583e5f87b398699fddf8a8571f'

search = tmdb.Search()
l = list()

#movies list
movies_list = ['Antman','Black Panther','Avengers: Endgame','Inside Out','A Quiet Place',
'Logan','The Prestige','John Wick','Memento','Ford v Ferrari','The Last Samurai',
'Troy',"Ocean's Twelve",'The Dark Knight','Superman Returns','Isle of Dogs','Tomb Raider'
,'The Chronicles of Narnia: Prince Caspian','Slumdog Millionaire','Inception','Ferdinand'
'La La Land','Searching','Parasite','Knives Out','Roma','Tomorrowland','Frozen',
'Monsters University','The Jungle Book','Zootopia','Finding Dory','Moana','Beauty and the Beast',
'The Incredibles 2','Cars 3','Mulan','Deadpool 2','Iron Man','Iron Man 3','Spider-Man 2','Captain Marvel',
'The Incredible Hulk','Doctor Strange','Thor','Fantastic Four','Avatar','The Martian',
'The Revenant','Ice Age','The Boss Baby','Planet of the Apes','Turbo','Hidden Figures',
'Night at the Museum','Game of Thrones','Joker','Money Heist','The Lion King','Captain Marvel',
'Ant-Man and the Wasp','Guardians of the Galaxy','Guardians','Scoob!','Frozen 2','Toy Story 4',
'The Emoji Movie','Coco','The Grinch','Fight club','Escape Room','The Meg','Interstellar','Rampage'
'The Matrix','Momento','The Prestige','Inception','3 Idiots','Wall-E','Intouchables','Blade Runnder',
'Greyhound','Midway','The Irishman','Gemini Man','Stuber','Dark Phoenix','Ma','Aladdin',
'Shazam','Hotel Mumbai','Alita: Battle Angel','Glass','Bumblebee','The Mule','Aquaman','Green Book'
'First Man','A Star is Born','Venom','Night School','Smallfoot','The Predator','Roma','Christopher Robin']


for i in movies_list:
    response = search.movie(query = i)
    if response['total_results'] > 0:
        k = k + 1
        l.append({'id':response['results'][0]['id']  ,'poster_path': response['results'][0]['poster_path'] ,'title':response['results'][0]['original_title']})



with open('movie_details.txt','w') as filehandle:
    json.dump(l,filehandle)

print('successful')
