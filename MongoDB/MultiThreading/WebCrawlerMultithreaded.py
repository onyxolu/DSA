from concurrent.futures import ThreadPoolExecutor
from threading import Lock
import collections
from typing import List

# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
# class HtmlParser(object):
#     def getUrls(self, url):
#         """
#         :type url: str
#         :rtype List[str]
#         """

# Clarify: does getUrls return cross-hostname links too? expected latency/scale?
# I/O bound problem → multithreading helps, CPU-bound work wouldn't benefit (GIL)
#
# Key insight: separate slow I/O (getUrls) from fast shared-state access (queue, visited)
# Only the shared-state section needs a lock — never lock around network calls
#
# Volunteer before being asked:
#   - Unbounded threads risky → ThreadPoolExecutor caps concurrency (default 10, configurable)
#   - Race condition risk → visited set + queue accessed by multiple threads → needs Lock
#   - Real world: this is a simplified single-machine version of "Design a Distributed Web Crawler"
#     (Bloom filter for dedup, Kafka for URL frontier, per-domain rate limiting, robots.txt)

class Solution:
    def __init__(self):
        self.lock = Lock()
        self.queue = collections.deque()
        self.visited = set()

    def extractHostName(self, url: str) -> str:
        return url.split('/')[2]                          # full hostname, no slicing needed

    def downloadUrl(self, curr_url: str) -> None:
        next_urls = self.htmlParser.getUrls(curr_url)     # slow network call — OUTSIDE lock
                                                            # safe: doesn't touch shared state

        with self.lock:                                    # shared state — must be exclusive
            for url in next_urls:
                if url not in self.visited and self.extractHostName(url) == self.curr_hostname:
                    self.queue.append(url)
                    self.visited.add(url)

    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        self.htmlParser = htmlParser
        self.curr_hostname = self.extractHostName(startUrl)
        self.visited = {startUrl}
        self.queue.append(startUrl)

        with ThreadPoolExecutor(max_workers=10) as executor:   # bounded pool, tunable
            while self.queue:
                futures = []
                while self.queue:
                    futures.append(executor.submit(self.downloadUrl, self.queue.pop()))

                for future in futures:
                    future.result()                       # wait for this round before checking again

        return list(self.visited)

# Edge cases:
#   startUrl has no outgoing links → returns [startUrl]
#   all links same hostname → all get crawled
#   circular links (A→B→A) → visited set prevents infinite loop

# Complexity:
#   time → O(U / min(threads, U)) roughly, bounded by slowest round, U = total unique URLs
#   space → O(U) for visited set and queue

# Follow-ups:
#   Why 10 workers? → tunable; too few wastes concurrency, too many risks overwhelming target server
#   Why pop() not popleft()? → DFS vs BFS order, doesn't matter since output order is unspecified
#   What if getUrls() hangs forever? → add a timeout per future.result()
#   System design version → distributed crawler: Bloom filter dedup, Kafka URL frontier,
#                            per-domain rate limiting, robots.txt compliance, MongoDB for storage