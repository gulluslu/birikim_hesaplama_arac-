
import streamlit as st

st.title("EV HESAPLAMA ARACI")

baslangic_yas = 25
nihai_yas = 65

her_ay_biriken = st.number_input("Her ay biriken para:", value=3000)
ev_fiyat = st.number_input("Ev fiyatı:", value=1250000)
ilk_odeme_oran = st.number_input("İlk ödeme oranı:", value=0.20)
aylik_kira = st.number_input("Aylık kira geliri:", value=8000)
kredi_yil = st.number_input("Kredi süresi (yıl):", value=15)


toplam_ay = (nihai_yas - baslangic_yas) * 12
ilk_odeme_miktar = ev_fiyat * ilk_odeme_oran

kredi_suresi_ay = kredi_yil * 12
kredi_miktar = ev_fiyat - ilk_odeme_miktar
aylik_taksit = kredi_miktar / kredi_suresi_ay

kalan_para = 0.0
ev_sayisi = 0
krediler = []
yillik_bilgi = []


for ay in range(1, toplam_ay + 1):

    kalan_para = kalan_para + her_ay_biriken
    kalan_para = kalan_para + (ev_sayisi * aylik_kira)

    kredi_sayisi = len(krediler)
    toplam_odeme = kredi_sayisi * aylik_taksit
    kalan_para = kalan_para - toplam_odeme

    kredi_kalan_aylar = []
    for kalan in krediler:
        kalan = kalan - 1
        if kalan > 0:
            kredi_kalan_aylar.append(kalan)
    krediler = kredi_kalan_aylar

    if kalan_para >= ilk_odeme_miktar:
        kalan_para = kalan_para - ilk_odeme_miktar
        ev_sayisi = ev_sayisi + 1
        krediler.append(kredi_suresi_ay)

    if ay % 12 == 0:
        yas = baslangic_yas + (ay // 12)
        aylik_toplam_kira = ev_sayisi * aylik_kira
        yillik_bilgi.append((yas, ev_sayisi, aylik_toplam_kira, int(kalan_para)))


st.write("### Yıllık Durum:")
for x in yillik_bilgi:
    st.write(x[0], "yaşında:",
             "Ev:", x[1],
             "Kira:", x[2],
             "Biriken para:", x[3])

