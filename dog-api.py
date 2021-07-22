import requests, json, random, time
from PIL import Image


response = requests.get('https://random.dog/woof.json')

dogUrl = response.json()['url']

print(dogUrl)

def showAndSaveDog():
    try:
        response = requests.get('https://random.dog/woof.json')

        dogUrl = response.json()['url']
        im = Image.open(requests.get(dogUrl, stream=True).raw)

        im.show()
        #im.save('images\dog.jpg')
        time.sleep(5)
        im.close()
    except:
        print("An Error Occurred. Retrying...")
        showAndSaveDog()

showAndSaveDog()




