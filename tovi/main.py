from pytube import YouTube
from video_indexer import VideoIndexer

class ToVI(VideoIndexer):
  def YouTubeToVI(self, 
                  youtube_link,
                  video_name,
                  video_language = "English"):
    yt = YouTube(youtube_link)
    yt_selected = yt.streams.filter(file_extension='mp4').first()
    download = yt_selected.download()
    output_name = download.split("/")[-1]
    video_id = self.upload_to_video_indexer(
              input_filename=output_name,
              video_name=video_name,  # identifier for video in Video Indexer platform, must be unique during indexing time
              video_language=video_language)
    print(f"Upload complete! video_id {video_id}")