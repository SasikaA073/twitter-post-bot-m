# TODO: IMPORT LIBRARIES
from datetime import datetime
from threading import Timer
import time


from python.get_quotes import getMotivationalQuote, updateQuotesLogFile
# from python.photo_edit import 
from python.unsplash import saveAllPhotosIds,getUnsplashPhoto,downloadPhoto

## DIRECTORIES
python_file_path = __file__
python_file_path = python_file_path.split("\\")

main_directory = '\\'.join(python_file_path[:-1]) + '\\'

assets_path = main_directory + "assets\\"
fonts_path = assets_path + "fonts\\"
images_path  = assets_path + "images\\"

log_path = main_directory + "log\\"
program_files_path = main_directory + "python\\"

results_path = main_directory + "results\\"


## Social Media Account Keys
ig_email = ""
ig_password = ""

twitter_email = ""
twitter_password = ""
 
delay = 60*60*6  # 6 hours

# TODO: Post 4 photos per day
while True:
    # TODO: Get a quote
    quote_author = (quote,author) = getMotivationalQuote()
    updateQuotesLogFile(quote_author)

    # TODO: Get a photo
    
    time.sleep(delay)





# TODO: Edit the photo accordingly

# TODO: Upload photo to twitter 

# TODO: Upload photo to instagram


