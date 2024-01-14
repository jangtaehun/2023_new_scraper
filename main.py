import requests
from bs4 import BeautifulSoup

# class_ -> python에는 class가 있다.
# find("") -> 맨 앞에 있는 하나만 가져온다.
# _ -> 무시

# url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"

all_jobs = []
def scrape_page(url):
    print(f'scraping {url}...')
    # response.status_code
    # response.content #그 page의 source code를 줘야한다.
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    #첫 번째 매개변수 - content / 두 번째 매개변수 - 넘겨준 데이터가 어떤 종류의 형태이지를 알려줘야 한다.

    jobs = soup.find("section", class_='jobs').find_all("li")[1:-1]

    for job in jobs:
        title = job.find('span', class_='title').text
        company, position, region = job.find_all('span', class_='company')
        url = job.find('div', class_='tooltip').nextSibling['href']
        job_data = {
            'title': title,
            'company': company.text,
            'position': position.text,
            'region': region.text,
            'url': f"https://weworkremotely.com/{url}"
        }
        all_jobs.append(job_data)

def get_pages(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return len(soup.find('div', class_='pagination').find_all('span', class_='page'))

total_pages = get_pages('https://weworkremotely.com/remote-full-time-jobs?page=1')

for x in range(total_pages):
    url = f'https://weworkremotely.com/remote-full-time-jobs?page={x+1}'
    scrape_page(url)

print(all_jobs)