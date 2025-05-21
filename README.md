# kutuphane-sistemi
Kütüphane Yönetim Sistemi - Proje Dokümantasyonu
1. Proje Analizi
🎯 Amaç:
Kütüphane kitaplarının takibini yapmak, kullanıcıların kitap ödünç alıp iade etmelerini sağlamak.
👥 Kullanıcı Türleri:
- Kütüphane Görevlisi: Kitap ve üye ekleyebilir, ödünç işlemlerini yönetebilir.
📌 Temel İşlevler:
- Kitap ekleme
- Üye ekleme
- Kitap ödünç alma
- Kitap iade etme
- Ödünç alınan kitapları listeleme
2. Sınıf Tanımları
📚 Kitap Sınıfı
- Özellikler:
  - kitap_id: (str) Kitap kimliği
  - ad: (str) Kitap adı
  - yazar: (str) Kitap yazarı
  - odunc_durumu: (bool) Ödünçte mi?
- Metotlar:
  - durum_guncelle(durum: bool): Ödünç durumunu günceller.
👤 Üye Sınıfı
- Özellikler:
  - uye_id: (str) Üye kimliği
  - ad: (str) Ad
  - soyad: (str) Soyad
🔄 Odunc Sınıfı
- Özellikler:
  - odunc_kayitlari: (list) Ödünç kayıtlarını tutar.
- Metotlar:
  - odunc_al(uye, kitap): Kitap ödünç alma işlemini yapar.
  - iade_et(uye, kitap): Kitabı iade eder.
  - odunc_bilgisi(): Tüm ödünç kayıtlarını listeler.
3. Veri Yapıları
Veri Türü	Kullanılan Yapı	Açıklama
Kitaplar	list[Kitap]	Kütüphanedeki tüm kitapları tutar.
Üyeler	list[Üye]	Kütüphane üyelerini tutar.
Ödünç Kayıtları	list[dict]	Kitap ve üye eşleşmeleriyle ödünç bilgilerini saklar.
4. Arayüz Tasarımı
Kullanıcı Arayüzü:
- Kitap ekleme formu
- Üye ekleme formu
- Mevcut kitap ve üye listeleri
- Ödünç alma ve iade butonları
- Ödünç bilgilerini listeleyen alan
Kullanılan Teknoloji:
- tkinter modülü ile masaüstü GUI
5. Kodlama
Sınıflar ve metotlar Python dilinde oluşturulmuştur. Kodlama sırasında nesne yönelimli programlama (OOP) prensipleri izlenmiştir.
6. Sistem Testi
Test Edilecek İşlevler:
- Kitap ve üye ekleme çalışıyor mu?
- Aynı kitap birden fazla kez ödünç verilebiliyor mu? (Verilmemeli)
- Ödünç alınan kitaplar listeleniyor mu?
- İade işlemi sonrası kitap tekrar ödünç alınabiliyor mu?
7. Kullanım Kılavuzu
Adım Adım:
1. Kitap Ekle: Kitap bilgilerini girin ve ekleyin.
2. Üye Ekle: Üye bilgilerini girin ve ekleyin.
3. Ödünç Al: Listelerden kitap ve üye seçin, ödünç alma butonuna basın.
4. İade Et: Aynı yollarla iade işlemini gerçekleştirin.
5. Ödünç Bilgileri: Güncel ödünç kayıtlarını görüntüleyin.
8. Geliştirme Önerileri
📈 İleri Seviye Geliştirmeler:
- Tarih bilgisi eklenmesi (ödünç tarihi, iade tarihi)
- Arama ve filtreleme özellikleri
- JSON veya veritabanı ile veri kalıcılığı
- Geç iade ve ceza sistemi
- Giriş yapma özelliği ile kullanıcı yönetimi
