class ProdukKosmetik(object):
    nama_produk = None

    def __init__(self, nama_produk):
        self.nama_produk = nama_produk

    def aplikasi(self):
        print('{} siap untuk digunakan di wajah/kulit.'.format(self.nama_produk))


class KosmetikPremium(ProdukKosmetik):
    nama_produk = None
    website = None

    def __init__(self, nama_produk):
        self.nama_produk = nama_produk

    def aplikasi(self):
        print('{} diaplikasikan secara merata untuk hasil terbaik.'.format(self.nama_produk))

    def set_website(self, website):
        self.website = website


pelembab = KosmetikPremium('Moisture Hadalabo milk')
pelembab.set_website('hadalabo.com')
pelembab.aplikasi()

lipstik = KosmetikPremium('Velvet Matte Lipstick')
lipstik.set_website('velvetlips.com')
lipstik.aplikasi()