#https://www.youtube.com/watch?v=02h0nevMqmY&list=PLto9KpJAqHMQNY3XP0JqLs7NyeU_dnNj0&index=180

import schedule, time
def sendWakeUp():
    print('wakeUp')



schedule.every(2).seconds.do(sendWakeUp)

while True:
    schedule.run_pending()
    time.sleep(1)
