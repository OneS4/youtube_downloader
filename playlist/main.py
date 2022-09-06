from pytube import Playlist


def download_playlist():
    try:
        playlist = Playlist(input('Ссылка на плейлист: '))
        title = list(playlist.title)
        for i, char in enumerate(title):
            if char in r'\/:*?"<>|':
                title[i] = ''
        title = "".join(title)
        begin = int(input('С какого видео по индексу начать скачивание: ')) - 1
        end = int(input('До какого индекса (включительно): '))
        print(f'Скачивание плейлиста: {title}')
        for video in playlist.videos[begin:end]:
            print(f'{video.title} ❌', end='')
            video.streams.get_by_resolution('720p').download(f'C:\\Users\\Serfed\\Desktop\\Video\\{title}',
                                                             skip_existing=True)
            print(f'\r{video.title} ✔')
        input('Готово ✅')
    except:
        print('Не удалось скачать плейлист')
        input()
