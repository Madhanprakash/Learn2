from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.cricbuzz.com/")
    page.screenshot(path="screenshot6.png")
    browser.close()