from playwright.sync_api import sync_playwright


def start_browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        return playwright, browser
