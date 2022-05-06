import requests
from bs4 import BeautifulSoup

STACK_URL="https://stackoverflow.com/jobs/companies?q=python"


def getpages():
    readUrl = requests.get(STACK_URL)
    soup = BeautifulSoup(readUrl.text, "html.parser")
    pagination = soup.find("div",{"class": "s-pagination"}).find_all("a")

    pages = []
    for page in pagination[:-1]:
        pages.append(int(page.find("span").get_text()))
    
    last_page = pages[-1]
    return last_page

def get_job(item):
    company = item.find("h2").get_text().strip("\n")

    return {
        "Company": company
    }



def get_stack_page(last_page):

    jobs = []
    for page in range(last_page):
        print(f"Scrapping page : {page}")
        readUrl = requests.get(f"{STACK_URL}&={page + 1}")
        soup = BeautifulSoup(readUrl.text, "html.parser")
        company_list = soup.find("div", {"class": "company-list"}).find_all("div", {"class": "-company"})
        
        for result in company_list:
           job = get_job(result)
           jobs.append(job)

    return jobs
