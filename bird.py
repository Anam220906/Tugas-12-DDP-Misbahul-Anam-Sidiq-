from  Animal import  animal

class Bird(animal):
    # konstruktor properti
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, paruh,):
        super().__init__ (nama, makanan,hidup,berkembang_biak,)
        self.warna = warna
        self.paruh = paruh

        # Method 
    def info_bird(self):
        super().info_Animal()
        print("warna\t\t: ", self.warna,
              "\nJenisparuh\t\t\t: ", self.paruh)
            
# Objek 
print()
bird =  bird("Elang","Daging", "Ditebing",
             "Menghasilkan telur", "coklat", "Bengkok dan Lancip")
print("## INFO BRe ##")
bird.info_bird() 

              