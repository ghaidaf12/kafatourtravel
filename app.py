import streamlit as st
from datetime import date

# ===== PAGE CONFIG (WAJIB PALING ATAS) =====
st.set_page_config(page_title="Camp Riverside", layout="wide")

# ===== HIDE DEFAULT STREAMLIT MENU, HEADER, FOOTER =====
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ===== Sidebar =====
st.sidebar.image("https://i.ibb.co/PMKFFc9/camp-logo.png", width=150)
st.sidebar.title("Camp Riverside")
st.sidebar.markdown("""
📍 Kadudampit, Sukabumi, Jawa Barat  
📞 [WhatsApp](https://wa.me/62812xxxxxxx)  
📸 [Instagram](https://instagram.com/kafatourtravel)
""")

menu = st.sidebar.radio("Navigasi", [
    "🏡 Beranda", "🧭 Tentang Kami", "🏕️ Aktivitas", "🖼️ Galeri", 
    "📋 Paket & Harga", "📝 Booking", "📌 Lokasi"
])

# ===== Layout Main Page =====
if menu == "🏡 Beranda":
    st.markdown("""
    <div style='background-color:#e8f5e9; padding:40px 20px; border-radius:12px;'>
        <h1 style='text-align:center; color:#2e7d32;'>🌲 Selamat Datang di <b>Kafa Tour Travel</b></h1>
        <p style='text-align:center; font-size:18px;'>Nikmati pengalaman camping dan susur sungai terbaik di kaki Gunung Salak</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""<br><h4 style='text-align:center;'>Highlight Kegiatan</h4>""", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://i.ibb.co/9YHqWhh/camp1.jpg", caption="Area Tenda", use_container_width=True)
    with col2:
        st.image("https://i.ibb.co/WPgsZ7K/river1.jpg", caption="Susur Sungai", use_container_width=True)
    with col3:
        st.image("https://i.ibb.co/Kr03K4j/outbound.jpg", caption="Outbound", use_container_width=True)

elif menu == "🧭 Tentang Kami":
    st.header("Tentang Camp Riverside")
    st.write("""
    Camp Riverside adalah destinasi wisata alam yang menawarkan pengalaman berkemah, susur sungai, outbound,
    edukasi alam, dan kegiatan outdoor lainnya. Dikelola secara profesional dengan tetap mempertahankan nuansa alami.
    """)
    st.image("https://i.ibb.co/zVPdytJ/about-camp.jpg", width=600)

elif menu == "🏕️ Aktivitas":
    st.header("Aktivitas Unggulan")
    cols = st.columns(3)
    aktivitas = [
        ("Camping Ground", "https://i.ibb.co/9YHqWhh/camp1.jpg"),
        ("Susur Sungai", "https://i.ibb.co/WPgsZ7K/river1.jpg"),
        ("Outbound Anak & Dewasa", "https://i.ibb.co/Kr03K4j/outbound.jpg")
    ]
    for i, (nama, gambar) in enumerate(aktivitas):
        with cols[i]:
            st.image(gambar, use_container_width=True)
            st.markdown(f"### {nama}")

elif menu == "🖼️ Galeri":
    st.header("Galeri Dokumentasi")
    st.image([
        "https://i.ibb.co/9YHqWhh/camp1.jpg",
        "https://i.ibb.co/pjzjM0s/camp2.jpg",
        "https://i.ibb.co/WPgsZ7K/river1.jpg",
        "https://i.ibb.co/zVPdytJ/about-camp.jpg"
    ], width=300, caption=["Area Tenda", "Tepi Sungai", "Susur Sungai", "Suasana Alam"], use_container_width=False)

elif menu == "📋 Paket & Harga":
    st.header("Daftar Paket dan Harga")
    st.markdown("""
    | Paket                  | Harga / Orang |
    |------------------------|---------------|
    | Camping + Makan 3x     | Rp 150.000    |
    | Susur Sungai           | Rp 100.000    |
    | Outbound Anak          | Rp 75.000     |
    | Outbound Dewasa        | Rp 95.000     |
    """)

elif menu == "📝 Booking":
    st.header("Formulir Booking")
    with st.form("form_booking"):
        nama = st.text_input("Nama Lengkap")
        tanggal = st.date_input("Tanggal Booking", value=date.today())
        jumlah = st.number_input("Jumlah Orang", min_value=1)
        kontak = st.text_input("Nomor WhatsApp")
        submit = st.form_submit_button("Kirim")
        if submit:
            st.success(f"Terima kasih {nama}, booking kamu untuk {jumlah} orang pada tanggal {tanggal} telah dicatat.")

elif menu == "📌 Lokasi":
    st.header("Lokasi Lembah Uyut")

# Alamat dengan link aktif
st.markdown("""
📍 **Alamat:** Cinumpang, Sukamaju, Kecamatan Kadudampit, Kabupaten Sukabumi, Jawa Barat  
🌐 <a href="https://maps.app.goo.gl/FgTYYGHrmkKitxAJ7" target="_blank">🔗 Lihat di Google Maps</a>
""", unsafe_allow_html=True)

# Peta interaktif Google Maps (iframe embed)
st.components.v1.iframe(
    "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d31748.213705630525!2d106.92440408890623!3d-6.859735874193036!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e683d259d3e6d05%3A0x88c86f7991d06b62!2sCinumpang%2C%20Kecamatan%20Kadudampit%2C%20Sukabumi%2C%20Jawa%20Barat!5e0!3m2!1sid!2sid!4v1718271758296!5m2!1sid!2sid",
    width=700,
    height=450
)

