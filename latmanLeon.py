# Carilah artikel berita pada media massa online. Simpan dalam bentuk file *.txt.
# Buatlah program untuk membaca file *.txt tersebut dan membaca file baris demi baris kalimat.
# Untuk setiap kalimat, pecahlah menjadi setiap kata dengan fungsi split(). Simpan kata pada
# variable kata dengan tipe data list. Hasil akhir program ialah variable kata akan menyimpan
# kata unik pada file berita tersebut. Hasil luaran seperti pada gambar 9.1.
namafile = "beritaleon.txt"
kata = []
handle = open(namafile)
line = handle.read()
line_R = line.replace("\n", "")
kata1 = set
kata.extend(list(kata1))

print("=====ISI BERITA=====", "\n", line)
print("=====KATA UNIK=====", "\n",kata)