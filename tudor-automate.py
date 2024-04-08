import requests
import logging

#Setup the loggers
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)
logging.basicConfig(filename='output.log', 
                    level=logging.DEBUG, 
                    format='%(levelname)s | %(asctime)s | %(message)s')

#Make the API call to vote
url = 'https://tools.gardenandgunmag.com/vote.php?env=live&s=192112&id=15&vt=bracket&v1=bracket000&v2=9d59ddca33cfe733dbadee24fdc0b620&cv=y&os=24&r=5&_=1712425379624'
r = requests.get(url)
output = r.json()

#log the records
logger.info(output)