#!/usr/bin/env python3
"""Dolmus koltuk paylasim protokolu.

Calisan bir durusma motoru. Ag yok, veritabani yok, sadece iddia ve koltuk.
"""

from __future__ import annotations

import argparse
import hashlib
from dataclasses import dataclass


@dataclass
class Yolcu:
    ad: str
    yasli_veya_cocuklu: bool = False
    agir_canta: bool = False
    kapida_once: bool = False
    inecegim_diye_yalan: bool = False
    kulaklikli: bool = False
    sofore_abi: bool = False

    def puan(self) -> int:
        toplam = 10
        if self.yasli_veya_cocuklu:
            toplam += 40
        if self.agir_canta:
            toplam += 15
        if self.kapida_once:
            toplam += 12
        if self.inecegim_diye_yalan:
            toplam -= 25
        if self.kulaklikli:
            toplam -= 8
        if self.sofore_abi:
            toplam += 3
        return toplam


def demo_yolcular() -> list[Yolcu]:
    return [
        Yolcu("Teyze Necla", yasli_veya_cocuklu=True, sofore_abi=True),
        Yolcu("Stajyer Kerem", agir_canta=True, kapida_once=True),
        Yolcu("Kulaklikli Ege", kulaklikli=True, kapida_once=True),
        Yolcu("Inmiyorum Abi", inecegim_diye_yalan=True, sofore_abi=True),
        Yolcu("Sessiz Deniz"),
    ]


def koltuk_dagit(yolcular: list[Yolcu], koltuk: int) -> tuple[list[Yolcu], list[Yolcu]]:
    sirali = sorted(yolcular, key=lambda y: (-y.puan(), y.ad))
    return sirali[:koltuk], sirali[koltuk:]


def tutanak_no(yolcular: list[Yolcu]) -> str:
    ham = "|".join(f"{y.ad}:{y.puan()}" for y in yolcular)
    return hashlib.sha256(ham.encode("utf-8")).hexdigest()[:10]


def durusma(yolcular: list[Yolcu], koltuk: int = 3) -> str:
    oturan, ayakta = koltuk_dagit(yolcular, koltuk)
    satirlar = [
        "DOLMUS KOLTUK PAYLASIM TUTANAGI",
        f"tutanak: {tutanak_no(yolcular)}",
        f"koltuk sayisi: {koltuk}",
        "",
        "OTURANLAR",
    ]
    for i, y in enumerate(oturan, 1):
        satirlar.append(f"  {i}. {y.ad} (puan {y.puan()})")
    satirlar.append("")
    satirlar.append("AYAKTA KALANLAR")
    if not ayakta:
        satirlar.append("  kimse. mucize.")
    for y in ayakta:
        satirlar.append(f"  - {y.ad} (puan {y.puan()}) resmi uzuntu aldi")
    satirlar.append("")
    satirlar.append("hukum: koltuk puana gore dagitildi. itiraz bir sonraki durakta.")
    return "\n".join(satirlar)


def self_test() -> None:
    yolcular = demo_yolcular()
    oturan, ayakta = koltuk_dagit(yolcular, 3)
    assert oturan[0].ad == "Teyze Necla"
    assert any(y.ad == "Inmiyorum Abi" for y in ayakta)
    assert "tutanak:" in durusma(yolcular)


def main() -> None:
    parser = argparse.ArgumentParser(description="Dolmus koltuk protokolu")
    parser.add_argument("--demo", action="store_true", help="ornek durusmayi bas")
    parser.add_argument("--koltuk", type=int, default=3)
    args = parser.parse_args()
    self_test()
    if args.demo or True:
        print(durusma(demo_yolcular(), args.koltuk))
        print()
        print("DAMGA: 05 Ekim 2026 | Kayyum Grok | Tentivory")
        print("Muhur ciddidir. Muhuru basan kisi degildir.")


if __name__ == "__main__":
    main()
