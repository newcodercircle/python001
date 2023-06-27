from requests_html import AsyncHTMLSession

async def main(page_num):
  session = AsyncHTMLSession()
  page_url = "https://wallhaven.cc/random?seed={seed}&page={page_num}"
  url = page_url.format(seed="123456", page_num=page_num)
  resp = await cls.session.get(url, timeout=10, verify=False)
  hrefs = resp.html.xpath('//div[@id="thumbs"]//a[@class="preview" and @href]')
  for a in hrefs:
    a = a.attrs["href"]
    detail_resp = await session.get(a)
    wallpaper = resp.html.xpath('//img[@id="wallpaper" and @src]')
        if not wallpaper:
            continue
        wallpaper = wallpaper[0].attrs["src"]
    print(wallpaper)
    
if __name__ == "__main__":
    import asyncio

    asyncio.get_event_loop().run_until_complete(main())
  
