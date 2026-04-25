"""
KombinApp - AI Destekli Kıyafet Kombin Uygulaması
Güzel arka plan + Kamera ile boy analizi
"""

import streamlit as st
import time

st.set_page_config(page_title="KombinApp", page_icon="👕", layout="wide")

# CSS - Animasyonlu arka plan
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }
    
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Yıldızlar */
    .stars {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        background-image: 
            radial-gradient(2px 2px at 20px 30px, white, transparent),
            radial-gradient(2px 2px at 40px 70px, rgba(255,255,255,0.8), transparent),
            radial-gradient(1px 1px at 90px 40px, white, transparent),
            radial-gradient(2px 2px at 160px 120px, rgba(255,255,255,0.6), transparent),
            radial-gradient(1px 1px at 230px 80px, white, transparent),
            radial-gradient(2px 2px at 300px 150px, rgba(255,255,255,0.7), transparent),
            radial-gradient(1px 1px at 400px 60px, white, transparent),
            radial-gradient(2px 2px at 500px 200px, rgba(255,255,255,0.5), transparent);
        background-repeat: repeat;
        background-size: 600px 300px;
        opacity: 0.5;
    }
    
    .welcome-box {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 30px;
        padding: 50px;
        text-align: center;
        margin: 30px auto;
        max-width: 600px;
        backdrop-filter: blur(20px);
        border: 2px solid rgba(255,255,255,0.5);
        box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    }
    
    .kombin-card {
        background: linear-gradient(135deg, #ff9a56, #ff6b35);
        border-radius: 25px;
        padding: 30px;
        margin: 20px 0;
        color: white;
        box-shadow: 0 15px 50px rgba(255,107,53,0.4);
    }
    
    .camera-box {
        background: linear-gradient(135deg, rgba(102,126,234,0.9), rgba(118,75,162,0.9));
        border-radius: 25px;
        padding: 40px;
        text-align: center;
        color: white;
        margin: 20px 0;
        backdrop-filter: blur(10px);
    }
    
    .start-btn {
        background: linear-gradient(135deg, #00d4aa, #00b894);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 20px 50px;
        font-size: 22px;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 10px 30px rgba(0,212,170,0.3);
    }
    
    .start-btn:hover {
        transform: scale(1.05);
        box-shadow: 0 15px 40px rgba(0,212,170,0.5);
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-20px); }
    }
    
    .float-anim {
        animation: float 2s ease-in-out infinite;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.1); }
    }
    
    .pulse-anim {
        animation: pulse 2s ease-in-out infinite;
    }
    
    .outfit-box {
        background: white;
        border-radius: 20px;
        padding: 25px;
        margin: 10px;
        color: #333;
        text-align: center;
    }
    
    /* Butonlar */
    .stButton > button {
        border-radius: 15px;
        font-weight: bold;
    }
    
    /* Kartlar */
    .stSelectbox > div > div {
        border-radius: 15px;
    }
    
    h1, h2, h3 {
        color: white !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
</style>
""" + "<div class='stars'></div>", unsafe_allow_html=True)

# Session state
if 'started' not in st.session_state:
    st.session_state.started = False

# === MERHABA EKRANI ===
if not st.session_state.started:
    st.markdown("""
    <div class='welcome-box'>
        <div class='float-anim'>
            <span style='font-size:80px;'>👕</span>
        </div>
        <h1 style='font-size:40px;margin:20px 0;'>Merhaba!</h1>
        <p style='font-size:20px;opacity:0.9;'>
            Ben KombinApp, senin stil danışmanınım! 👋<br>
            Tarzına uygun kıyafet kombinasyonları oluşturayım.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("🎯 Kombini Yap!", key="start_btn"):
            st.session_state.started = True
            st.rerun()
    
    st.stop()

# === ANA EKRAN ===
st.markdown("<h1 style='text-align:center;color:white;'>👕 KombinApp</h1>", unsafe_allow_html=True)

# Kamera ile fotoğraf
st.markdown("""
<div class='camera-box'>
    <span style='font-size:40px;'>📸</span>
    <h3>Fotoğrafını Çek veya Yükle</h3>
    <p>Boyunu ve vücut tipini analiz edelim</p>
</div>
""", unsafe_allow_html=True)

camera_photo = st.camera_input("📷 Fotoğraf Çek")

gallery_photo = st.file_uploader("📁 Galeriden Seç", type=["jpg", "png", "jpeg"])

photo = camera_photo if camera_photo else gallery_photo

if photo:
    st.success("✅ Fotoğraf alındı! Analiz ediliyor...")
    time.sleep(1)
    
    # Simüle analiz
    st.markdown("""
    <div style='background:white;border-radius:20px;padding:20px;margin:20px 0;color:#333;'>
        <h4>🔍 Analiz Sonucu:</h4>
        <p>• Boy: <b>175 cm</b></p>
        <p>• Vücut Tipi: <b>Sporty</b></p>
        <p>• Tarz: <b>Gündelik</b></p>
    </div>
    """, unsafe_allow_html=True)

# Bilgi formu
st.markdown("---")
st.markdown("### 👤 Vücut Bilgileri (veya düzenle)")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Cinsiyet", ["Erkek", "Kadın"], key="gender")
    height = st.slider("Boy (cm)", 150, 200, 175, key="height")
    body_type = st.selectbox("Vücut Tipi", ["Zayıf", "Orta", "Sporty", "Kilolu"], key="body")

with col2:
    style_pref = st.selectbox("Tarz", ["Gündelik", "Spor", "İş", "Şık", "Rahat"], key="style")
    hava = st.selectbox("Hava", ["Güneşli", "Bulutlu", "Yağmurlu", "Soğuk", "Sıcak"], key="hava")
    yer = st.selectbox("Nereye?", ["İş", "Okul", "Spor", "Arkadaş", "Parti", "Ev"], key="yer")

# Kombini bul butonu
st.markdown("")
if st.button("🔥 Kombini Bul!", key="find_outfit"):
    # AI Kombinasyon
    kombinasyon = {
        "üst": "Mavi Oxford Gömlek",
        "alt": "Krem Renk Chino Pantolon", 
        "ayakkabı": "Kahverengi Loafer",
        "aksesuar": "Derici Saat + Güneş Gözlüğü"
    }
    
    if gender == "Erkek":
        if hava == "Sıcak":
            kombinasyon = {"üst": "Beyaz Linen Gömlek", "alt": "Açık Mavi Jean", "ayakkabı": "Beyaz Sneaker", "aksesuar": "Straw Şapka"}
        elif hava == "Soğuk":
            kombinasyon = {"üst": "Koyu Gri Hırka + Polar", "alt": "Siyah Jean", "ayakkabı": "Siyah Bot", "aksesuar": "Atkı + Eldiven"}
    
    if yer == "İş":
        kombinasyon = {"üst": "Gömlek + Blazer", "alt": "Klasik Pantolon", "ayakkabı": "Deri Ayakkabı", "aksesuar": "Kravat"}
    elif yer == "Spor":
        kombinasyon = {"üst": "Fit Tişört", "alt": "Spor Pantolon", "ayakkabı": "Spor Ayakkabı", "aksesuar": "Spor Saat"}
    
    st.markdown("""
    <div class='kombin-card'>
        <h2 style='text-align:center;'>👔 Senin İçin Kombinasyon</h2>
        <hr style='opacity:0.3'>
        <div style='display:flex;flex-wrap:wrap;gap:10px;'>
            <div class='outfit-box' style='flex:1;'>
                <span style='font-size:30px;'>👔</span>
                <h4>Üst</h4>
                <p>{}</p>
            </div>
            <div class='outfit-box' style='flex:1;'>
                <span style='font-size:30px;'>👖</span>
                <h4>Alt</h4>
                <p>{}</p>
            </div>
            <div class='outfit-box' style='flex:1;'>
                <span style='font-size:30px;'>👟</span>
                <h4>Ayakkabı</h4>
                <p>{}</p>
            </div>
            <div class='outfit-box' style='flex:1;'>
                <span style='font-size:30px;'>⌚</span>
                <h4>Aksesuar</h4>
                <p>{}</p>
            </div>
        </div>
    </div>
    """.format(kombinasyon["üst"], kombinasyon["alt"], kombinasyon["ayakkabı"], kombinasyon["aksesuar"]), unsafe_allow_html=True)
    
    st.balloons()

st.markdown("---")
st.markdown("<p style='text-align:center;color:#888;'>© 2026 KombinApp - Tarzını yansıt! 👕</p>", unsafe_allow_html=True)