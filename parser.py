from bs4 import BeautifulSoup
import requests


def parse_cmd(name):
    '''

    если пользователь вводит несколько слов, то слова соединяются через "_"
    а после добавляются в ссылку к запросу

    '''

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

        '''
        
        если у запроса будет несколько значений в википедии, то пользователю выдаст несколько тем, в которых
        присутствует запрос
        
        '''

        if 'означать:' in info.split():
            next = [i.text for i in soup.select('span[class=mw-headline]')][:3]
            for i in next:
                info += '\n' + i

        final_msg = f'''
         
            {info}\n\n{url}
            
                    '''
        return final_msg

    else:
        return 'проблемы подключением к сайту'
