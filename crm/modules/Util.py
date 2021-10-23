import uuid
import json
from dotenv import load_dotenv
import os

load_dotenv()

def rand_uuid_str() ->str:
    '''
    Generate uuid in string
    '''
    return str(uuid.uuid4())

def json_to_dict(payload) -> dict:
    '''
    Convert json to dictionary
    '''
    return json.load(payload)

def email_sender(key) -> str:
    '''
    Get email sender for tis email
    '''
    emails =  {
                'support': os.getenv('SUPPORT_EMAIL'),
                'sales': os.getenv('SALES_EMAIL')
              }

    if not key in emails.keys():
        return os.getenv('SUPPORT_EMAIL')

    if emails.get(key) == None:
        raise(Exception("No email has been set in env for email sender"))

    return emails.get(key) 