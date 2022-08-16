import requests

def getstuff(word):
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
    url = url+ word
    try:
        response = requests.get(url).json()[0]
        mean,exmp = None,None
        if 'meanings' in response:
            response = response['meanings'][0]
            if 'definitions' in response:
                response = response['definitions'][0]
                if 'definition' in response:
                    mean = response['definition']
                if 'example' in response:
                    exmp = response['example']  
                return [mean,exmp]
            else:
                return [None,None]
        else:
            return [None,None]
    except Exception as e:
        print(str(e))
        return  [None,None]



if __name__ == "__main__":
    print(getstuff('ObliQue'))