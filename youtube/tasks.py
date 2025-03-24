from .models import Youtube, Video, ShortVideo
import requests
import datetime


def get_videos():
    try:
        # VIDEOS
        channel = Youtube.objects.first()
        channel_url = channel.videos_url.split("@")[-1]
        video_count = channel.videos_count

        url_channel_api_id = f'https://youtube.googleapis.com/youtube/v3/channels?forHandle=%40{channel_url}&key=AIzaSyAhWCXF6-HD3lyAZoz126AsYT9eEk_u8Tg'
        response = requests.get(url_channel_api_id)
        data = response.json()
        if 'error' not in data:
            channel_api_id = data['items'][0]['id']

            url_video_info_api_medium = f'https://youtube.googleapis.com/youtube/v3/search?part=snippet&type=video&order=date&videoDuration=medium&maxResults={video_count}&channelId={channel_api_id}&key=AIzaSyAhWCXF6-HD3lyAZoz126AsYT9eEk_u8Tg'
            response = requests.get(url_video_info_api_medium)
            data = response.json()
            medium_videos = data['items']

            url_video_info_api_long = f'https://youtube.googleapis.com/youtube/v3/search?part=snippet&type=video&order=date&videoDuration=long&maxResults={video_count}&channelId={channel_api_id}&key=AIzaSyAhWCXF6-HD3lyAZoz126AsYT9eEk_u8Tg'
            response = requests.get(url_video_info_api_long)
            data = response.json()
            long_videos = data['items']

            all_videos = medium_videos + long_videos
            # Сортировка по дате добавления
            all_videos.sort(key=lambda x: x['snippet']['publishedAt'], reverse=True)

            affected_rows = Video.objects.all().delete()  # Отчистка таблицы

            for video in all_videos[:video_count]:
                id_video = video['id']['videoId']
                video_link = f"https://www.youtube.com/watch?v={id_video}"
                video_title = video['snippet']['title']
                video_image = video['snippet']['thumbnails']['medium']['url']

                publish_datetime = datetime.datetime.fromisoformat(video['snippet']['publishedAt'][:-1])
                publish_date = publish_datetime.date()

                video_object = Video.objects.create(title=video_title, link=video_link, preview=video_image,
                                                    video_id=id_video, date_published=publish_date)
    except Exception as e:
        print(e)


def get_shorts_videos_data():
    try:
        channel = Youtube.objects.first()
        video_count = channel.videos_count
        # #SHORTS
        shorts_playlist_id = channel.shorts_url.split("list=")[-1]

        url_video = f'https://www.googleapis.com/youtube/v3/playlistItems/?playlistId={shorts_playlist_id}&part=snippet&maxResults=50&key=AIzaSyAhWCXF6-HD3lyAZoz126AsYT9eEk_u8Tg'
        response = requests.get(url_video)
        data = response.json()
        if 'error' not in data:
            all_videos = data.get('items', [])

            while 'nextPageToken' in data:
                next_page_token = data['nextPageToken']
                url_video = f'https://www.googleapis.com/youtube/v3/playlistItems/?playlistId={shorts_playlist_id}&part=snippet&maxResults=50&pageToken={next_page_token}&key=AIzaSyAhWCXF6-HD3lyAZoz126AsYT9eEk_u8Tg'
                response = requests.get(url_video)
                data = response.json()
                all_videos.extend(data.get('items', []))

            last_videos = all_videos[-video_count:]

            affected_rows = ShortVideo.objects.all().delete()

            for video in last_videos:
                if (video['snippet']['title'] != 'Private video'):
                    id_video = video['snippet']['resourceId']['videoId']
                    video_link = f"https://www.youtube.com/watch?v={id_video}"
                    video_title = video['snippet']['title']
                    video_image = video['snippet']['thumbnails']['medium']['url']

                    publish_datetime = datetime.datetime.fromisoformat(video['snippet']['publishedAt'][:-1])
                    publish_date = publish_datetime.date()

                    video_object = ShortVideo.objects.create(title=video_title, link=video_link, preview=video_image,
                                                             video_id=id_video, date_published=publish_date)
    except Exception as e:
        print(e)


