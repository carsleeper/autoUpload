from trend import loadingTrends
from gpt import writingArticles
from auto import upload
import schedule
import time
import random

#refreshing HotKeywordList
def refreshingKeywordList():
    global keywordList
    keywordList = loadingTrends()

def main(i):
    #uploading tistory articles
    x = upload(writingArticles(keywordList[i]))
    if x == 0:
        print(0)
    while x == 1:
        x = upload(writingArticles(keywordList[i]))
        print(1)

if __name__ == '__main__':
    #scheduling refreshingKeywordList function
    schedule.every().day.at("06:00").do(refreshingKeywordList)

    #scheduling auto-upload
    for _ in range(15):
        schedule.every().day.at(f"{(_+7):0>2}:{(random.randint(0,30)):0>2}").do(main,i=_)

    #running schedule handler
    refreshingKeywordList()
    
    while True:
        schedule.run_pending()
        time.sleep(1)
    



