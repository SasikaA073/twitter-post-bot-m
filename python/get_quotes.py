import requests,json

# Get the motivational quotes
def getMotivationalQuote():
    key = "d0f8bc38f4db848680994db93d77e22001f33a66"
    modes = ['random','today','quotes']
    mode = modes[0]
    urlZen = f"https://zenquotes.io/api/{mode}/{key}"

    responseZen = requests.get(urlZen)

    # .content -> in Bytes , u have to decode this
    responseContent  = responseZen.content
    responseText = responseContent.decode('utf-8')

    # .text -> in Str, after decoding
    responseText2 = responseZen.text

    responseJson = json.loads(responseText)
    responseJson = responseJson[0]
    # print((responseText2))
    # pprint.pprint(responseJson)
    # pprint.pprint(responseZen.content)
    # content

    quote = responseJson['q']
    author = responseJson['a']

    return (quote,author)

def updateQuotesLogFile(x:tuple)-> None:
    """ 
    Update the quotes file
    """
    file = open('assets/all_quotes.text','r')
    lines = file.readlines()
    line_no = int(lines[-1].split(":")[0])
    file.close()

    file = open('all_quotes.text','a')
    file.write(f"{line_no + 1} : {x[0]} : {x[1]}\n")
    file.close()
