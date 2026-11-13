
from pathlib import Path
import shutil
import csv
from datetime import datetime

# =====================================
# 1. KLASOR YOLLARI
# =====================================

downloads = Path.home() / "Downloads"

documents = Path.home() / "Documents"
pictures = Path.home() / "Pictures"
videos = Path.home() / "Videos"
music = Path.home() / "Music"

rapor_dosyasi = Path(__file__).parent / "organizer_report.csv"


# =====================================
# 2. DOSYA UZANTILARI
# =====================================

resim_uzantilari = [".jpg", ".jpeg", ".png", ".webp"]

belge_uzantilari = [
    ".pdf", ".docx", ".doc", ".txt",
    ".csv", ".xlsx", ".xls"
]

video_uzantilari = [".mp4", ".mkv", ".avi", ".mov"]

muzik_uzantilari = [".mp3", ".wav", ".flac"]

arsiv_uzantilari = [".zip", ".rar", ".7z"]

program_uzantilari = [".exe", ".msi"]


# =====================================
# 3. HEDEF KLASORLER
# =====================================

hedefler = {
    "Images": pictures,
    "Documents": documents,
    "Videos": videos,
    "Music": music,
    "Archives": downloads / "Archives",
    "Software": downloads / "Software",
    "Others": downloads / "Others"
}


# =====================================
# 4. KATEGORI BELIRLEME
# =====================================

def kategori_belirle(dosya):

    uzanti = dosya.suffix.lower()

    if uzanti in resim_uzantilari:
        return "Images"

    elif uzanti in belge_uzantilari:
        return "Documents"

    elif uzanti in video_uzantilari:
        return "Videos"

    elif uzanti in muzik_uzantilari:
        return "Music"

    elif uzanti in arsiv_uzantilari:
        return "Archives"

    elif uzanti in program_uzantilari:
        return "Software"

    else:
        return "Others"


# =====================================
# 5. DOSYA ISMI CAKISMASI KONTROLU
# =====================================

def benzersiz_yol(hedef):

    if not hedef.exists():
        return hedef

    sayac = 1

    while True:

        yeni_isim = (
            hedef.stem
            + f"_{sayac}"
            + hedef.suffix
        )

        yeni_hedef = hedef.with_name(yeni_isim)

        if not yeni_hedef.exists():
            return yeni_hedef

        sayac += 1


# =====================================
# 6. CSV RAPORUNA KAYIT EKLEME
# =====================================

def rapora_kaydet(dosya_adi, kategori, hedef, durum, hata=""):

    alanlar = [
        "Dosya",
        "Kategori",
        "Hedef",
        "Tarih",
        "Durum",
        "Hata"
    ]

    kayit = {
        "Dosya": dosya_adi,
        "Kategori": kategori,
        "Hedef": str(hedef),
        "Tarih": datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
        "Durum": durum,
        "Hata": hata
    }

    dosya_var = rapor_dosyasi.exists()

    with open(
        rapor_dosyasi,
        "a",
        newline="",
        encoding="utf-8-sig"
    ) as dosya:

        yazici = csv.DictWriter(
            dosya,
            fieldnames=alanlar
        )

        if not dosya_var:
            yazici.writeheader()

        yazici.writerow(kayit)


# =====================================
# 7. ANA PROGRAM
# =====================================

def main():

    print("=" * 45)
    print("       SMART FILE ORGANIZER")
    print("=" * 45)

    if not downloads.is_dir():
        print("HATA: Downloads klasoru bulunamadi!")
        return

    print("\nDownloads klasoru bulundu.")

    # Gerekli alt klasorleri olustur
    for kategori in ["Archives", "Software", "Others"]:

        try:

            hedefler[kategori].mkdir(
                parents=True,
                exist_ok=True
            )

        except OSError as hata:

            print(f"{kategori} klasoru olusturulamadi: {hata}")
            return

    # Windows kullanici klasorlerini kontrol et
    for kategori in ["Images", "Documents", "Videos", "Music"]:

        if not hedefler[kategori].is_dir():

            print(
                f"UYARI: {kategori} hedef klasoru bulunamadi: "
                f"{hedefler[kategori]}"
            )

    # Dosyalari analiz et
    tasima_plani = []

    for dosya in downloads.iterdir():

        if not dosya.is_file():
            continue

        kategori = kategori_belirle(dosya)
        hedef_klasor = hedefler[kategori]

        if not hedef_klasor.is_dir():

            print(f"Hedef mevcut degil, atlandi: {dosya.name}")
            continue

        hedef_yol = benzersiz_yol(
            hedef_klasor / dosya.name
        )

        tasima_plani.append(
            (dosya, hedef_yol, kategori)
        )

    # Dosya bulunamadiysa
    if not tasima_plani:

        print("\nTasima yapilacak dosya bulunamadi.")
        return

    # Tasima onizlemesi
    print("\n" + "=" * 45)
    print("TASIMA ONIZLEMESI")
    print("=" * 45)

    for kaynak, hedef, kategori in tasima_plani:

        print(f"\nDosya: {kaynak.name}")
        print(f"Kategori: {kategori}")
        print(f"Hedef: {hedef}")

    print("\nToplam dosya:", len(tasima_plani))

    # Kullanici onayi
    onay = input(
        "\nBu dosyalari tasimak istiyor musunuz? (e/h): "
    ).strip().lower()

    if onay != "e":

        print("\nIslem kullanici tarafindan iptal edildi.")
        return

    # =================================
    # 8. DOSYALARI TASIMA
    # =================================

    tasinan = 0
    hatali = 0
    kategori_sayilari = {}

    print("\nDosyalar tasiniyor...\n")

    for kaynak, hedef, kategori in tasima_plani:

        try:

            # Tasima aninda isim cakismasini tekrar kontrol et
            hedef = benzersiz_yol(hedef)

            shutil.move(
                str(kaynak),
                str(hedef)
            )

            tasinan += 1

            kategori_sayilari[kategori] = (
                kategori_sayilari.get(kategori, 0) + 1
            )

            print(f"TASINDI: {kaynak.name} -> {hedef}")

            # Basarili islemi rapora kaydet
            try:

                rapora_kaydet(
                    kaynak.name,
                    kategori,
                    hedef,
                    "Basarili"
                )

            except OSError as rapor_hatasi:

                print("Rapor kaydedilemedi:", rapor_hatasi)

        except OSError as hata:

            hatali += 1

            print(f"HATA: {kaynak.name} -> {hata}")

            # Hatali islemi rapora kaydet
            try:

                rapora_kaydet(
                    kaynak.name,
                    kategori,
                    hedef,
                    "Basarisiz",
                    str(hata)
                )

            except OSError as rapor_hatasi:

                print("Hata raporu kaydedilemedi:", rapor_hatasi)

    # =================================
    # 9. ISLEM RAPORU
    # =================================

    print("\n" + "=" * 45)
    print("          ISLEM RAPORU")
    print("=" * 45)

    print("Basariyla tasinan:", tasinan)
    print("Hatali islemler:", hatali)

    print("\nKategori dagilimi:")

    for kategori, adet in kategori_sayilari.items():

        print(f"{kategori}: {adet} dosya")

    print("\nCSV rapor konumu:")
    print(rapor_dosyasi)

    print("\nDosya duzenleme islemi tamamlandi!")


# =====================================
# 10. PROGRAMI BASLAT
# =====================================

if __name__ == "__main__":
    main()
