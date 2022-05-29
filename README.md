# Books-To-Scrape
My approach to books.toscrape.com with Scrapy CrawlSpider and ItemLoaders

#### Requirements
- python3
- pip3
- itemadapter==0.6.0
- itemloaders==1.0.4
- Scrapy==2.6.1

#### Instructions
Clone the repo and install dependencies, dependencies are available at *requirements.txt*
```bash
git clone https://github.com/egarcia2506/books-to-scrape
cd books-to-scrape
pip3 install -r requirements.txt
```

#### To run the Crawler and get the output in a JSON file
```bash
scrapy crawl book -o books.json
```