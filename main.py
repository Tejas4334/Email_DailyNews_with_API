import smtplib,ssl,os
import requests
from pyexpat.errors import messages

# getting URL for API 
topic = "tesla"
url = f"https://newsapi.org/v2/everything?q={topic}&"\
      "from=2025-05-23&"\
      "sortBy=publishedAt&apiKey=9c62d6ae47f44d84865fa6a47524463d&"\
      "language=en"

# Make a Request
Api = requests.get(url)

# get the data in dict format
content = Api.json()

content_text = f"""Subject: News_Test4


"""

for article in content['articles'][:20]:
    if article["title"] is not None or article["description"] is not None:
        content_text = content_text \
                       + article['title'] +": \n\t" \
                       + article['description'] \
                       +'\n' +article["url"]+ 2*"\n"
    
# print(content_text)
#=======================Mail====================

host = "smtp.gmail.com"
port = 465

username = "tejasdevelopments@gmail.com"
password = os.getenv("Password")

receiver = username

context = ssl.create_default_context()

content_text = content_text.encode("utf-8")
message = content_text

with smtplib.SMTP_SSL(host,port,context=context) as server:
    server.login(username,password)
    server.sendmail(username,receiver,message)