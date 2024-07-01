import time
from playsound import playsound

def pomodoro_timer(work_duration, break_duration, cycles):
    for cycle in range(cycles):
        print(f"Pomodoro {cycle + 1}")
        print("Çalışma zamanı!")
        time.sleep(work_duration)
        playsound('work_end.mp3')  # Çalışma süresi bittiğinde çalınacak ses
        print("Mola zamanı!")
        time.sleep(break_duration)
        playsound('break_end.mp3')  # Mola süresi bittiğinde çalınacak ses
    print("Pomodoro tamamlandı!")

# 25 dakika çalışma, 5 dakika mola, 4 döngü
pomodoro_timer(25 * 60, 5 * 60, 4)
