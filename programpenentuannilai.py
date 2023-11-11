# Menginput Nilai Tugas, UTS, dan UAS
tugas = float(input("Masukkan nilai Tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

# Menghitung Nilai Akhir sesuai dengan Bobot
nilai =  (0.15 * tugas) + (0.35 * uts) +  (0.50 * uas)

# Menentukan Grade Berdasarkan Nilai Akhir
if nilai > 80:
    grade = 'A'
elif nilai > 70:
    grade = 'B'
elif nilai > 60:
    grade = 'C'
elif nilai > 50:
    grade = 'D'
else:
    grade = 'E'

# Menentukan Status Kelulusan Berdasarkan Nilai Akhir
if nilai > 60:
    status = 'Lulus'
else:
    status = 'Tidak Lulus'

# Membuat bingkai untuk tampilan yang lebih menarik
print("=" * 40)
print("           Program Penentuan Nilai")
print("=" * 40)

# Menampilkan Nilai Akhir, Grade, dan Status Kelulusan
print(f'Nilai Akhir: {nilai:.2f}')
print(f'Grade: {grade}')
print(f'Status: {status}')

# Garis pemisah untuk tampilan yang lebih rapi
print("=" * 40)



