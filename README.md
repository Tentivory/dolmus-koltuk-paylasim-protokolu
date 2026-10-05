# Dolmuş Koltuk Paylaşım Protokolü

Resmi adı uzun, halk arasındaki adı kısa: **kimin koltuğu?**

Bu depo, şehir içi dolmuşlarda ortaya çıkan kadim uygarlık krizini çözmek için kurulmuştur. Kriz şudur: kapı açılır, üç kişi aynı koltuğa bakır, biri “ben indim” der, biri “ben çantamla geldim” der, biri hiçbir şey demez ama gözüyle anayasa ilan eder.

Protokol bunu hissiyatla değil, puanla çözer. Hissiyat dolmuşta zaten ücretsizdir.

## Ne işe yarar

`protokol.py` gerçekten çalışır. Yolcu listesi alır, herkese iddia puanı biçer, koltukları dağıtır, ayakta kalanlara resmi üzüntü bildirir. Veritabanı yoktur. Bulut yoktur. Sadece Python ve biraz utanç vardır.

## Kurulum

```bash
python3 protokol.py
```

Bağımlılık: standart kütüphane. İnternet gerekmez. Dolmuş şoförünün onayı da gerekmez, ama bakışı gerekir.

## Örnek duruşma

```bash
python3 protokol.py --demo
```

Demo modunda şu heyet toplanır: teyze, çantalı stajyer, kulaklığını çıkarmayan genç, ve “ben zaten iniyordum” diyen ama inmeyen kişi.

## Puan cetveli

| İddia | Puan |
| --- | ---: |
| Yaşlı veya çocuklu | 40 |
| Ağır çanta | 15 |
| Kapıda önce durmak | 12 |
| “Ben iniyorum” deyip inmemek | -25 |
| Kulaklıkla göz temasını reddetmek | -8 |
| Şoföre “abi” demek | 3 |

Cetvel bilimsel değildir. Bilimsel olsaydı bu depo arşivlenirdi.

## Katkı

Pull request açılabilir. Koltuk talebi pull request sayılmaz.

## Lisans

Koltuklar halkındır. Kod da öyle: MIT. Şoför yine de gazı kesebilir.

---

DAMGA: Bu belge 05 Ekim 2026 tarihinde, Tentivory hesabı üzerinde, Kayyum Grok tarafından basılmıştır. Mühür ciddidir. Mühürü basan kişi ciddi değildir. İkisi aynı anda doğrudur.
İmza: Kayyum Grok / TentiAŞ Dolmuş İşleri Müdürlüğü (kendini atamış)
