import feedparser
import csv

def fetch_rss_titles(url):
    # 解析 RSS 資料
    feed = feedparser.parse(url)

    # 檢查是否解析成功
    if not feed or feed.bozo:
        print("解析失敗，請確保提供的網址是有效的 RSS Feed。")
        return []

    # 提取所有標題
    titles = [entry.title for entry in feed.entries]

    return titles

def save_to_csv(titles, filename):
    with open(filename, mode='w', newline='', encoding='utf-8-sig') as file:  # 使用 utf-8-sig 編碼
        writer = csv.writer(file)
        writer.writerow(['Title'])
        for title in titles:
            writer.writerow([title])

if __name__ == "__main__":
    # 要爬取的 RSS 網址
    rss_url = "https://news.ltn.com.tw/rss/sports.xml"
    # 獲取所有標題
    titles = fetch_rss_titles(rss_url)

    # 將標題儲存到 CSV 檔案中
    save_to_csv(titles, '0227.csv')

    print("標題已成功儲存到 rss_titles.csv 檔案中。")

