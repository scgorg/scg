from datetime import date

import requests

THIS_YEAR = date.today().year
FACEBOOK_SHARE_LINK = "https://www.facebook.com/sharer.php"
HASHTAG = f" #PyConTW{THIS_YEAR}"
ACCEPTED = f"was accepted for PyCon Taiwan {THIS_YEAR}."

TWITTER_SHARE_LINK = "https://twitter.com/intent/tweet"


def get_facebook_sharelink(link) -> str:
    url = FACEBOOK_SHARE_LINK
    params = {'u': link,
              'hashtag': HASHTAG,
              }

    # prepare_url 可以預先準備好 url 及參數
    final_url = requests.Request('GET', url, params=params).prepare().url
    return final_url


def get_twiter_sharelink(title, link) -> str:
    url = TWITTER_SHARE_LINK
    params = {'text': title + ACCEPTED + link + HASHTAG}

    # prepare_url 可以預先準備好 url 及參數
    final_url = requests.Request('GET', url, params=params).prepare().url
    return final_url


if __name__ == '__main__':
    # Usage
    print(get_facebook_sharelink('https://tw.pycon.org/2023/en-us'))
    print(get_twiter_sharelink(title="My submission '使用 airflow 測試爬蟲'",
                               link='https://tw.pycon.org/2023/en-us'))
