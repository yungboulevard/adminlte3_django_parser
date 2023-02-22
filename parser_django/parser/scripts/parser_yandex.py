from snscrape.modules.telegram import TelegramChannelScraper, TelegramPost
from ..models import News


def run():
    scraper = TelegramChannelScraper('market_marketplace')

    result = []
    tag = []
    time = []
    links = []
    text_content = []


    for i, item in enumerate(scraper.get_items()):

        scr = TelegramPost(url=item.url, date=item.date, outlinks=item.outlinks,
                           content=item.content)
        tag.append('yandex')
        time.append(scr.date)
        links.append(scr.outlinks)
        text_content.append(scr.content)

        if i == 9:
            break

    for i in range(len(tag)):
        news = News.objects.create(tag=tag[i], time=time[i], links=links[i], text_content=text_content[i])
