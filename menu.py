from tkinter import *
from tkinter import ttk
import main
import yazdir

def baslikListele():
    folder_path = "/Users/ilayda/Desktop/PDF"
    title_list = main.read_pdf_titles(folder_path)

    pencere1 = Toplevel()
    pencere1.title("Başlık Listele")
    pencere1.geometry("750x650")

    if title_list:
        title_text = "\n".join(title_list)
    else:
        title_text = "Başlık bulunamadı."

    label = Label(pencere1, text=title_text)
    label.pack()

    buton1 = Button(pencere1, text="Geri", command=pencere1.destroy)
    buton1.pack()

def baslikYazdir():
    folder_path = "/Users/ilayda/Desktop/PDF"
    output_file = 'pdf_titles.txt'

    yazdir.write_pdf_titles_to_txt(folder_path, output_file)

    pencere2 = Toplevel()
    pencere2.title("Başlık Yazdır")
    pencere2.geometry("750x650")

    label = Label(pencere2, text=f"Başlıklar {output_file} dosyasına yazıldı.")
    label.pack()

    buton2 = Button(pencere2, text="Geri", command=pencere2.destroy)
    buton2.pack()

pencere = Tk()
pencere.title("PDF Başlık Okuma ve Yazdırma")
pencere.geometry("700x250")

etiket = Label(pencere, text="PDF Başlık Okuma ve Yazdırma Sistemine Hoşgeldiniz. Çalıştırmak istediğiniz butona tıklayınız.")
etiket2 = Label(pencere, text="-------Menü--------")
etiket.pack()
etiket2.pack()

menuOgeleri = ["Başlık Listele", "Başlık Yazdır", "Çıkış"]
menuFonksiyonlari = [baslikListele, baslikYazdir, pencere.quit]

for idx, oge in enumerate(menuOgeleri):
    ttk.Button(pencere, text=" " + oge, command=menuFonksiyonlari[idx]).pack()

pencere.mainloop()
