import random
import time

while True:
    print()
    rd1 = random.randint(1, 10)
    rd2 = random.randint(1, 10)
    print(f"Apa Jawaban Dari: {rd1} + {rd2}")
    
    start_time = time.time()  # Catat waktu mulai
    
    ipt = int(input("Masukkan Jawaban: "))
    
    end_time = time.time()  # Catat waktu berakhir
    
    if ipt == rd1 + rd2:
        elapsed_time = end_time - start_time
        print("Jawaban Benar")
        print(f"Waktu yang Dibutuhkan: {elapsed_time:.2f} detik")
    else:
        print(f"Salah!, Jawabannya Adalah: {rd1 + rd2}")
