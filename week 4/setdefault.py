kontak = {'Fadhli': '08123456789'}
print("Sebelum setdefault:", kontak)
kontak.setdefault('Andi', '08234567890')
kontak.setdefault('Fadhli', '09000000000')
print("Setelah setdefault:", kontak)