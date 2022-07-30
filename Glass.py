import time
from plyer import notification


if __name__ == '__main__':

    
    while True:

        
        notification.notify(

            
            title="It's time to drink water, please drink water!",
            message="Water boosts energy and it helps weight loss and digestion. Water hydrates skin.",
            app_icon="Glass-water.ico",
            timeout=5
        )

        
        time.sleep(60*60)