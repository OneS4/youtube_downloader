from pytube import YouTube


def download_video():
    try:
        video = YouTube(input('Ссылка на видео: '))
        print(f'{video.title} ❌', end='')
        video.streams.get_by_resolution('720p').download(f'C:\\Users\\Serfed\\Desktop\\Video',
                                                         skip_existing=True)
        print(f'\r{video.title} ✔')
        input('Готово ✅')
    except:
        print('Не удалось скачать видео')
        input()
