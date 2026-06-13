# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

from concurrent.futures import ThreadPoolExecutor
from threading import Lock

class Solution:
    def __init__(self):
        self.lock = Lock()
        self.queue = collections.deque()
        self.visited = set()

    def extractHostName(self, url):
        return '.'.join(url.split('/')[2].split('.')[1:])    

    def downloadUrl(self, curr_url):
        next_urls = self.htmlParser.getUrls(curr_url)
        
        # Use Lock to protect shared states.
        with self.lock:
            for url in next_urls:
                if url not in self.visited and self.curr_hostname == self.extractHostName(url):
                    self.queue.append(url)
                    self.visited.add(url)  

    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        """
        :type startUrl: str
        :type htmlParser: HtmlParser
        :rtype: List[str]
        """
        self.queue.append(startUrl)
        self.curr_hostname = self.extractHostName(startUrl)
        self.visited = {startUrl}
        self.htmlParser = htmlParser
        # Limit to 10 worker threads
        with ThreadPoolExecutor(max_workers = 10) as executor:
            while self.queue:

                executor_list = list()
                # Execute this batch of threads with threadpool
                while self.queue:
                    executor_list.append(executor.submit(self.downloadUrl, self.queue.pop()))

                # Main thread waiting for the above threads to finish
                for future in executor_list:
                    future.result()
        
        return list(self.visited)    
        
        