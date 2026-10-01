from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://pavosoftwebsite.web.app/portfolio")
    page.screenshot(path="screenshot5.png")
    browser.close()