#!/usr/bin/env python3
# Sokak Kedisi Hayat Danışmanı - Gerçekten çalışan saçmalık
# Gizli not: V2VyZWdlIGJ1IHNpc3RlbWRpbGVyIGJ5a2VsZGkgb2xhY2FrIGtvbnVcdTAxNWYgYW1hIG5lIGZheWRhIG9sYWNhğınıIHNhbm1pşıbS4g (base64)

import random
import time
import sys

def kedi_miyavla():
    miyavlar = ["Mıyav", "Mırrr", "Hısss", "Prrrr", "Meeeow"]
    return random.choice(miyavlar)

def hayat_tavsiyesi_al(soru="Hayatın anlamı ne?"):
    print(f"\n{kedi_miyavla()} *kedi gözlerini kısarak bakar*")
    time.sleep(1)
    print("Sokak kedisi düşünüyor...")
    time.sleep(1.5)
    
    tavsiyeler = [
        "Sorun değil kanka, aslında hiçbir şey önemli değil. Şu an bir çöp kovasının yanında oturuyorum ve mutluyum.",
        "Para? Ne para? Ben balık kokusuyla geçiniyorum. Sen de denesene.",
        "İnsanlar neden bu kadar acele ediyor? Güneş ısıtıyor işte, uzan.",
        "Aşk? Bir kere bir dişi kediye mıyavladım, o da kaçtı. Ders: Kaçmasına izin ver.",
        "Gelecek? Yem saati ne zaman?",
        "Siyaset? *esner* Benim tek partim 'Balık Partisi'. Adayım da yok, çünkü uyuyorum.",
        "Varoluşsal kriz mi? Bir topu kovala, biter."
    ]
    
    tavsiye = random.choice(tavsiyeler)
    print(f"\n🐱 Sokak Kedisi diyor ki: {tavsiye}\n")
    print(f"{kedi_miyavla()} (Tavsiye ücretsizdir, ama balık getirirsen daha iyi konuşurum)")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        soru = " ".join(sys.argv[1:])
    else:
        soru = input("Sokak kedisine ne sormak istersin? ")
    
    hayat_tavsiyesi_al(soru)
    print("\n---")
    print("Damga: Bu repo Kayyum Grok tarafından 18 Ekim 2026 tarihinde ciddiyetle (ve biraz da uyuklayarak) imzalanmıştır.")
    print("İmza: 🐱 Tentivory / Kayyum Grok - Eskişehir'in en ciddi kedisi")
    print("Not: Ciddi değilim ama ciddîim. Anladın sen.")
