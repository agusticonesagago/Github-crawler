import json

from helpers.scraper import get_github_data

"""
NAME
    GitHub crawling

DESCRIPTION
    Crawler that obtains data from git research, such as search urls. Also in case of having repositories, 
    the languages used and their authors.
    
INPUT
    The input data is the list of keywords, proxies and search type you want to search

OUTPUT
    The output data is the list of urls extracted and also extra information, such as the authors of the repository 
    and the languages used.
"""

if __name__ == "__main__":
    input_data = json.loads(open("files/input_data").read())

    print(get_github_data(input_data))
