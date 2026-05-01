import os
from datetime import datetime

def take_screenshot(driver, name="screenshot"):
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    url = driver.current_url.replace("https://","").replace("/","_")
    file_name = f"screenshots/{name}_{url}_{timestamp}.png"

    driver.save_screenshot(file_name)

    
    

   

    