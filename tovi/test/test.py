import json
from ..main import ToVI

with open("config.keys", "r") as keys:
    keys = json.load(keys)

vi = ToVI(
    vi_subscription_key=keys['SUBSCRIPTION_KEY'],
    vi_location="Trial",
    vi_account_id=keys['ACCOUNT_ID']
)

vi.YouTubeToVI(youtube_link = "https://www.youtube.com/watch?v=a8fHgx9mE5U",
                video_name = "lego",
                video_language = "English")


result = vi.get_video_info(vi.video_id)

