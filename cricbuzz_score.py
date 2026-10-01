from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.cricbuzz.com/", wait_until="domcontentloaded")

    print("URL:", page.url)
    print("TITLE:", page.title())

    print(page.locator("body").inner_text()[:5000])

    page.screenshot(path="cricbuzz_debug.png", full_page=True)

    input("Press Enter to close...")

    browser.close()
   