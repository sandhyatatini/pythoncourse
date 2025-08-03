def count_up_to(n):
    count=1
    while count<=n:
        yield count
        count+=1
counter=count_up_to(5)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
#-------------------
def square_numbers(n):
    for i in range(1,n):
        yield i*i
squares=square_numbers(5)
print(next(squares))
print(next(squares))
#-------------------
def square_number(n):
    result=[]
    for i in range(1,n):
        result.append(i*i)
    return result
print(square_number(5))
#---------------------
def stream_video(chunks):
    for chunk in chunks:
        yield chunk
video_chunks=["chunk1","chunk2","chunk3"]
player=stream_video(video_chunks)
print(next(player))
#--------------------
def fetch_posts():
    post_id=1
    while True:
        yield f"Post {post_id}"
        post_id+=1
news_feed=fetch_posts()
print(next(news_feed))
print(next(news_feed))