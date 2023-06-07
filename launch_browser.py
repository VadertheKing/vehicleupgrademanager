# Launches a browser asynchronously using Playwrightimport asyncio
from playwright.sync_api import Playwright, sync_playwright


def main() -> None:
    async def run(playwright: Playwright) -> None:
        browser = await playwright.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto('https://www.google.com')
        await browser.close()

    if __name__ == '__main__':
        with sync_playwright() as playwright:
            asyncio.run(run(playwright))


if __name__ == '__main__':
    main()
