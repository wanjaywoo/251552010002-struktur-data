class warung_soto: 
    def __init__(self):
        self.mangkuk = []
    
    def tambah_pesanan(self, item):
        self.mangkuk.append(item)
    
    def hidangkan(self):
        if not self.is_empty():
            return self.mangkuk.pop() 
        return "soto habis"
    
    def cek_paling_atas(self):
        if not self.is_empty():
            return self.mangkuk[-1]
        
    def is_empty(self):
        return len(self.mangkuk) == 0