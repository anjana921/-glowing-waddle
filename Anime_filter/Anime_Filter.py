# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 22:04:50 2021

@author: gunas
"""

# import asyncio
# from pyppeteer import launch
# import io

# async def main():
#     browser = await launch()
#     page = await browser.newPage()
#     await page.goto('http://www.google.com')
#     await page.screenshot({ 'path': "C:/Users/gunas/OneDrive/Pictures/Screenshots/Screenshot (44).png"})
#     await browser.close()

# asyncio.get_event_loop().run_until_complete(main())

import asyncio
import time
from pyppeteer import launch
from bs4 import BeautifulSoup
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://www.imdb.com/')
    await page.type('#suggestion-search','naruto shippuden')
    await page.keyboard.down('Enter')


    # Fill content into the search field
    content = "naruto shippuden"
    # await page.evaluate(f"""() => {{
    #     document.getElementById('suggestion-search').click();
    #     document.getElementById('suggestion-search').value = 'naruto shippuden';
    # }}""")
    
    # await page.evaluate(f"""() => {{
    #     console.log('hello');
    #     }}""")

    # await page.evaluate(f"""() => {{ 
    #     document.getElementById('suggestion-search').setRangeText("text");
    #     }}""")
    # ele =
    # await page.evaluate(f"""() => {{
    #     ele = document.getElementsByClassName('react-autosuggest__container')
    #     }}""")
    # print (ele)
        
    # Now click the search button  
    #await page.click("button.suggestion-search-button")
    # await page.evaluate(f"""() => {{
    #     document.getElementById('imdbHeader-searchOpen').dispatchEvent(new MouseEvent('click', {{
    #         bubbles: true,
    #         cancelable: true,
    #         view: window
    #     }}));
    # }}""")

    # # Wait until search results page has been loaded
    await page.waitForSelector('.findSectionHeader')
    time.sleep(3)    
    await page.click('[class="primary_photo"]')
    
            
    await page.waitForSelector('.ipc-inline-list__item')
   
    await page.keyboard.down('PageDown')
    await page.waitForSelector('.ipc-title__text')
    time.sleep(3) 
    await page.click('[class="ipc-title__text"]')
    time.sleep(3)
    await page.screenshot({'path': 'C:/Users/gunas/temp/screenshot.png'})
    
    count = 0
    
    while (count == 0):
        
        if (await page.waitForSelector('[id=load_previous_episodes]')):
            count = 0
            print("scrape data")
            await page.waitForSelector('[id=list detail eplist]')
            await page.click('[id=load_previous_episodes]')
            episode_num = soup.select(div.load_previous_episodes)
            print(episode_num.toString)
            time.sleep(3)
            await page.screenshot({'path': 'C:/Users/gunas/temp/screenshot_prev.png'})
            count += 1
            
        else:
            count += 1
            print(count)
    
    
   #__next > main > div > section.ipc-page-background.ipc-page-background--base.TitlePage__StyledPageBackground-wzlr49-0.dDUGgO > section > div:nth-child(4) > section > section > div.TitleBlock__Container-sc-1nlhx7j-0.hglRHk > div.TitleBlock__TitleContainer-sc-1nlhx7j-1.jxsVNt > h1

    #await page.select('#byYear','2009')

    #await page.keyboard.press('Enter')
    
    time.sleep(3)

    # Now take screenshot and exit
    await page.screenshot({'path': 'C:/Users/gunas/temp/screenshot.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())


