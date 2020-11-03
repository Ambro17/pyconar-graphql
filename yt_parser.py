import json
import re
from videos_2018 import a2018
from videos_2019 import a2019


def dump_videos_info(yt_data, filename):
    items = yt_data['items']
    videos = [{
        'title': item['snippet']['title'],
        'video': f"https://www.youtube.com/watch?v={item['snippet']['resourceId']['videoId']}"
    } for item in items]
          
    with open(filename, 'w') as f:
        json.dump(videos, f, ensure_ascii=False, indent=4)

#dump_videos_info(a2018, 'videos_2018.json')
#dump_videos_info(a2019, 'videos_2019.json')
with open('pyconar/data/charlas.json', 'r') as f: charlas = json.load(f)
#charlas_2018_titles = [re.split('[,.]', x['title'], maxsplit=1)[0] for x in charlas['2018']]
#yt_2018 = [re.split('[,.]', x['title'], maxsplit=1)[0] for x in videos]
video_with_titles = [
    {
        'title': item['snippet']['title'],
        'video': f"https://www.youtube.com/watch?v={item['snippet']['resourceId']['videoId']}"
    }
    for item in a2018['items']
]
videos_2019 = [
    {
        'title': item['snippet']['title'],
        'video': f"https://www.youtube.com/watch?v={item['snippet']['resourceId']['videoId']}"
    }
    for item in a2019['items']
]

#diff = set(charlas_2018_titles) - set(yt_2018)
#print(len(diff), diff)
#print('charlas 2018:', len(charlas['2018']))
print('charlas 2019:', len(charlas['2019']))
print('videos 2019:', len(videos_2019))
has_video = [
    x['title'] 
    for x in charlas['2019']
    if any(x['title'][:10].lower() in video['title'].lower() for video in videos_2019)
]
doesnt_have_video = [
    x['title'] 
    for x in charlas['2019']
    if not any(x['title'][:10].lower() in video['title'].lower() for video in videos_2019)    
]

def save_video_info_to_charlas(charlas, year, videos, filename):
    sin_video = []
    for charla in charlas[year]:
        video = next((vid for vid in videos if charla['title'][:10].lower() in vid['title'].lower()), None)
        if video:
            charla['video'] = video['video']
        else:
            charla['video'] = 'No hay video para esta charla :('
            sin_video.append(charla)

    print(f"Charlas without video={len(sin_video)}")
    with open(filename, 'w') as f:
        json.dump(charlas, f, ensure_ascii=False, indent=4)

print('Has Video: ', len(has_video), 'Doesnt: ', len(doesnt_have_video))
import pprint
pprint.pprint(doesnt_have_video)
#save_video_info_to_charlas(charlas, '2018', video_with_titles, 'pyconar/data/charlas.json')

save_video_info_to_charlas(charlas, '2019', videos_2019, 'pyconar/data/charlas.json')
