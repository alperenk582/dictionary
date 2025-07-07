import requests

class Dictionary():
    def __init__(self):
        self.api_url="https://api.dictionaryapi.dev/api/v2/entries/en/"

    def getApi(self,wrd):
        try:
            response=requests.get(self.api_url+wrd)
            response.raise_for_status()
            return response.json()
        except (requests.RequestException,ValueError):
            return None
    
    def findDefinition(self,data):
        if data:
            print("Defintion: ",data[0]["meanings"][0]["definitions"][0]["definition"])
        else:
            print("No definition found")

    def findType(self,data):
        if data:
            print("Type: ",data[0]["meanings"][0]["partOfSpeech"])
        else:
            print("No type info found")

    def findSentence(self,data):
        if data:
            try:
                print("Example sentences: ",data[0]["meanings"][0]["definitions"][0]["example"])
            except KeyError:
                print("There is no example sentence")
        else:
            print("No sentence found")

dictionary=Dictionary()

while True:
    word=input("word (or q to exit):  ")

    if word.lower()=="q":
        break
    data=dictionary.getApi(word)
    dictionary.findDefinition(data)
    dictionary.findType(data)
    dictionary.findSentence(data)


    
    