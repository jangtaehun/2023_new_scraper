from playwright.sync_api import sync_playwright

p = sync_playwright().start()

browser = p.chromium.launch(headless=False) #기본값 True

page = browser.new_page()

page.goto('http://google.com')

page.screenshot(path='screenshot.png')
#우리가 브라우저를 볼 수 없다 -> headless mode