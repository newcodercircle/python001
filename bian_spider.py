from requests_html import HTMLSession
from pathlib import Path


def run(url):
    resp = session.get(url)
    resp.encoding = "gbk"  # 指定页面对应编码
    detail_elements = resp.html.xpath('//*[@class="list"]//a[@href and @title]')
    detail_urls = list(map(lambda x: x.absolute_links.pop(), detail_elements))
    print(detail_urls)
    for detail_url in detail_urls:
        detail_resp = session.get(detail_url)
        pic_element = detail_resp.html.xpath('//div[@class="pic"]//img[@src and @alt and @title]')[0]
        pic_url = pic_element.attrs["src"]
        pic_title = pic_element.attrs["title"]
        print("下载", pic_title)
        s = HTMLSession()
        c = s.get(pic_url)
        Path(__file__).absolute().parent.joinpath(pic_title.replace(" ", "") + ".jpg").write_bytes(
            s.get(pic_url).content)
    next_page_element = resp.html.xpath('//*[@id="main"]//a[@href and @class="prev"]')
    if next_page_element:
        next_page_url = next_page_element[-1].absolute_links.pop()
        print("下一页", next_page_url)
        run(next_page_url)


if __name__ == '__main__':
    session = HTMLSession()
    headers = {
        "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        "Cookie": "__yjs_duid=1_b497766f9f42be0a65a58dea63b7b03e1675436689118; trenvecookieclassrecord=%2C7%2C; trenvecookieinforecord=%2C7-29874%2C7-29560%2C7-29870%2C7-29910%2C7-3718%2C; yjs_js_security_passport=c17723f660a3c7ccf4972f07314461c599102820_1675729327_js",
        "Host": "www.netbian.com",
        "Referer": "http://www.netbian.com/meinv/index_2.htm",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    }
    session.headers.update(headers)
    first_page = "http://www.netbian.com/meinv/index_2.htm"
    run(first_page)
