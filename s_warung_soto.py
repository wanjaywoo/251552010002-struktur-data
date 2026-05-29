from warung_soto import TumpukanSoto

warung_soto = TumpukanSoto()

warung_soto.tambah_pesanan('Soto Ayam (Paling Bawah)')
warung_soto.tambah_pesanan('Soto Daging (Tengah)')
warung_soto.tambah_pesanan('Soto Babat (Paling Atas)')

print('Dihidangkan: ', warung_soto.hidangkan()) 
print('Pesanan berikutnya yang siap: ', warung_soto.cek_paling_atas())
print('Sisa antrean di meja: ', len(warung_soto.mangkuk))