# python3
### 安裝 Flask
    python3 pip install flask

### 安裝 Scrapy
    python3 pip install scrapy

### 建立 Scrapy EX
    scrapy startproject crawler_demo

### 建立 Spider EX
    scrapy genspider google google.com.tw


### 注意事項
    atmovies.py 要寫入多少項資料 有兩個檔案 連動 items.py, pipelines.py

    執行寫入檔案 settings.py 註解要打開
    TEM_PIPELINES = {
        'crawler_demo.pipelines.CrawlerDemoPipeline': 300,

    由flask進入會有寫入讀取檔案會有編碼問題 需加 encoding='utf-8

    Spider 與 flask 溝通
    os.chdir 進入該資料夾
    os.system 執行 scrapy crawl xxxxx