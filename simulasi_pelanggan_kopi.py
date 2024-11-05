import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parameter-parameter untuk model pelanggan
capacity = 5000  # Kapasitas maksimum pelanggan
initial_customers = 500  # Jumlah pelanggan awal
new_customers_rate = 15  # Laju pelanggan baru masuk per menit
churn_rate = 5  # Laju pelanggan keluar per menit
time_steps = 300  # Total waktu simulasi dalam menit

# Definisikan model dinamika pelanggan
def model(customers, t, new_rate, churn_rate, capacity):
    # Pelanggan bertambah dengan laju new_customers_rate dan berkurang dengan laju churn_rate
    # Model ini juga mempertimbangkan kapasitas maksimum pelanggan
    dC_dt = new_rate - churn_rate  # perubahan jumlah pelanggan per waktu
    # Pastikan pelanggan tidak melebihi kapasitas maksimum atau negatif
    if customers + dC_dt > capacity:
        return 0  # Kapasitas penuh, tidak ada pertumbuhan pelanggan lebih lanjut
    if customers + dC_dt < 0:
        return 0  # Tidak ada pelanggan yang tersisa
    return dC_dt

# Rentang waktu simulasi (dalam menit)
waktu_simulasi = np.linspace(0, time_steps, time_steps+1)

# Kondisi awal jumlah pelanggan
initial_conditions = initial_customers

# Menyelesaikan ODE untuk model pelanggan menggunakan odeint
hasil_simulasi = odeint(model, initial_conditions, waktu_simulasi, args=(new_customers_rate, churn_rate, capacity))

# Menampilkan hasil plot
plt.figure(figsize=(10, 5))

# Plot jumlah pelanggan
plt.plot(waktu_simulasi, hasil_simulasi, 'b-', label="Jumlah Pelanggan")
plt.axhline(y=capacity, color='r', linestyle='--', label="Kapasitas Maksimum")

# Menambahkan label dan judul
plt.xlabel('Waktu (menit)')
plt.ylabel('Jumlah Pelanggan')
plt.title('Simulasi Peningkatan Jumlah Pelanggan pada Pedagang Kopi')
plt.legend()
plt.grid(True)

# Tampilkan grafik
plt.show()
