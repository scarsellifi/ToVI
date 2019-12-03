# toVi
## Library to upload file to Video Indexer from different sources in automatic way.

Get free account video indexer on [Microsoft Site](https://vi.microsoft.com/it-it/) 
and obtain your 
* ACCOUNT_ID and
![ACCOUNT_ID](https://docs.microsoft.com/it-it/azure/media-services/video-indexer/media/video-indexer-use-apis/account-id.png)
* SUBSCRIPTION_KEY
![SUBSCRIPTION_KEY](https://docs.microsoft.com/it-it/azure/media-services/video-indexer/media/video-indexer-use-apis/video-indexer-api03.png)

#Installation 
```bash
pip3 install tovi 
```

# Use
```python
from tovi import ToVI

CONFIG = {
    'SUBSCRIPTION_KEY': {your subscription key}, 
    'LOCATION':   {your subscription key}, #'trial'
    'ACCOUNT_ID': {your ACCOUNT_ID} # i must hidden in a configuration file 
}

## instantiate the object 
vi = ToVI(
    vi_subscription_key=CONFIG['SUBSCRIPTION_KEY'],
    vi_location=CONFIG['LOCATION'],
    vi_account_id=CONFIG['ACCOUNT_ID']
)
 
## select source (for now you-tube only, the name of the video and the language used)
vi.YouTubeToVI(youtube_link = "https://www.youtube.com/watch?v=a8fHgx9mE5U",
                  video_name = "lego",
                  video_language = "English")
```



## Credits
Thanks to [bklim](https://github.com/bklim5/python_video_indexer_lib) for his great python_video_indexer_lib.


<iframe width="580" height="780" src="https://www.videoindexer.ai/embed/insights/247da5ad-66e3-4284-bdba-be073a8f32e7/10bb0407d5/" frameborder="0" allowfullscreen></iframe>

