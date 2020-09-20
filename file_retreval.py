import random
import json

with open('movie_details.txt','r') as filehandle:
    l = json.load(filehandle)


sample_list = random.sample(l,2)
print(sample_list[0]['title'],sample_list[1]['title'])
