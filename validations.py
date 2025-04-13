import re
from datetime import datetime

def is_valid_phone(phone: str)->str | ValueError:
    pattern = r"^\d+$"
    if re.match(pattern, phone):
        return True
    else: 
        raise ValueError("The phone is not valid")
        
def is_valid_name(name: str)-> bool|ValueError:
    if len(name) > 2:
            return True
    else:
        raise ValueError("The name must be more than 2 letters.")
    
    
       
def is_valid_date_format(date:str):
    
    pattern = r"\d{2}\.\d{2}\.\d{4}"  
    if not re.fullmatch(pattern, date):
         raise ValueError("Invalid date format. Use DD.MM.YYYY")
       
    try:
        day, month, year = date.split('.')
        return datetime(int(year), int(month), int(day))
            
    except ValueError:
        raise ValueError("Invalid date. Please write the corect date")
