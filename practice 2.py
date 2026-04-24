class DaftarTugas:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return 'Semua tugas sudah selesai!'
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return 'Tidak ada tugas yang harus dikerjakan'
        
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
def main():
    tugas = DaftarTugas()
    tugas.push('Laporan MTK')
    tugas.push('Koding Python')
    tugas.push('Tugas B.Indo')
    
    print("Tugas yang masuk:", tugas)
    print("Tugas yang dikerjakan (hapus):", tugas.pop())
    print("Tugas paling atas:", tugas.peek())
    print("Apakah daftar kosong?", tugas.is_empty())
    print("Jumlah tugas:", tugas.size())
    print("Isi stack sekarang:", tugas)

main()