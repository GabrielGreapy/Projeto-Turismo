from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.route("*/**.{png.jpg.jpeg}", lambda route: route.abort())
    page.goto("https://www.google.com/search?client=opera-gx&q=playwright+test&sourceid=opera&ie=UTF-8&oe=UTF-8")
    print(page.title())
    browser.close()