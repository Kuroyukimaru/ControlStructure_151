##Tugas 1
# mendapatkan persentase siswa dari pengguna
percentage = float(input("Enter the student's percentage: ")) #menggunakan float biar menginput nilai menggunakan desimal

# mengevaluasi berdasarkan beberapa kondisi
if percentage >= 90:
    print("Excellent performance")
elif percentage >= 80:
    print("Very Good performance")
elif percentage >= 70:
    print("Good performance")
elif percentage >= 60:
    print("Average performance")
else:
    print("Needs improvement")

#Tugas 2
# menginput 3 nilai berbeda
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

# menemukan angka terbesar
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest =c

print("The largest number is:", largest) #Ngeprin nilai terbesar

#Tugas 3
n = int(input("Masukkan batas bilangan Fibonacci: "))  # Input batas bilangan Fibonacci yang diinginkan

a, b = 0, 1  # Inisialisasi dua elemen pertama Fibonacci
while a <= n:  # Loop hingga nilai a melebihi n
    print(a, end=" ")  # Cetak nilai a saat ini
    a, b = b, a + b # Update nilai a dan b untuk elemen berikutnya
print ("\n") 

#Tugas 4
#Mencetak bilangan ganjil
n = int(input("Masukkan batas atas: "))  # Input batas atas hingga n

for i in range(1, n + 1):  # Loop dari 1 hingga n
    if i % 2 != 0:  # Jika i adalah bilangan ganjil
        print(i, end=" ")  # Cetak bilangan ganjil
print ("\n")

#Tugas 5
n = int(input("Masukkan nilai n: "))  # Input nilai n sebagai batas pola

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()