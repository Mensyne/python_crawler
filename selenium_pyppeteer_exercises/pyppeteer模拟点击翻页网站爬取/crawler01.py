
from  pyppeteer  import launch
import asyncio
from pyquery import PyQuery

width,height  = 1366,768

async def main():
    browser = await launch(
        headless=False,
        #devtools=True,
        autoClose=False,
        args=['--no-sandbox',
              '--diable-infobars',
                f'--window-size={width},{height}']
    )
    page = await browser.newPage()
    await page.setViewport({'width': width, 'height': height}) 
    await page.goto('https://www.fxstreet.com/news')

    
    ## 滚动到页面底部
    await page.screenshot({path: 'example.png'})
    #await page.evaluate('window.scrollBy(0,window.innerHeight)')  # 滚动到页面底部

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())

    
