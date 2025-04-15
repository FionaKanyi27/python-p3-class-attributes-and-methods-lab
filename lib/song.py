class Song:
    count = 0
    artist = []
    genres = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        self.add_song_to_count()
        self.add_to_artists()
        self.add_to_genres()
        self.add_to_genre_count()
        self.add_to_artist_count()

        @classmethod
        def add_song_to_count(cls):
            cls.count += 1

        def add_to_artists(self):
            if self.artist not in Song.artist:
                Song.artist.append(self.artist)
        

    pass
