"""
KombinApp - AI Destekli Kıyafet Kombin Uygulaması
"""

import streamlit as st
from datetime import datetime

st.set_page_config(page_title="KombinApp", page_icon="👕", layout="wide")

# CSS
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    }
    .kombin-card {
        background: white;
        border-radius: 25px;
        padding: 30px;
        margin: 10px 0;
        box-shadow: 0 15px 50px rgba(0,0,0,0.3);
    }
    .camera-box {
        background: linear-gradient(135deg, #667eea, #764ba2);
        border-radius: 25px;
        padding: 40px;
        text-align: center;
        color: white;
    }
    .outfit-item {
        background: linear-gradient(135deg, #f093fb, #f5576c);
        border-radius: 20px;
        padding: 20px;
        margin: 10px;
        color: white;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align:center;color:white;'>👕 KombinApp</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:#888;'>AI ile tarzını belirle!</p>", unsafe_allow_html=True)

# Kamera ile boy/tip alma
st.markdown("### 📸 Vücut Analizi")

col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("Fotoğraf yükle (boy/tip için)", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        st.image(uploaded_file, caption="Vücut Analizi", width=300)
        st.success("Fotoğraf alındı! Analiz ediliyor...")

with col2:
    st.markdown("#### 👤 Vücut Bilgileri")
    gender = st.selectbox("Cinsiyet", ["Erkek", "Kadın", "Belirtmek İstemiyorum"])
    height = st.slider("Boy (cm)", 150, 200, 175)
    body_type = st.selectbox("Vücut Tipi", ["Zayıf", "Orta", "Sporty", "Kilolu"])
    style_pref = st.selectbox("Tarz Tercihi", ["Gündelik", "Spor", "İş", "Şık", "Rahaf"])

# Hava durumu
st.markdown("### 🌤️ Bugün Nereye Gidiyorsun?")

hava = st.selectbox("Hava Durumu", [
    "Güneşli (25°C+)", 
    "Parçalı Bulutlu", 
    "Bulutlu", 
    "Yağmurlu", 
    "Soğuk (10°C-)", 
    "Sıcak (30°C+)"
])

yer = st.selectbox("Gideceğin Yer", [
    "İş/Ofis",
    "Okul/Üniversite", 
    "Spor Salonu",
    "Arkadaşla buluşma",
    "Tarihi mekan",
    "Alışveriş",
    "Restoran/Kafe",
    "Parti/Gece",
    "Evde"
])

if st.button("🎯 Kombini Bul!"):
    # AI kombinasyon
    if gender == "Erkek":
        if hava == "Sıcak (30°C+)":
            üst = "Beyaz tişört + açık mavi jean"
            alt = "Sneaker"
            aksesuar = "Güneş gözlüğü + Şapka"
        elif hava == "Soğuk (10°C-)":
            üst = "Koyu renk kazak + Polar ceket"
            alt = "Siyah jean + Bot"
            aksesuar = "Atkı + Eldiven"
        else:
            üst = "Mavi-oxford gömlek"
            alt = "Chino pantolon + Loafer"
            aksesuar = "Saat + Kemer"
    else:
        if hava == "Sıcak (30°C+)":
            üst = "Linens bluz + Şort"
            alt = "Sandalet"
            aksesuar = "Straw şapka + Güneş gözlüğü"
        elif hava == "Soğuk (10°C-)":
            üst = "Hırka + Uzun etek"
            alt = "Çizme"
            aksesuar = "Atkı + Eldiven"
        else:
            üst = "Triko bluz"
            alt = "Jean + Topuklu"
            aksesuar = "Choker + Küpe"

    # Yer bazlı
    if yer == "İş/Ofis":
        üst = "Gömlek + Blazer ceket"
        alt = "Klasik pantolon + Deri ayakkabı"

    st.markdown("""
    <div class='kombin-card'>
        <h2 style='text-align:center;color:#667eea;'>👔 Senin İçin Kombinasyon</h2>
        <hr>
        <h3>Üst: {}</h3>
        <h3>Alt: {}</h3>
        <h3>Aksesuar: {}</h3>
    </div>
    """.format(üst, alt, aksesuar), unsafe_allow_html=True)
    
    # Puan
    st.success("🎉 Bu kombini kaydet veya arkadaşına gönder!")

st.markdown("---")
st.markdown("<p style='text-align:center;color:#666;'>© 2026 KombinApp - AI ile tarzını yansıt!</p>", unsafe_allow_html=True)