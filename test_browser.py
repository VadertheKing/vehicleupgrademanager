import asyncio

from playwright.async_api import async_playwright


async def test(playwright):
    browser = await playwright.chromium.launch()
    context = await browser.new_context()
    page = await context.new_page()

    await page.goto('https://www.google.com/')

    bing_search = 'bing.com'

    await page.goto('https://www.' + bing_search)

    await page.type('input', 'BMW', delay=100)

    await page.keyboard.press('Enter')

    await page.click('#b_results > li:nth-child(1) > div.b_caption > h2 > a')

    print(await page.title())

    await browser.close()


async def main():
    async with async_playwright() as p:
        await test(p)


if __name__ == '__main__':
    asyncio.run(main())
