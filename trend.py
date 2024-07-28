from pytrends.request import TrendReq
import pandas as pd

#generating google trends list
def loadingTrends() -> list:
    pytrends = TrendReq(hl="ko-KR", tz=540)
    data = pytrends.trending_searches(pn="south_korea")
    keywordList = [data[0].loc[i] for i in range(15)]

    return keywordList