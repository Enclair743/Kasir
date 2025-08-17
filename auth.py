import streamlit as st
from auth import authenticate
from gsheet_service import get_records, append_row

st.set_page_config(page_title="Aplikasi Toko", layout="wide")

st.title("Aplikasi Toko Streamlit + Google Sheets")

# Login
if "user" not in st.session_state:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user = authenticate(username, password)
        if user:
            st.session_state.user = user
            st.success(f"Selamat datang, {user['nama_lengkap']}! ({user['role']})")
        else:
            st.error("Username atau password salah!")
    st.stop()

user = st.session_state.user

# Dashboard
st.sidebar.title("Menu")
role = user["role"].lower()

if role == "admin":
    menu = st.sidebar.radio("Admin Menu", ["Akun", "Barang", "Transaksi", "Barang Dihapus"])
    if menu == "Akun":
        st.header("Manajemen Akun")
        akun = get_records("akun")
        st.table(akun)
        # Tambah/Edit/Hapus Akun (implementasi lanjutan)
    elif menu == "Barang":
        st.header("Manajemen Barang")
        barang = get_records("barang")
        st.table(barang)
        # Tambah/Edit/Hapus Barang (implementasi lanjutan)
    elif menu == "Transaksi":
        st.header("Riwayat Transaksi")
        transaksi = get_records("transaksi")
        st.table(transaksi)
    elif menu == "Barang Dihapus":
        st.header("Log Barang Dihapus")
        barang_dihapus = get_records("barang_dihapus")
        st.table(barang_dihapus)
elif role == "kasir":
    menu = st.sidebar.radio("Kasir Menu", ["Transaksi", "Stok Barang"])
    if menu == "Transaksi":
        st.header("Input Transaksi")
        # Form input transaksi barang, update sheet 'transaksi' dan 'barang'
        st.write("Form transaksi (implementasi lanjutan)")
    elif menu == "Stok Barang":
        st.header("Lihat Stok Barang")
        barang = get_records("barang")
        st.table(barang)
else:
    st.error("Role tidak dikenali!")

st.sidebar.button("Logout", on_click=lambda: st.session_state.pop("user"))
