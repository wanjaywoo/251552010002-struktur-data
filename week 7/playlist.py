class SongNode:
    def __init__(self, title):
        self.title = title
        self.next = None

class playlist:
    def __init__(self):
        self.head = None

    def add_song(self,title):
        new_song = SongNode(title)
        if not self.head:
            self.head = new_song
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_song
        print(f"lagu'{title}'ditambahkan kedalam playlist.")

    def show_playlist(self):
        current = self.head
        if not current:
            print("playlist kosong")
            return
        print("playlist:")
        while current:
            print(f"memutar semua lagu:")
            while current:
                print(f"memutar:{current.title}")
                current = current.next

                
    def play_all(self):
        current = self.head
        if not current:
            print("tidak ada lagu yang diputar.")
            return
        print("memutar semua lagu:")
        while current:
            print(f"memutar:{current.title}")
            current = current.next

    
Playlist = playlist()
Playlist.add_song("lagu radioactive")
Playlist.add_song("lagu alan walker")
Playlist.add_song("coldplay")

print()
Playlist.show_playlist()

print()
Playlist.play_all()