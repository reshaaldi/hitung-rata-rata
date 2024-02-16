input_str = input("Masukan nilai-nilai numerik, pisahkan dengan koma: ")

nilai_list = input_str.split(",")

nilai_list = [float(nilai) for nilai  in nilai_list]

rata_rata = sum(nilai_list) / len(nilai_list)

print ("Hasil nilai rata-ratanya: ", rata_rata)