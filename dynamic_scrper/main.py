from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup

p = sync_playwright().start()

browser = p.chromium.launch(headless=False) #기본값 True
#우리가 브라우저를 볼 수 없다 -> headless mode

page = browser.new_page()

page.goto('https://www.wanted.co.kr/jobsfeed?utm_source=google&utm_medium=sa&utm_campaign=kr_recruit_web_sa_signup&utm_term=wanted&utm_content=brand_new&gad_source=1&gclid=CjwKCAiAqY6tBhAtEiwAHeRopS3-vUc2AC-SpkXbsoM59_b4EcGlUlwIi0TIYqQ8WBnCgjNEYbBJ0RoCjlsQAvD_BwE')
time.sleep(3)

page.click("button.Aside_searchButton__Xhqq3")
#page.locator("button.Aside_searchButton__Xhqq3").click()
time.sleep(3)

page.get_by_placeholder("검색어를 입력해 주세요.").fill("python")
time.sleep(3)

page.keyboard.down("Enter")
time.sleep(3)

page.click("a#search_tab_position")
time.sleep(3)
for x in range(5):
    time.sleep(3)
    page.keyboard.down("End")

content = page.content()
p.stop()

soup = BeautifulSoup(content, "html.parser")

    # page.keyboard.down("End")
    # time.sleep(3)
    #
    # page.keyboard.down("End")
    # time.sleep(3)
    #
    # page.keyboard.down("End")
    # time.sleep(3)

# page.screenshot(path='screenshot.png')
