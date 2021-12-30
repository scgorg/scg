import urllib.parse


def get_facebook_post(video, talk):
    video_link = urllib.parse.quote(video)

    word = urllib.parse.quote(f"My PyConTW talk '{talk}' is up on YouTube!")
    link = f"https://www.facebook.com/sharer.php?u={video}&hashtag=%23pycontw2021%23&quote={word}"

    # print(link)

    return link


def get_twitter_tweet(video, talk):
    word = urllib.parse.quote(
        f"My @PyConTW talk '{talk}' is up on YouTube! {video} #pycontw2021"
    )

    link = f"https://twitter.com/intent/tweet?text={word}"
    # print(link)
    return link


if __name__ == "__main__":
    # return_url_tw(
    #     "https://www.youtube.com/watch?v=GL-toRY_z88&list=PLqtzN042QpfdYu4HOnqIa1PHIsih3MYmx&index=8&ab_channel=PyConTaiwan",
    #     "網路爬蟲即學即用 - 透過 Python 快速蒐集人力銀行的職缺資訊")
    pass
