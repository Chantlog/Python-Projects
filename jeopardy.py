import requests, json, random
from fuzzywuzzy import fuzz

print("\033c")
req = requests.get('http://jservice.io/api/random')

list = json.loads(req.text)

qIndex = random.randrange(0,len(list))

category = list[qIndex]['category']['title']

question = list[qIndex]['question']
answer = list[qIndex]['answer']

print('The Category is %s'%category)
#print(answer)
userAnswer = input('%s\n'%question)



if(fuzz.ratio(userAnswer.lower(),answer.lower()) > 80):
    correct = True
else:
    correct = False

if(correct):
    print('Correct')
else:
    print('Incorrect, the answer was %s' %answer)
    