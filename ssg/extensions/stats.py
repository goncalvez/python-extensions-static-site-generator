from ssg import hooks
import time

start_time = None
total_writen = 0

@hooks.register("start_build")
def start_build():
    global start_time = time.time()
    
@hooks.register("written")
def written():
    global total_writen += 1

@hooks.register("stats")
def stats():
    final_time = start_time

    if total_writen != 0:
        average = final_time / total_writen

    


