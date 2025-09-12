import os
import time
from tqdm import tqdm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pykrx import stock

fail = 0
start = 0
end = 0

# 코스피200 구성종목의 종목코드 리스트 가져옴
tickers = list(map(str, list(pd.read_csv("KOSPI200comp.csv", dtype=str)["종목코드"])))

# krx에서 KOSPI200에 속한 종목의 1년치 일별 종가 데이터 크롤링
for ticker in tqdm(tickers) :
    try :
        df = stock.get_market_ohlcv("20220101", "20230226", ticker)["종가"].reset_index(drop=True).dropna()

        # 종목별로 60영업일(대략 3개월)씩 나누고, 그래프로 만들어 저장
        savedir = "C:/Users/USER/Desktop/DMPredict/charts"
        for i in range(len(df) // 20) :
            start = i + i * 20
            end = start + 60
            df1 = df[start:end]

            filename = ("%s%d.png" %(ticker, i))
            filepath = os.path.join(savedir, filename)

            plt.figure(figsize=(10, 5))
            plt.gca().axes.xaxis.set_visible(False)
            plt.gca().axes.yaxis.set_visible(False)
            plt.plot(df1.index, df1)
            plt.savefig(filepath)
            plt.close()

        # 서버 차단 방지용 딜레이
        time.sleep(0.5)
    except :
        fail += 1
        print(f"Failed to get data for {ticker}. fail ratio: {fail}/{len(tickers)}")
