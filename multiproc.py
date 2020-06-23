import requests
import asyncio
from concurrent.futures import ProcessPoolExecutor as PoolExecutor
from googlesearch import search

NUM_LOOPS = 150
MAX_HITS = 3
payload = {}


def fetch(loop_num):
    
    url = "https://www.google.com"
    
    query = f"{loop_num} new cases"
    
    payload[loop_num] = []
    for i in search(query, tld="com", num=MAX_HITS, stop=MAX_HITS, pause=5):
        payload[loop_num].append(i)    
    
    
    # with session.get(url, params=params) as response:
    #     data = response.text
    #     if response.status_code != 200:
    #         print("FAILURE::{0}".format(url))
    #     print(data)
    #     return data

def main():
    with PoolExecutor(max_workers=2) as executor:
        for _ in executor.map(fetch, range(NUM_LOOPS)):
            pass
    print(payload)
    
main()
