print("A(m,n) matrisinin boyutlarini giriniz:")
m = int(input("A matrisinin satır sayısını giriniz"))
n = int(input("A matrisinin sütun sayısını giriniz"))


print("B(f,p) matrisinin boyutlarini giriniz:")
f = int(input("B matrisinin satır sayısını giriniz"))
p = int(input("B matrisinin sütun sayısını giriniz"))



if n != f:
    print("Girdiğiniz matrisler çarpılamaz")
    y = input("-----PROGRAM BİTTİ...-----")
else:
    A = [[0 for i in range(n)] for i in range(m)]
    B = [[0 for i in range(p)] for i in range(f)]
    C = [[0 for i in range(p)] for i in range(m)]



    print("A matrisinin elemanlarını giriniz:")
    for i in range(m):
        for j in range(n):
            print("A[{}][{}]".format(i+1, j+1))
            A[i][j] = int(input())
    print("1. matris (A matrisi): ", A)



    print("B matrisinin elemanlarını giriniz:")
    for i in range(f):
        for j in range(p):
            print("B[{}][{}]".format(i+1, j+1))
            B[i][j] = int(input())
    print("2. matris (B matrisi): ", B)



    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

print("Girdiğiniz matrislerin çarpımı:", C, end=' ')
print(' ')

x = input("-----PROGRAM BİTTİ...-----")
print("----------------------")