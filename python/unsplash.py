
import requests,os,json,pprint,pickle

unsplash_access_key = "kHdTdIu6jxJxJkxrCGhcAJ-FSVyjNur1A-Jy-duvMp0"
unsplash_secret_key = "y0AzQhHmMcHwDM8qP6ulxFIqQrfyyHC8gGrGPcpTx4Q"

BASE_URL = "https://api.unsplash.com"

order_by = ["oldest","latest","popular"]
results_per_page = 5
# no_pages = 100
n = 0

unsplash_photos_ids_file = f"unsplash_photos_ids{n}.txt"

types = ["raw","full","regular","small","thumb"]

def saveAllPhotosIds(text_file:str,no_pages:int) -> None:
    """
    Input : 
        text_file : save 1000 photos ids at a time
        
    Returns:
        none
        
    """
    with open(text_file,'w',newline="\n") as file:
        for i in range(1,no_pages+1):

            photos_list_url = BASE_URL 
            photos_list_url += f"/photos/?client_id={unsplash_access_key}&"
            photos_list_url += f"page={i}&"
            photos_list_url += f"per_page={results_per_page}&"
            photos_list_url += f"order_by={order_by[2]}"

            r = requests.get(photos_list_url)
            
            if r.status_code == 200:
                rJson = json.loads(r.text)
                # pprint.pprint(rJson)
                for i in range(len(rJson)):
                    photo_id = rJson[i]['id']
                    print(i,photo_id)
                    file.writelines(f"{photo_id}\n")
            else:
                print(r.status_code)
                pass
    return None

def getUnsplashPhoto(id:str,type:str)->str:
    """
    input: 
        id: unsplash photo id
    Process:
        downloads the relevant photo
    Returns: 
        tuple 
            id : as the name of the photo
            url : the url of the photo
    """

    photo_details = BASE_URL 
    photo_details += f"/photos/{id}?client_id={unsplash_access_key}&"

    r = requests.get(photo_details)

    if r.status_code == 200:
        rJson = json.loads(r.text)
        # pprint.pprint(rJson)
        
        return (
            id, #name
            rJson['urls'][type], # photo_url
            rJson['color'], # color
            rJson['alt_description'],
            rJson['location']['country']
            

        )
    else:
        print(r.status_code)
        print("Error when getting the Unsplash photo by id")
        return None
    """
    input: 
        id: unsplash photo id
    Process:
        downloads the relevant photo
    Returns: 
        tuple 
            id : as the name of the photo
            url : the url of the photo
    """

    photo_details = BASE_URL 
    photo_details += f"/photos/{id}?client_id={unsplash_access_key}&"

    r = requests.get(photo_details)

    if r.status_code == 200:
        rJson = json.loads(r.text)
        # pprint.pprint(rJson)
        return (id,rJson['urls'][type])
    else:
        print(r.status_code)
        print("Error when getting the Unsplash photo by id")
        return None
    
# r = getUnsplashPhoto("78A265wPiO4",types[2]) 

def downloadPhoto(input:getUnsplashPhoto)->None:

    """
    Save the image file to the assets folder
    """
    
    name = input[0]
    url = input[1]
    color = input[2]
    description = input[3]
    country = input[4]

    try:
        r = requests.get(url)
        file = open(f"assets/images/image_{name}.jpg","wb")
        file.write(r.content)
        file.close()

        return 200
    except:
        return -1

# downloadPhoto(r)

def loadPhoto(id:str):

