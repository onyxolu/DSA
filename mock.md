# don't visit a link more than once

# limited worker threads to a default: 10

# lock to handle race condition

class Solution:
def **init**(self):
self.lock = Lock()
self.queue = collections.deque()
self.visited = set()

    def extractHostName(self, url):
        return url.split('/')[2]

    def downloadUrls(self, url:str):
        next_urls = self.htmlParser.getUrls(url)

        with self.lock:
            for url in next_urls:
                if url not in self.visited and self.extractHostName(url) == self.cur_hostname:
                    self.queue.append(url)
                    self.visited.add(url)

    def crawlUrls(self, startUrl, htmlParser):
        self.htmlParser = htmlParser
        self.cur_hostname = self.extractHostName(startUrl)
        self.visited = {startUrl}
        self.queue.append(startUrl)

        with ThreadPoolExecutor(max_workers = 10) as executor:
        # ThreadPoolExecutor handles freeing up threads when they are free
            while self.queue: #BFS
                futures = []
                while self.queue:
                    futures.append(executor.submit(self.downloadUrls, self.queue.pop()))

                for future in futures:
                    future.result()

        return list(self.visited)
