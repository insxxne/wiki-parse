from bs4 import BeautifulSoup
import requests


def parse_cmd(name):
    if len(name.split()) > 1:
        split_words = [i.title() for i in name.split()]
        url = f'https://ru.wikipedia.org/wiki/{"_".join(split_words)}'
    else:
        url = f'https://ru.wikipedia.org/wiki/{name}'

    r = requests.get(url)
    if r.status_code == 200:
        get_html = r.content
        soup = BeautifulSoup(get_html, 'html.parser')

        info = soup.select_one('p').text

        final_msg = f''' {info}\n{url}
        '''
        return final_msg
