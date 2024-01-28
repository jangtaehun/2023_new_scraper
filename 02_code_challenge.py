import requests
from bs4 import BeautifulSoup

# 막힐 때 -> network -> 첫 번째 request -> request header: 브라우저가 서버에 보내는 정보 -> user-agent
# title, company, position, region, url
# print(response.status_code)

all_jobs = []
all_position = []

class Scraper():
    def __init__(self, keyword, url='https://remoteok.com/'):
        self.url = url + f'remote-{keyword}-jobs'
        print(f'scraping {url}...')

    def scraping_jobs(self):
        #개발자 모드 -> Network -> User-Agent
        response = requests.get(self.url, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})
        soup = BeautifulSoup(response.content, 'html.parser')  # content / 넘겨준 데이터가 어떤 종류의 형태이지를 알려줘야 한다.
        jobs = soup.find_all("tr", class_='job')
        for job in jobs:
            title = job.find("h2", itemprop="title")  # get_text() == text
            company = job.find("h3", itemprop="name")
            region = job.find("div", class_='location')

            position = [positions.find('h3').text.strip() for positions in job.find_all('a', class_='action-add-tag')[:3]]
            all_position.append(position)

            urls = f'https://remoteok.com/' + job.find("a", class_='preventLink')['href']
            job_data = {
                'title': title.text.strip(),
                'company': company.text.strip(),
                'position': '/'.join(position),
                'region': region.text.strip(),
                'url': urls
            }
            all_jobs.append(job_data)
        print(all_jobs)

    def waiting(self):
        return f'scraping {self.url}...'


keywords = [
    "flutter",
    "python",
    "golang"
]
scrap = Scraper(keyword = keywords[0])
scrap.scraping_jobs()
