import time

def countDown(seconds):
    while seconds > 0:
        min, secs = divmod(seconds, 60)
        show_time = '{:02d}:{:02d}'.format(min, secs)
        print(show_time, end='\r')
        time.sleep(1)
        seconds -= 1
    print("00:00 \n Time over!! ⌛")
   

print("  🚦Welcome to the countdown!!!!")
get_seconds =int(input("Enter seconds for countdown timer :"))
countDown(get_seconds)