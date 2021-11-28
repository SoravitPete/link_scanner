from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
import urllib
from typing import List
import urllib.error, urllib.request
import sys


def get_links(url):
    """Find all links on page at the given url.

    Returns:
        a list of all unique hyperlinks on the page,
        without page fragments or query parameters.
    """
    llist = []
    browser.get(url)
    all_link = browser.find_elements_by_tag_name("a")
    for link in all_link:
        url = link.get_attribute('href')
        if url:
            if '#' in url:
                llist.append(url.split('#')[0])
            elif '?' in url:
                llist.append(url.split('?')[0])
            else:
                llist.append(url)
    return llist


def is_valid_url(url: str) -> bool:
    """Check if the url is valid and reachable.

    Returns:
        True if the URL is OK, False otherwise.
    """
    try:
        urllib.request.urlopen(url)
        return True
    except urllib.error.HTTPError:
        return False


def invalid_urls(urllist: List[str]) -> List[str]:
    """Validate the urls in urllist and return a new list containing
    the invalid or unreachable urls.
    """
    inavlid_urls_list = []
    for url in urllist:
        if not is_valid_url(url):
            inavlid_urls_list.append(url)
    return inavlid_urls_list


if __name__ == "__main__":
    browser: WebDriver = webdriver.Chrome(r'C:\Users\hanat\PycharmProjects\pythonProject\link_scanner\chromedriver.exe')
    url = sys.argv[1]
    link_list = get_links(url)
    bad_link = invalid_urls(link_list)
    print('All of good links')
    for each_url in link_list:
        print(each_url)
    print('All of bad links')
    for each_url in bad_link:
        print(each_url)
    browser.quit()
