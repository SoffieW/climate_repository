
import os
from dotenv import find_dotenv,load_dotenv
from requests import session
import logging

#payload for login to kaggle
payload = { 
    'action': 'login',
    'username': os.environ.get("KAGGLE_USERNAME"),
    'password': os.environ.get("KAGGLE_PASSWORD")

}


def extract_data(url, file_path): #Downloads file from kaggle website
    '''
    method to extract data
    '''
    #setup session
    with session() as c:
        c.post('https://www.kaggle.com/account/login', data =payload)
        with open(file_path, 'wb') as handle:
            response = c.get(url,stream = True)
            for block in response.iter_content(1024):
                handle.write(block)
                
def main(project_dir): #Get logger instance using get logger function
    '''
    main method
    '''
    #get logger
    logger = logging.getLogger(__name__)
    logger.info('getting raw data')
    
    #url
    url = 'https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data/download/GlobalLandTemperaturesByCity.csv'
    
    #file path
    raw_data_path = os.path.join(project_dir,'data','raw')
    data_path = os.path.join(raw_data_path,'GlobalLandTemperaturesByCity.csv')
    #extract data
    extract_data(url,data_path)
    logger.info('downloaded raw data')

if __name__ == '__main__':
    #getting root directory
    project_dir = os.path.join(os.path.dirname(__file__),os.pardir,os.pardir)
    #setup logger
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format = log_fmt)
    
    #find .env automatically by walking up directories until found
    dotenv_path = find_dotenv()
    #load up the entries as environment variables
    load_dotenv(dotenv_path)
    
    #call the main
    main(project_dir)
