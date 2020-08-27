def rajut(data):
    hasil = ''                  #buat string kosong, yang nantinya akan menjadi tempat penampungan dari hasil looping
    for i in data:              #membuat loop utk mengambil tiap string
        if i not in hasil:      #jika nilai i belum ada di variabel hasil, maka akan dilanjutkan ke proses penambahan i dari data
            hasil += i          #maka hasil ditambahkan i
    return hasil                #menyimpan nilai hasil
    
print(rajut('CCoCodCode')) # cetak nilai yang telah disimpan di hasil