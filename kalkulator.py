# module
import os,sys,time,subprocess
# daftar menu
def penjumlahan(y,x):
    return y+x
def perkalian(y,x):
    return y*x
def pembagian(y,x):
    return y/x
def pengurangan(y,x):
    return y-x
# menu
os.system("clear")
print("\033[1;95m+\033[1;96m---------------------------------------\033[1;95m+")
print("\033[1;90m[\033[1;93m1\033[1;90m] \033[1;92mpenjumlahan")
print("\033[1;90m[\033[1;93m2\033[1;90m] \033[1;92mperkalian")
print("\033[1;90m[\033[1;93m3\033[1;90m] \033[1;92mpembagian")
print("\033[1;90m[\033[1;93m4\033[1;90m] \033[1;92mpengurangan")
print("\033[1;90m[\033[1;93m0\033[1;90m] \033[1;92mkeluar/exit")
pilih=input("\033[1;96mpilih menu \033[1;93m~\033[1;91m> \033[1;95m")

angka_1 = int(input("masukan angka pertama ~> "))
angka_2 = int(input("masukan angka kedua ~> "))
# menu
# ini untuk penjumlahan
if pilih =="1":
    print(angka_1,"+",angka_2,"=",penjumlahan(angka_1,angka_2))
elif pilih =="2":
     print(angka_1,"*",angka_2,"=",perkalian(angka_1,angka_2))
elif pilih =="3":
    print(angka_1,"/",angka_2,"=",pembagian(angka_1,angka_2))
elif pilih =="4":
    print(angka_1,"-",angka_2,"=",pengurangan(angka_1,angka_2))
elif pilih =="0":
    print("\033[1;96mBye Bye")
    sys.exit()
else:
    print("pilih input dgn benar")
    os.system("python3 kalkulator.py")
