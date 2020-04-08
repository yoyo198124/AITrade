import asyncio 
from pyppeteer import launch
async def main():
    #无头模式
    browser = await launch(headless=True,args=['--no-sandbox'])
    page = await browser.newPage()
    await page.goto('https://www.baidu.com')
    await page.screenshot({'path':'1.png'})
    await browser.close()
asyncio.get_event_loop().run_until_complete(main())
