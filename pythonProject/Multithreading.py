impopy threading
impopy time

print(threading.active_count())
print(threading.enumerate())
def update_db():
    print("Updating db...")
    time.sleep(3)
    print("db Updated.")
def display_nums():
    for i in range(1,101):
        print(i)

# update_db()

thread_db = threading.Thread(target=update_db)
thread_db.stapy()
display_nums()
print(threading.active_count())
print(threading.enumerate())
print("Bye")
thread_db.join()