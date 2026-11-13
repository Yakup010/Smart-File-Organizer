# 📁 Smart File Organizer

**Smart File Organizer**, bilgisayardaki dosyaları uzantılarına göre otomatik olarak kategorilere ayıran ve ilgili klasörlere taşıyan Python tabanlı bir dosya düzenleme aracıdır.

Bu proje, dosya yönetimini kolaylaştırmak ve manuel dosya düzenleme işlemlerini otomatikleştirmek amacıyla geliştirilmiştir.

## ✨ Özellikler

- Dosyaları uzantılarına göre otomatik kategorilere ayırma
- Resim, belge, video, müzik, arşiv ve yazılım dosyalarını sınıflandırma
- Dosyaları ilgili klasörlere taşıma
- Aynı isimli dosyalarda isim çakışmasını önleme
- Taşıma öncesinde işlem önizlemesi sunma
- Kullanıcı onayıyla dosya taşıma
- İşlem sonuçlarını CSV formatında raporlama
- Başarılı ve başarısız işlemleri kayıt altına alma

## 📂 Dosya Kategorileri

| Kategori | Desteklenen Uzantılar |
|---|---|
| Images | JPG, JPEG, PNG, WEBP |
| Documents | PDF, DOCX, DOC, TXT, CSV, XLSX, XLS |
| Videos | MP4, MKV, AVI, MOV |
| Music | MP3, WAV, FLAC |
| Archives | ZIP, RAR, 7Z |
| Software | EXE, MSI |
| Others | Diğer dosya türleri |

## ⚙️ Kullanılan Teknolojiler

- **Python:** Uygulamanın temel programlama dili
- **Pathlib:** Dosya ve klasör işlemleri
- **Shutil:** Dosya taşıma işlemleri
- **CSV:** İşlem raporlarının oluşturulması
- **Datetime:** Tarih ve saat bilgilerinin kaydedilmesi

## 🚀 Kurulum ve Kullanım

### Gereksinimler

- Windows işletim sistemi
- Python 3.10 veya üzeri

### 1. Projeyi klonlayın

```bash
git clone https://github.com/Yakup010/Smart-File-Organizer.git
```

### 2. Proje klasörüne girin

```bash
cd Smart-File-Organizer
```

### 3. Uygulamayı çalıştırın

```bash
python main.py
```

### 4. Dosyalarınızı düzenleyin

Uygulama, Downloads klasöründeki dosyaları tarar ve kategorilerine göre taşıma önizlemesi sunar. Kullanıcı onayının ardından dosyalar ilgili klasörlere taşınır.

## 📊 İşlem Raporu

Uygulama, gerçekleştirilen işlemleri `organizer_report.csv` dosyasında saklar.

Raporda bulunan bilgiler:

- Dosya adı
- Dosya kategorisi
- Hedef klasör
- İşlem tarihi
- İşlem durumu
- Hata bilgisi

Oluşturulan CSV raporu Microsoft Excel ile görüntülenebilir.

## 🛡️ Güvenlik

- Dosyalar kullanıcı onayı olmadan taşınmaz.
- Aynı isimli dosyaların üzerine yazılmaz.
- İşlem hataları raporlanır.
- İlk kullanımda örnek dosyalarla test yapılması önerilir.

**Not:** Uygulama dosyaları taşır. Önemli dosyalarınızı düzenlemeden önce yedek almanız önerilir.

## 🔮 Gelecek Geliştirmeler

- [ ] Grafik kullanıcı arayüzü (GUI)
- [ ] Windows için bağımsız EXE uygulaması
- [ ] Geçici ve gereksiz dosya temizliği
- [ ] Depolama alanı analizi
- [ ] Yinelenen dosyaları tespit etme

## 👨‍💻 Geliştirici

**Yakup**

Yazılım geliştirme, Python programlama ve otomasyon alanlarında pratik kazanmak amacıyla geliştirilen kişisel bir projedir.

**Proje:** Smart File Organizer  
**Sürüm:** 1.0  
**Durum:** İlk geliştirme sürümü
