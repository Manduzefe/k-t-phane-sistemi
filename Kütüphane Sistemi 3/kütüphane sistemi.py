print ('hello world')
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# ---------- Sınıflar ---------- #

class Kitap:
    def __init__(self, kitap_id, ad, yazar, odunc_durumu=False):
        self.kitap_id = kitap_id
        self.ad = ad
        self.yazar = yazar
        self.odunc_durumu = odunc_durumu

    def durum_guncelle(self, durum):
        self.odunc_durumu = durum

class Uye:
    def __init__(self, uye_id, ad, soyad):
        self.uye_id = uye_id
        self.ad = ad
        self.soyad = soyad

class Odunc:
    def __init__(self):
        self.odunc_listesi = []

    def odunc_al(self, uye, kitap):
        if not kitap.odunc_durumu:
            kitap.odunc_durumu = True
            tarih = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.odunc_listesi.append({'uye': uye, 'kitap': kitap, 'tarih': tarih})
            return True
        return False

    def iade_et(self, uye_id, kitap_id):
        for odunc in self.odunc_listesi:
            if odunc['uye'].uye_id == uye_id and odunc['kitap'].kitap_id == kitap_id:
                odunc['kitap'].odunc_durumu = False
                self.odunc_listesi.remove(odunc)
                return True
        return False

    def odunc_bilgisi(self):
        bilgiler = []
        for odunc in self.odunc_listesi:
            bilgiler.append(f"{odunc['uye'].ad} {odunc['uye'].soyad} -> {odunc['kitap'].ad} ({odunc['tarih']})")
        return bilgiler

# ---------- Veriler ---------- #

kitaplar = []
uyeler = []
odunc_yonetimi = Odunc()

# ---------- Arayüz ---------- #

def arayuz_olustur():
    pencere = tk.Tk()
    pencere.title("Kütüphane Yönetim Sistemi")
    pencere.configure(bg="black")

    # Stil
    fg = "white"
    bg = "black"

    # Kitap Ekle
    def kitap_ekle():
        kid = entry_kitap_id.get()
        ad = entry_kitap_ad.get()
        yazar = entry_kitap_yazar.get()
        if kid and ad and yazar:
            kitaplar.append(Kitap(kid, ad, yazar))
            messagebox.showinfo("Başarılı", "Kitap eklendi.")
            entry_kitap_id.delete(0, tk.END)
            entry_kitap_ad.delete(0, tk.END)
            entry_kitap_yazar.delete(0, tk.END)
            guncelle_kitaplar()

    # Üye Ekle
    def uye_ekle():
        uid = entry_uye_id.get()
        ad = entry_uye_ad.get()
        soyad = entry_uye_soyad.get()
        if uid and ad and soyad:
            uyeler.append(Uye(uid, ad, soyad))
            messagebox.showinfo("Başarılı", "Üye eklendi.")
            entry_uye_id.delete(0, tk.END)
            entry_uye_ad.delete(0, tk.END)
            entry_uye_soyad.delete(0, tk.END)
            guncelle_uyeler()

    # Ödünç Al
    def odunc_al():
        try:
            uye = uyeler[listbox_uyeler.curselection()[0]]
            kitap = kitaplar[listbox_kitaplar.curselection()[0]]
            if odunc_yonetimi.odunc_al(uye, kitap):
                messagebox.showinfo("Başarılı", "Ödünç alındı.")
                guncelle_kitaplar()
            else:
                messagebox.showwarning("Uyarı", "Kitap zaten ödünç alınmış.")
        except:
            messagebox.showerror("Hata", "Lütfen bir kitap ve bir üye seçin.")

    # İade Et
    def iade_et():
        try:
            uye = uyeler[listbox_uyeler.curselection()[0]]
            kitap = kitaplar[listbox_kitaplar.curselection()[0]]
            if odunc_yonetimi.iade_et(uye.uye_id, kitap.kitap_id):
                messagebox.showinfo("Başarılı", "İade işlemi tamamlandı.")
                guncelle_kitaplar()
            else:
                messagebox.showwarning("Uyarı", "İade edilecek kayıt bulunamadı.")
        except:
            messagebox.showerror("Hata", "Lütfen bir kitap ve bir üye seçin.")

    # Bilgi Göster
    def odunc_goster():
        bilgiler = odunc_yonetimi.odunc_bilgisi()
        text_bilgi.delete("1.0", tk.END)
        if bilgiler:
            text_bilgi.insert(tk.END, "\n".join(bilgiler))
        else:
            text_bilgi.insert(tk.END, "Henüz ödünç alınmış kitap yok.")

    # Listeleri Güncelle
    def guncelle_kitaplar():
        listbox_kitaplar.delete(0, tk.END)
        for k in kitaplar:
            durum = "Ödünçte" if k.odunc_durumu else "Uygun"
            listbox_kitaplar.insert(tk.END, f"{k.ad} - {k.yazar} ({durum})")

    def guncelle_uyeler():
        listbox_uyeler.delete(0, tk.END)
        for u in uyeler:
            listbox_uyeler.insert(tk.END, f"{u.ad} {u.soyad}")

    # Arayüz Elemanları

    tk.Label(pencere, text="Kitap ID", fg=fg, bg=bg).grid(row=0, column=0)
    entry_kitap_id = tk.Entry(pencere, bg="gray", fg=fg)
    entry_kitap_id.grid(row=0, column=1)

    tk.Label(pencere, text="Kitap Adı", fg=fg, bg=bg).grid(row=1, column=0)
    entry_kitap_ad = tk.Entry(pencere, bg="gray", fg=fg)
    entry_kitap_ad.grid(row=1, column=1)

    tk.Label(pencere, text="Yazar", fg=fg, bg=bg).grid(row=2, column=0)
    entry_kitap_yazar = tk.Entry(pencere, bg="gray", fg=fg)
    entry_kitap_yazar.grid(row=2, column=1)

    tk.Button(pencere, text="Kitap Ekle", command=kitap_ekle, bg="white").grid(row=3, column=1)

    tk.Label(pencere, text="Üye ID", fg=fg, bg=bg).grid(row=4, column=0)
    entry_uye_id = tk.Entry(pencere, bg="gray", fg=fg)
    entry_uye_id.grid(row=4, column=1)

    tk.Label(pencere, text="Ad", fg=fg, bg=bg).grid(row=5, column=0)
    entry_uye_ad = tk.Entry(pencere, bg="gray", fg=fg)
    entry_uye_ad.grid(row=5, column=1)

    tk.Label(pencere, text="Soyad", fg=fg, bg=bg).grid(row=6, column=0)
    entry_uye_soyad = tk.Entry(pencere, bg="gray", fg=fg)
    entry_uye_soyad.grid(row=6, column=1)

    tk.Button(pencere, text="Üye Ekle", command=uye_ekle, bg="white").grid(row=7, column=1)

    # Listboxlar
    tk.Label(pencere, text="Kitaplar", fg=fg, bg=bg).grid(row=0, column=2)
    listbox_kitaplar = tk.Listbox(pencere, width=40)
    listbox_kitaplar.grid(row=1, column=2, rowspan=6)

    tk.Label(pencere, text="Üyeler", fg=fg, bg=bg).grid(row=0, column=3)
    listbox_uyeler = tk.Listbox(pencere, width=40)
    listbox_uyeler.grid(row=1, column=3, rowspan=6)

    # Butonlar
    tk.Button(pencere, text="Ödünç Al", command=odunc_al, bg="white").grid(row=7, column=2)
    tk.Button(pencere, text="İade Et", command=iade_et, bg="white").grid(row=7, column=3)
    tk.Button(pencere, text="Ödünç Bilgileri", command=odunc_goster, bg="white").grid(row=8, column=1, columnspan=2)

    text_bilgi = tk.Text(pencere, height=8, width=80, bg="gray", fg=fg)
    text_bilgi.grid(row=9, column=0, columnspan=4, pady=10)

    pencere.mainloop()

if __name__ == "__main__":
    arayuz_olustur()
