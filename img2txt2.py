from PIL import Image
import sys

file = open('text.txt', 'r')
text = file.read().replace('\n', ' ').replace('\r', '').replace('\t', ' ').replace(' ', '')

#Fungsi mengambil kode warna pada pixel
def get_pixel(image, i, j):
    width, height = image.size
    if i > width or j > height:
        return None

    # Get Pixel
    pixel = image.getpixel((i, j))
    return pixel

input_img = input('Masukkan file gambar (jpg/png): ')

try:
    imagex = Image.open(input_img)
    width0, height0 = imagex.size
except FileNotFoundError:
    print("File tidak ditemukan")
    sys.exit()

baseheight  = int(input('Masukkan tinggi output (Rekomendasi max 70): '))
baseheight = 90 if baseheight == '' else baseheight

contrast = int(input('Adjustmen kontras (10-90): '))
contrast = .5 if contrast == '' or contrast > 90 or contrast < 10 else contrast/100

wpercent = (baseheight / float(height0))
wsize = int(1.4 * int((float(width0) * float(wpercent))))
new_image = imagex.resize((wsize, baseheight), Image.ANTIALIAS)

space_conf=input('Tambahkan spasi pada output? ketik Ya/ Tidak : ')
add_space = ' ' if space_conf.lower() == 'ya' else ''

# Transform to half tones
posTxt=0
print()
print('Apabila output terlalu gelap, naikkan nilai kontras!\n')
for i in range(0, baseheight):# Koordinat Y, baca per baris
    for j in range(0, wsize): # Koordinat X
        # Get Pixels
        p1 = get_pixel(new_image, j, i)

        # Transform to grayscale
        # gray1 = (p1[0] * 0.299)
        sat = (p1[0] * contrast)

        # Change white/ black with characters depending on saturation
        if sat > 200:
            print(' ',end=add_space)
        elif sat > 100:
            print(' ',end=add_space)
        elif sat > 50:
            print('·',end=add_space)
        elif sat > 10:
            print(text[posTxt:(posTxt+1)],end=add_space)
        else:
            print(text[posTxt:(posTxt+1)],end=add_space)

        if posTxt >= len(text):
            posTxt = 0
        else:
            posTxt += 1

    if wsize:
        print('')

print()
print()
