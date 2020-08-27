nama = 'Code' # set nama yang mau diuji
def urai(kata): # set function dengan nama urai dan parameternya adalah kata
    z=[]
    for row in range(len(kata)): #looping row pada jumlah kata 
        for column in range(0,row,len(kata)): # lopping column sesuai dengan jumlah row 
            z+=list(kata[:row]) # tambah value list dengan index yang panjangya sesuai hasil looping row 
        z+=list(kata[row]) #tambah value list denga index yang panjangnya sesuai dengan row
    gabung =''.join(z) #setelah itu ubah list z menjadi string dengan cara di gabung
    return gabung # kembalikan value yang ada di gabung
print (urai(nama)) # cetak return pada fungsi urai



