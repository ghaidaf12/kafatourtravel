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
📍 Desa Sukarasa, Bogor, Jawa Barat  
📞 [WhatsApp](https://wa.me/62812xxxxxxx)  
📸 [Instagram](https://instagram.com/camp.riverside)
""")

menu = st.sidebar.radio("Navigasi", [
    "🏡 Beranda", "🧭 Tentang Kami", "🏕️ Aktivitas", "🖼️ Galeri", 
    "📋 Paket & Harga", "📝 Booking", "📌 Lokasi"
])

# ===== Layout Main Page =====
if menu == "🏡 Beranda":
    st.markdown("""
    <div style='background-color:#e8f5e9; padding:40px 20px; border-radius:12px;'>
        <h1 style='text-align:center; color:#2e7d32;'>🌲 Selamat Datang di <b>Camp Riverside</b></h1>
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
    st.header("Lokasi Camp Riverside")
    st.markdown("""
    📍 Alamat: Desa Sukarasa, Kecamatan Pamijahan, Kabupaten Bogor, Jawa Barat  
    🌐 [Lihat di Google Maps](https://goo.gl/maps/xxxxxxxx)
    """)
    st.image("https://i.ibb.co/zGPdh1z/maps-preview.jpg", caption="Peta Lokasi Camp Riverside", width=700)
