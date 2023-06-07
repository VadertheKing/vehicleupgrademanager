import asyncio

from playwright.sync_api import async_playwright


async def get_browser():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto("http://www.google.com")
        await asyncio.sleep(10)
        await browser.close()


asyncio.run(get_browser())
