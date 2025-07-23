from PIL import Image

def gambar_ke_ascii_detail(path_gambar, lebar_baru=100>
    """Mengubah gambar menjadi ASCII art yang lebih de>

    Args:
        path_gambar (str): Path ke file gambar.
        lebar_baru (int): Lebar maksimum dari hasil AS>

    Returns:                                                   str: Representasi ASCII art yang lebih detail >
    """
    try:
        gambar = Image.open(path_gambar).convert('L') >
    except FileNotFoundError:
        return "Error: File gambar tidak ditemukan."

    lebar, tinggi = gambar.size                            rasio_aspek = tinggi / lebar
    tinggi_baru = int(lebar_baru * rasio_aspek * 0.55)>
    gambar_resized = gambar.resize((lebar_baru, tinggi>
    piksel = gambar_resized.getdata()

    karakter = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrj>
    panjang_karakter = len(karakter)

    ascii_art = ""
    for pixel_value in piksel:
        index = pixel_value * panjang_karakter // 255
        ascii_art += karakter[panjang_karakter - 1 - i>
    return [ascii_art[i:i+lebar_baru] for i in range(0>

if __name__ == "__main__":
    path_gambar = input("Path lengkap gambar: ")
    lebar_hasil = int(input("Ukuran Ascii: "))

    hasil_ascii = gambar_ke_ascii_detail(path_gambar, >

    if isinstance(hasil_ascii, str) and hasil_ascii.st>
        print(hasil_ascii)
    else:
        for baris in hasil_ascii:
            print(baris)
