import feedparser
import logging
from datetime import datetime

class PodcastCrawler:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        
    def fetch_podcasts(self, rss_urls):
        podcasts = []
        for url in rss_urls:
            try:
                feed = feedparser.parse(url)
                for entry in feed.entries:
                    podcast_data = {
                        'title': entry.title,
                        'description': entry.description if hasattr(entry, 'description') else '',
                        'published': entry.published if hasattr(entry, 'published') else '',
                        'link': entry.link if hasattr(entry, 'link') else '',
                        'source_url': url,
                        'crawled_at': datetime.now().isoformat()
                    }
                    podcasts.append(podcast_data)
                self.logger.info(f"Successfully fetched {len(feed.entries)} entries from {url}")
            except Exception as e:
                self.logger.error(f"Error fetching from {url}: {str(e)}")
        return podcasts 