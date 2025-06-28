import random

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

class Playlist:
    def __init__(self):
        self._playlist = []

    def add_song(self, song):
        self._playlist.append(song)

    def __iter__(self, mode="normal"):
        return PlaylistIterator(self._playlist, mode)

class PlaylistIterator:
    def __init__(self, playlist, mode="normal"):
        self.mode = mode
        self.playlist = playlist[:]

        if self.mode == "shuffle":
            random.shuffle(self.playlist)
        elif self.mode == "reverse":
            self.playlist.reverse()

        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.playlist):
            song = self.playlist[self.index]
            self.index += 1
            return song.title, song.artist, song.duration
        raise StopIteration


def main():
    playlist = Playlist()

    playlist.add_song(Song("Shape of You", "Ed Sheeran", "4:24"))
    playlist.add_song(Song("Blinding Lights", "The Weeknd", "3:20"))
    playlist.add_song(Song("Levitating", "Dua Lipa", "3:23"))

    print("\n🎧 Normal Order:")
    for song in playlist.__iter__(mode="normal"):
        print(song)

    print("\n🔁 Reverse Order:")
    for song in playlist.__iter__(mode="reverse"):
        print(song)

    print("\n🔀 Shuffled Order:")
    for song in playlist.__iter__(mode="shuffle"):
        print(song)

if __name__ == "__main__":
    main()

