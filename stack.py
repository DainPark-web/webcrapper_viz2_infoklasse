import requests
from bs4 import BeautifulSoup

STACK_URL = "https://stackoverflow.com/jobs/companies?q=python"

def get_pages():
    read_url = requests.get(STACK_URL)
    soup = BeautifulSoup(read_url.text, "html.parser")
    pagination = soup.find("div", {"class": "s-pagination"}).find_all("a")

    pages = []
    for page in pagination[:-1]:
        pages.append(int(page.find("span").get_text()))

    last_page = pages[-1]
    return last_page


def get_job(item):
    company = item.find("h2").find("a").get_text()
    return {
        "Comapny": company
    }

   

def get_jobs(last_page):
    jobs = []
    for page in range(last_page):
        read_url = requests.get(f"{STACK_URL}&pg={page + 1}")
        soup = BeautifulSoup(read_url.text, "html.parser")
        companylist = soup.find("div", {"class": "company-list"}).find_all("div", {"class": "-company"})
        
        for item in companylist:
            jobs.append(get_job(item))
    print(jobs)
    return jobs
   
