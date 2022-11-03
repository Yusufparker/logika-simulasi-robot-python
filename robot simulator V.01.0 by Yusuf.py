'''
Simulasi Robot dalam Gudang Berbasis Python
Crated by Muhammad Yusuf
Information Technology of Institut Teknologi Indonesia

Program Name : Robot Simulator Sederhana V.01.0
'''


import os
os.system('cls')
import time


def help():
    print('''
Bantuan :
- r = robot berjalan ke kanan
- l = robot berjalan ke kiri
- u = robot berjalan ke atas
- d = robot berjalan ke bawah
- pi = mengambil barang
    - r = robot mengambil barang yang ada di sebelah kanan
    - l = robot mengambil baarang yang ada di sebelah kiri
    - u = robot mengambil barang yang ada di atas
    - d = robot mengambil barang yang ada di bawah
- pu = meletakan barang
    - r = robot meletakan barang yang dibawa ke sebelah kanan
    - l = robot meletakan baarang yang dibawa ke sebelah kiri
    - u = robot meletakan barang yang dibawa ke atas
    - d = robot meletakan barang yang dibawa ke bawah
- w = mencetak kondisi gudang saat ini

Simbol :
- * = lantai rusak
- 1 = barang
- x = robot
- o = pintuk keluar

Perhatian :
- robot harus bisa anda bawa ke pintu keluar (o)
- robot tidak bisa melewati dinding gudang
- robot tidak bisa melewati barang atau lantai yang rusak (*)
- robot bisa memindahkan barang (1)
- robot hanya bisa membawa satu barang (1)
- robot tidak bisa memindahkan barang ke lantai yang rusak (*) dan pintu keluar (o)
''')



def show(list2D):
    print('_'*colom*2)
    for i in list2D:
        i = ' '.join(i)
        print(i)
    print('_'*colom*2)

def anyWall():
    print('Mau kemana? ada dinding disana!')

def succes(level):
    print(f'Level {level-1} berhasil....\n')

def anyObject():
    print('Ada barang di sana!')

def brokenFloor():
    print('Ada lantai rusak di sana!')

def wall(posisi):
    print(f'Ada dinding di {posisi}')

def no_objek(posisi):
    print(f'Tidak ada barang di {posisi}')

def noPut_lantaiRusak(posisi):
    print(f'Tidak dapat meletakan barang!\nAda lantai rusak di {posisi}!')

def noPut(posisi):
    print(f'Tidak dapat meletakan barang!\nsudah ada barang di {posisi}!')

def main(line,colom,list2D,pick):
    
    while list2D[line-1][colom-1]!='x':
        for i in range (line):
        #kolom = len(list2D[i])
            for j in range (colom):
                if list2D[i][j] == "x":
                #informasi robot
                    robotx=i
                    roboty=j
                    
        command = input('Masukkan Perintah (tekan h untuk bantuan): ').lower()

        if command == 'u':
            if robotx-1<0:
                anyWall()
            else:
                if list2D[robotx-1][roboty]==' ':
                    list2D[robotx-1][roboty]='x'
                    list2D[robotx][roboty]=' '
                    show(list2D)
                elif list2D[robotx-1][roboty]=='1':
                    anyObject()
                elif list2D[robotx-1][roboty]=='*':
                    brokenFloor()

        elif command == 'd':
            if robotx+1>line-1:
                anyWall()
            else:
                if list2D[robotx+1][roboty]==' ':
                    list2D[robotx+1][roboty]='x'
                    list2D[robotx][roboty]=' '
                    show(list2D)
                elif list2D[robotx+1][roboty]=='1':
                    anyObject()
                elif list2D[robotx+1][roboty]=='*':
                    brokenFloor()

                elif list2D[robotx+1][roboty]=='o':
                    if pick == False:
                        list2D[robotx+1][roboty]='x'
                        list2D[robotx][roboty]=' '
                    else:
                        print('Anda sedang membawa barang!\nTaruh barang terlebih dahulu!')
                        time.sleep(0.5)
                        show(list2D)                        
     
        elif command == 'l':
            if roboty-1<0:
                    anyWall()
            else:
                if list2D[robotx][roboty-1]==' ':
                    list2D[robotx][roboty-1]='x'
                    list2D[robotx][roboty]=' '
                    show(list2D)
                elif list2D[robotx][roboty-1]=='1':
                    anyObject()
                elif list2D[robotx][roboty-1]=='*':
                    brokenFloor() 

        elif command == 'r':
            if roboty+1>colom-1:
                anyWall()
            else:
                if list2D[robotx][roboty+1]==' ':
                    list2D[robotx][roboty+1]='x'
                    list2D[robotx][roboty]=' '
                    show(list2D)
                elif list2D[robotx][roboty+1]=='1':
                    anyObject()
                elif list2D[robotx][roboty+1]=='*':
                    brokenFloor()

                elif list2D[robotx][roboty+1]=='o':
                    if pick == False:
                        list2D[robotx][roboty+1]='x'
                        list2D[robotx][roboty]=' '
                    else:
                        print('Anda sedang membawa barang!\nTaruh barang terlebih dahulu!')
                        time.sleep(0.5)
                        show(list2D)

        elif command == 'w':
            show(list2D)

        elif command =='pi':
                    if pick==True:
                        print('Maaf, Anda sedang membawa barang')
                    else:
                        arah=input('Tentukan arah barang yang ingin di ambil: ')
                        if arah=='u':
                            posisi='atas'
                            if robotx-1<0:
                                wall(posisi)
                            else:
                                if list2D[robotx-1][roboty]==' 'or list2D[robotx+1][roboty]=='*':
                                    no_objek(posisi)
                                elif list2D[robotx-1][roboty]=='1':
                                    pick=True
                                    print('Barang ditemukan')
                                    list2D[robotx-1][roboty]=' '
                                    print('Mengambil barang...')
                                    show(list2D)

                        elif arah=='d':
                            posisi='bawah'
                            if robotx+1>line-1:
                                wall(posisi)
                            else:
                                if list2D[robotx+1][roboty]==' ' or list2D[robotx+1][roboty]=='*':
                                    no_objek(posisi)

                                elif list2D[robotx+1][roboty]=='1':
                                    pick=True
                                    print('Barang ditemukan')
                                    list2D[robotx+1][roboty]=' '
                                    print('Mengambil barang...')
                                    show(list2D)

                        elif arah=='r':
                            posisi='kanan'
                            if roboty+1>colom-1:
                                wall(posisi)
                            else:
                                if list2D[robotx][roboty+1]==' ' or list2D[robotx][roboty+1]=='*':
                                    no_objek(posisi)
                                elif list2D[robotx][roboty+1]=='1':
                                    pick=True
                                    print('Barang ditemukan')
                                    list2D[robotx][roboty+1]=' '
                                    print('Mengambil barang...')
                                    show(list2D)
                        
                        elif arah=='l':
                            posisi='kiri'
                            if roboty-1<0:
                                wall(posisi)
                            else:
                                if list2D[robotx][roboty-1]==' ' or list2D[robotx][roboty-1]=='*':
                                    no_objek(posisi)
                                elif list2D[robotx][roboty-1]=='1':
                                    pick=True
                                    print('Barang ditemukan')
                                    list2D[robotx][roboty-1]=' '
                                    print('Mengambil barang...')
                                    show(list2D)

                        else:
                            print('Arah tak diketahui!')


        elif command == 'pu':
            if pick==False:
                print('Ambil barang terlebih dahulu!')
            else:
                arah=input('Tentukan arah untuk meletakan barang: ')
                if arah =='u':
                    posisi='atas'
                    if robotx-1<0:
                        wall(posisi)
                    else:
                        if list2D[robotx-1][roboty]=='1':
                            noPut(posisi)
                        
                        elif list2D[robotx-1][roboty]=='*':
                            noPut_lantaiRusak(posisi)

                        elif list2D[robotx-1][roboty]==' ':
                            pick=False
                            print('Letakkan barang secara perlahan...')
                            list2D[robotx-1][roboty]='1'
                            show(list2D)

                elif arah == 'd':
                    posisi='bawah'
                    if robotx+1>line-1:
                        wall(posisi)
                    else:
                        if list2D[robotx+1][roboty]=='1':
                            noPut(posisi)
                        
                        elif list2D[robotx+1][roboty]=='*':
                            noPut_lantaiRusak(posisi)

                        elif list2D[robotx+1][roboty]=='o':
                            print('Tidak dapat meletakan barang di pintu keluar!')

                        elif list2D[robotx+1][roboty]==' ':
                            pick=False
                            print('Letakkan barang secara perlahan...')
                            list2D[robotx+1][roboty]='1'
                            show(list2D)

                elif arah == 'r':
                    posisi='kanan'
                    if roboty+1>colom-1:
                        wall(posisi)    
                    else:
                        if list2D[robotx][roboty+1]=='1': 
                            noPut(posisi)

                        elif list2D[robotx][roboty+1]=='*':
                            noPut_lantaiRusak(posisi)

                        elif list2D[robotx][roboty+1]=='*':
                            print('Tidak dapat meletakan barang di pintu keluar!')

                        elif list2D[robotx][roboty+1]==' ':
                            pick=False
                            print('Letakkan barang secara perlahan...')
                            list2D[robotx][roboty+1]='1'     
                            show(list2D)     

                elif arah=='l':
                    posisi='kiri'
                    if roboty-1<0:
                        wall(posisi)
                    else:
                        if list2D[robotx][roboty-1]=='1':
                            noPut(posisi)
                        
                        elif list2D[robotx][roboty-1]=='*':
                            noPut_lantaiRusak(posisi)
                
                        elif list2D[robotx][roboty-1]==' ':
                            pick=False
                            print('Letakkan barang secara perlahan...')
                            list2D[robotx][roboty-1]='1'
                            show(list2D)                    
                else:
                    print(f'Arah tak {arah} diketahui!')

        elif command == 'h':
            asking=input('Apakah anda yakin? (y/n)\n>').lower()
            if asking == 'y':
                time.sleep(1)
                help()
                time.sleep(1)
                show(list2D)
            elif asking =='n':
                time.sleep(1)
                show(list2D)
                continue
            else:
                print('Program tidak mengerti!')
                show(list2D)        

        else:
            print('Perintah tidak diketahui')


level1 = [['x',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ','o']]

level2 = [['x',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ','1',' ',' ',' ',' ',' ',' '],                  
          ['*',' ',' ',' ',' ',' ',' ','o']]


level3 = [['x','1',' ',' ',' ',' ',' ',' '],
         ['1',' ',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ','1',' ',' ',' ',' ',' ',' '],                  
          ['*',' ',' ',' ',' ',' ',' ','o']]

level4 = [['x','1','*',' ',' ',' ',' ',' '],
         ['1','*',' ',' ',' ',' ',' ',' '],
         [' ',' ',' ',' ',' ',' ',' ',' '],
         [' ','1',' ',' ',' ',' ',' ',' '],                  
          ['*',' ',' ',' ',' ',' ','1','o']]

level5 = [['x','1','*',' ',' ',' ',' ',' '],
         ['1','*',' ',' ',' ',' ',' ',' '],
         [' ',' ','1',' ',' ',' ',' ',' '],
         ['*','1',' ',' ',' ',' ','1','1'],                  
          [' ',' ',' ',' ',' ',' ','1','o']]

level6 = [['x','1','*',' ',' ',' ',' ',' '],
         ['1','*',' ',' ',' ',' ',' ',' '],
         [' ','1','1',' ',' ',' ',' ','*'],
         ['*','1',' ',' ',' ','*','1','1'],                  
          [' ',' ',' ',' ',' ',' ','1','o']]

level7 = [['x',' ',' ',' ',' ',' ',' ','1'],
         ['*','*','*','*','*','*','*','1'],
         [' ','1','1',' ',' ',' ',' ','1'],
         ['*','1',' ',' ',' ','*','1','*'],                  
          [' ',' ',' ',' ',' ',' ','1','o']]


level = 1
pick = False

print('''
Selamat Datang di Robot Simulator V.01.0
__________________________________________''')


name = input('Masukkan username: ')
while name == '':
    nama = input('masukkan nama anda: ')
print('Loading...')
time.sleep(1)
print('Tunggu sebentar...\n')
time.sleep(1)

while True:

    if level==1:
        colom = len(level1[0])
        line = len(level1)
        print(f'level : {level}')
        show(level1)
        main(line,colom,level1,pick)
        show(level1)
        level+=1
        succes(level)
        time.sleep(1.7)

    elif level == 2:
        colom = len(level2[0])
        line = len(level2)
        print(f'level : {level}')
        show(level2)
        main(line, colom, level2,pick)
        show(level2)
        level+=1
        succes(level)
        time.sleep(1.7)
    
    elif level == 3 :
        colom = len(level3[0])
        line = len(level3)
        print(f'level : {level}')
        show(level3)
        main(line, colom, level3,pick)
        show(level3)
        level+=1
        succes(level)
        time.sleep(1.7)

    elif level == 4 :
        colom = len(level4[0])
        line = len(level4)
        print(f'level : {level}')
        show(level4)
        main(line, colom, level4,pick)
        show(level4)
        level+=1
        succes(level)
        time.sleep(1.7)

    elif level == 5 :
        colom = len(level5[0])
        line = len(level5)
        print(f'level : {level}')
        show(level5)
        main(line, colom, level5,pick)
        show(level5)
        level+=1
        succes(level)
        time.sleep(1.7)

    elif level == 6 :
        colom = len(level6[0])
        line = len(level6)
        print(f'level : {level}')
        show(level6)
        main(line, colom, level6,pick)
        show(level6)
        level+=1
        succes(level)
        time.sleep(1.7)

    elif level == 7 :
        colom = len(level7[0])
        line = len(level7)
        print(f'level : {level}')
        show(level7)
        main(line, colom, level7,pick)
        show(level7)
        level+=1
        succes(level)
        time.sleep(1.7)

    else:
        print(f'Selamat {name}! Anda telah menyelesaikan permainan!')
        print('permainan selesai')
        print(f'Sorry! baru bikin sampe level {level-1} :v')
        break



        