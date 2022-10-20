import time
import datetime
start_time=datetime.datetime.now()
print(f"Job is Started: {start_time}")
time.sleep(10)
end_time=datetime.datetime.now()
print(f"Job is completed: {end_time}")
print(f"Job Duration: {end_time - start_time}")
