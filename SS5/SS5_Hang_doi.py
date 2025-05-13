queue = [1, 2, 3]

## Xem phần tử đầu tiên: 
# print(queue[0]) # 1

## Thêm vào hàng đợi: thêm vào cuối (nối đuôi)
queue.append(4) # queue = [1, 2, 3, 4]

## Lấy ra khỏi hàng đợi (dequeue)
front = queue.pop(0) # queue = [2, 3, 4]
# print(front) # 1

## kiểm tra rỗng: giống hệt với Stack


### Thực hành bài toán: App âm nhạc
import queue
class MP3Player:
    def __init__(self):
        self.song_queue = queue.Queue()
        self.current_song = None
    
    def add_song(self, song):
        
        
    def play_next_song(self):
        
    def skip_song(self):