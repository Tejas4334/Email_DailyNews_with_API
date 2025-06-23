import smtplib,ssl,os
import requests
from pyexpat.errors import messages

# getting URL for API

url = "https://newsapi.org/v2/"\
      "everything?q=tesla&from=2025-05-23"\
      "&sortBy=publishedAt&apiKey=9c62d6ae47f44d84865fa6a47524463d"

# Make a Request
Api = requests.get(url)

# get the data in dict format
content = Api.json()

content_text = ""

for article in content['articles']:
    content_text += f"\n{article['title']}: \n\t{article['description']}"
    
# # print(content_text)
# #=======================Mail====================
#
# host = "smtp.gmail.com"
# port = 465
#
# username = "tejasdevelopments@gmail.com"
# password = os.getenv("Password")
#
# receiver = username
#
# context = ssl.create_default_context()
#
# message = f"""\
# Subject: Test1
#
# {content_text}
#
# """
# with smtplib.SMTP_SSL(host,port,context=context) as server:
#     server.login(username,password)
#     server.sendmail(username,receiver,message)