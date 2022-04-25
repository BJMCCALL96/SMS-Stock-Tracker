import requests
from twilio.rest import Client
STOCK_ENDPOINT="https://www.alphavantage.co/query"
NEWS_ENDPOINT="https://newsapi.org/v2/everything"

STOCK_NAME="TSLA"
COMPANY_NAME="Telsa"


STOCK_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
NEWS_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


account_sid = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

stock_param={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":STOCK_API_KEY,

}
stock_res=requests.get(STOCK_ENDPOINT,params=stock_param)
data=(stock_res.json()["Time Series (Daily)"])
data_list= [value for (key,value) in data.items()]
yesterday_data=(data_list[0])
yesterday_close=(data_list[0]["4. close"])
print(yesterday_close)


day_before_yesterday_data=data_list[1]
day_before_yesterday_close=(data_list[1]["4. close"])
print(day_before_yesterday_close)



differnce=(float(yesterday_close)-float(day_before_yesterday_close))
diff_percent=(differnce/float(yesterday_close))*100
print(diff_percent)
up_down=None
if diff_percent > 0:
    up_down= "📈"
else:
    up_down="📉"


if diff_percent >= 3:
    news_param={
        "apiKey":NEWS_API_KEY,
        "qInTitle":COMPANY_NAME,
        "language":"en",
    }
    news_response=requests.get(NEWS_ENDPOINT,params=news_param)
    articles=(news_response.json())["articles"]
    three_articles=articles[:3]
    print(three_articles)
    formatted_articles=[f"{COMPANY_NAME} {up_down} {diff_percent}%\nHeadline: {articles['title']}. \nBrief: {articles['description']}" for articles in three_articles]
    print(formatted_articles)
    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages.create(
            messaging_service_sid='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
            body=article,
            to='XXX-XXX-XXXX',
        )






