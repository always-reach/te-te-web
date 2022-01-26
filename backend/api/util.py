def format_twitter_response(tweet_response: dict) -> dict:
    twitter_dict = tweet_response.copy()
    tweet_include_data: list = twitter_dict["includes"]["media"]
    for tweet in twitter_dict["data"]:
        if "attachments" in tweet:
            media = []
            for media_key in tweet["attachments"]["media_keys"]:
                include_media = tweet_include_data.pop(0)
                if media_key == include_media["media_key"] and include_media["type"] == "photo":
                    media.append(include_media["url"])
            tweet["media"] = media
    del twitter_dict["includes"]
    return twitter_dict
