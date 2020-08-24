import time
import threading
import random


class JukeBox:
    def __init__(self, balance=0, songs=None):
        self.__balance = balance
        self.__songs = songs if songs else dict()
        self.__is_autoplay = False
        self.__is_next = False

    def get_songs_list(self):
        for song in self.__songs:
            print(song)

    def play_song(self, song_id):
        if song_id not in self.__songs:
            raise KeyError("THERE IS NO SONG WITH THIS ID")
        print('NOW PLAYING: {}'.format(self.__songs[song_id]))
        time.sleep(song_id.duration)

    def play_next(self, song_id):
        self.__is_next = True
        if self.__is_autoplay:
            self.__wait_until_autoplay_song_end()
        self.play_song(song_id)
        self.__is_next = False

    def __wait_until_autoplay_song_end(self):
        while True:
            time.sleep(1)
            if not self.__is_autoplay:
                return

    def add_song(self, song):
        self.__songs.update({song.id: song})

    def remove_song(self, song_id):
        del self.__songs[song_id]

    def autoplay(self):
        while True:
            self.__is_autoplay = True
            random_song_id = self.__pick_random_song_id()
            self.play_song(random_song_id)
            if self.__is_next:
                self.__is_autoplay = False
                self.__wait_until_next_song_end()

    def __wait_until_next_song_end(self):
        while True:
            time.sleep(1)
            if not self.__is_next:
                return

    def __pick_random_song_id(self):
        return random.choice(list(self.__songs.keys()))


class Song:
    def __init__(self, id, name, duration):
        self.id = id
        self.name = name
        self.duration = duration

    def __str__(self):
        return '{}. {} - {}'.format(self.id, self.name, self.duration)
