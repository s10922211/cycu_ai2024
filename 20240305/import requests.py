import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.font_manager as fm

# 抓取網頁內容
url = "https://vipmbr.cpc.com.tw/mbwebs/ShowHistoryPrice_oil.aspx"
response = requests.get(url)

# 解析網頁內容
soup = BeautifulSoup(response.text, 'html.parser')

# 找到所有的 table 標籤
tables = soup.find_all('table')

# 將 HTML 表格轉換為 DataFrame
df1 = pd.read_html(str(tables[0]))[0]
df2 = pd.read_html(str(tables[1]))[0]

print(df1)
print(df2)

#將Dataframe 輸出到 CSV
df2.to_csv(r'C:\Users\Ethan\Desktop\cycu_ai2024\20240305\oil.csv', index=False, encoding='utf-8-sig')


# df2 只保留前兩個欄位的資料
df2 = df2.iloc[:, :5]

# 去除第二欄值是NaN的資料
df2 = df2.dropna(subset=[df2.columns[1]])

# 把第一欄的資料型態 轉成 datatime
df2[df2.columns[0]] = pd.to_datetime(df2[df2.columns[0]])
print(df2)

# 使用 matplotlib 繪製折線圖，x 軸為日期，y 軸為油價
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
font = fm.FontProperties(fname='msyh.ttf')
plt.plot(df2[df2.columns[0]], df2[df2.columns[1]], label='92無鉛汽油')
plt.plot(df2[df2.columns[0]], df2[df2.columns[2]], label='95無鉛汽油')
plt.plot(df2[df2.columns[0]], df2[df2.columns[3]], label='98無鉛汽油')
plt.plot(df2[df2.columns[0]], df2[df2.columns[4]], label='超級柴油', linestyle='solid')
plt.legend(loc='upper right')
plt.xlabel('日期')
plt.ylabel('油價')
plt.title('油價變化趨勢')
plt.show()
# 顯示圖片
