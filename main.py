# Python Tanggal dan Waktu

import time
import calendar

# TICK
# Tick adalah interval waktu dengan satuan detik

ticks = time.time()
print("Berjalan sejak 12:00am, January 1, 1970:", ticks)

localtime = time.localtime(time.time())
print("Waktu Lokal Saat ini:", localtime)

# fungsi asctime mendapatkan waktu yg mudah di baca
localtime = time.asctime(time.localtime(time.time()))
print("Waktu Lokal Saat ini:", localtime)

cal = calendar.month(2021,5)
print(cal)