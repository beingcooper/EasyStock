from bs4 import BeautifulSoup
import urllib2
import time
import msg    #Importing from msg.py

page=urllib2.urlopen("http://bnb.ieeedtu.com/getallnews.php")
# Replace the ablove link with the page you want to get updates from

soup=BeautifulSoup(page)
first=second=0

'''
The program keeps a count of the news item that are posted on the game page.
The same process is repeated after a fixed interval of time, the second count is
then compare with the first count. If not equal, a mobile SMS is sent with the
latest news update as text.
'''

'''
In most cases each news alert will be added as a new list element.
You can check this on the souce code of the page.
The same pattern was followed by our example website (bnb.ieeedtu.com).
Therefore, our code intends to count the list ('li') elements.
'''

for item in soup.ul.find_all('li'):
    first=first+1

while first > 0:        # Infinite loop
    page=urllib2.urlopen("http://bnb.ieeedtu.com/getallnews.php")
    soup=BeautifulSoup(page)

    # print(soup.ul.li.get_text()+"   ") For testing purpose
    # print(first)                       For testing purpose
    
    

    for item in soup.ul.find_all('li'):
        second=second+1;

    # print(second)                      For testing purpose
     
    if second != first :
        text=soup.ul.li.get_text() #Generting the latest news to be send as text
        msg.send_sms(text)   # Calling send_sms function from "msg.py"
        first=second
        # print("Message send\n"); For testing purpose
 

    second=0
    # print("Checking Again.....\n") For testing purpose
    time.sleep(50) # Wait for 50 seconds. Change to desired value.
   



