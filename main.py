import logging
from src.crawler import PodcastCrawler
from src.analyzer import TextAnalyzer
from src.database import DataStorage
import os

# 配置日誌
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/app.log'),
        logging.StreamHandler()
    ]
)

# RSS源列表
rss_urls = [

# Yahoo Finance的Presents Podcast，提供有關財經和市場動態的討論
'https://rss.art19.com/yahoofinancepresents',

# Simplecast提供的CNBC Podcast，專注於各種財經話題和市場報告
'<https://feeds.simplecast.com/_qvRgwME>',

# NPR的財經Podcast，包含商業、科技、投資等領域的分析
'<https://feeds.npr.org/510289/podcast.xml>',

# 《華爾街日報》的"Minute Briefing"，提供最新的市場、經濟和國際新聞摘要
'<https://video-api.wsj.com/podcast/rss/wsj/minute-briefing>',

# Forbes的"Daily Briefing"，這個Podcast每天更新一次，分析全球經濟與市場動態
'<https://rss.art19.com/forbes-daily-briefing>',

# CNN的"5 Things" Podcast，每日更新重要的國際與美國新聞，提供快速簡潔的報導
'<https://rss.art19.com/5-things>',

# Steve Forbes的"What's Ahead" Podcast，討論未來的經濟趨勢與市場動向
'<https://rss.art19.com/steve-forbes-whats-ahead>',

# 來自Financial Times的全球財經新聞Podcast，提供業內精英的觀點
'<https://feeds.sounder.fm/18447/rss.xml>',

# 《華爾街日報》的"The Journal"，深入報導商業、政治、科技和全球事件
'<https://video-api.wsj.com/podcast/rss/wsj/the-journal>',

# Financial Times的"Behind the Money" Podcast，帶您深入了解商業與投資的運作
'<https://www.ft.com/behind-the-money?format=rss>',

# Financial Times的"Money Clinic with Claer Barrett"，專注於個人理財和投資
'<https://www.ft.com/money-clinic-with-claer-barrett?format=rss>',

# Marketplace的Podcast，關注全球經濟、財經事件和市場趨勢
'<https://www.marketplace.org/feed/podcast/marketplace>',

# Morgan Stanley的"Thoughts on the Market" Podcast，討論市場走勢和投資建議
'<https://rss.art19.com/thoughts-on-the-market>',

# "The Bid" Podcast，提供全球市場的深度分析和投資策略
'<https://rss.art19.com/the-bid>',

# BiggerPockets的"Money Podcast"，專注於個人理財和投資策略，尤其是房地產
'<https://rss.art19.com/biggerpockets-money-podcast>',

# Schiff的"Radio" Podcast，提供對經濟和市場的政治分析與解讀
'<https://feeds.blubrry.com/feeds/schiffradio.xml>'

# JPMorgan的"Markets & Macro" Podcast，深入探討全球市場走勢及宏觀經濟問題
'http://www.jpmorgan.com/rss/podcasts/markets-macro.xml',

# JPMorgan的"Investment Insights" Podcast，專注於投資策略、資產配置及市場分析
'http://www.jpmorgan.com/rss/podcasts/investment-insights.xml',

]

def main():
    logger = logging.getLogger(__name__)
    logger.info("Starting financial analysis system...")
    
    try:
        # 初始化組件
        crawler = PodcastCrawler()
        analyzer = TextAnalyzer()
        storage = DataStorage()
        
        # 爬取 podcast
        logger.info("Starting podcast crawling...")
        podcasts = crawler.fetch_podcasts(rss_urls)
        
        # 分析文本
        logger.info("Starting text analysis...")
        analyzed_data = []
        for podcast in podcasts:
            analysis_result = analyzer.analyze_text(podcast['description'])
            financial_metrics = analyzer.analyze_financial_metrics(podcast['description'])
            
            analyzed_data.append({
                **podcast,
                'analysis': analysis_result,
                'financial_metrics': financial_metrics
            })
        
        # 儲存結果
        logger.info("Saving results...")
        storage.save_to_json(analyzed_data, 'podcast_analysis')
        storage.save_to_csv(analyzed_data, 'podcast_analysis')
        
        logger.info("Analysis completed successfully!")
        
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    main() 