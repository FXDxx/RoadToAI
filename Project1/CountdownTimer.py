import time

count = 0
finish_time = int(input("Set countdown timer"))
while count <= finish_time:
    print(count)
    count += 1
    time.sleep(2)
