# // Antrian Kendaraan di Gerbang Tol
queue = []

# Operasi enqueue (menambahkan kendaraan ke antrian)
queue.append("Mobil Alfard")
queue.append("Mobil Toyota")
queue.append("Mobil Ferari")
queue.append("Truck Mitsubishi")

print("Queue setelah operasi enqueue:", queue)
print(f"Jumlah kendaraan dalam antrian: {len(queue)}\n")

# Operasi dequeue (mengeluarkan kendaraan dari antrian)
print("Kendaraan yang keluar dari antrian (dequeue):", queue.pop(0))
print("Sisa kendaraan dalam antrian:", queue)
print("Kendaraan terdepan saat ini:", queue[0] if len(queue) > 0 else "Antrian kosong")
print(f"Jumlah kendaraan dalam antrian: {len(queue)}\n")

print("Kendaraan yang keluar dari antrian (dequeue):", queue.pop(0))
print("Sisa kendaraan dalam antrian:", queue)
print("Kendaraan terdepan saat ini:", queue[0] if len(queue) > 0 else "Antrian kosong")
print(f"Jumlah kendaraan dalam antrian: {len(queue)}\n")

print("Kendaraan yang keluar dari antrian (dequeue):", queue.pop(0))
print("Sisa kendaraan dalam antrian:", queue)
print("Kendaraan terdepan saat ini:", queue[0] if len(queue) > 0 else "Antrian kosong")
print(f"Jumlah kendaraan dalam antrian: {len(queue)}\n")

# Memeriksa apakah antrian kosong
print("Apakah antrian kosong?:", len(queue) == 0)


