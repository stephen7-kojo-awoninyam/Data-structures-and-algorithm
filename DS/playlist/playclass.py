

class Song:
    def __init__(self,artist,title,duration):
        self.artist = artist
        self.title = title
        self.duration = duration
        self.next = None
    def __repr__(self):
        return "<Artist:%s,Title:%s,Duration:%s>"%(self.artist,self.title,self.duration) 
    
class Playlist:
  
    def __init__(self):
        self.head = None
        
    def add(self,artist,title,duration):
        song = Song(artist,tile,durattion)
        self.head = song
        song.next = self.head
        
    def remove(self,song):
        current = self.head
        if current.artist == song.artist:
            current.next_node = None
        else:
            while current:
                current = current.next_node
                if current.artist == song.artist:
                    current.next = song.next
                    print("Remove successfully") 
                else:
                    continue
        return None
    def play_next(self,song):
        current = song.next
        return current
    def play_previous(self,song):
        if song == self.head:
            return None
        
        
                    
                           
    