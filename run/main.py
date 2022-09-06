from imports import *


def run():
    match input('Что скачать (1 - видео, 2 - плейлист, остальное - выход): '):
        case '1':
            video.download_video()
        case '2':
            playlist.download_playlist()
