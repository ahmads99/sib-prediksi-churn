import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Memuat model yang telah dilatih
model = pickle.load(open('model/logreg_model.pkl', 'rb'))

# Judul aplikasi
st.set_page_config(page_title="Prediksi Customer Churn", layout="centered")
st.title("📈 Dashboard Prediksi Customer Churn")
st.markdown("Gunakan data transaksi pelanggan untuk memprediksi kemungkinan mereka churn (berhenti berlangganan).")

# Sidebar untuk input
st.sidebar.title("📥 Masukkan Data Pelanggan")

# Nama Customer dengan placeholder
nama = st.sidebar.text_input("🧑 Nama Pelanggan", placeholder="Masukkan nama pelanggan")

# Customer ID dengan placeholder
id_cust = st.sidebar.text_input("🆔 ID Pelanggan", placeholder="Masukkan ID pelanggan")

# Jenis Kelamin dengan pilihan
gender = st.sidebar.selectbox("👤 Jenis Kelamin", ['Laki-laki', 'Perempuan'])

# Rata-rata Transaksi dengan placeholder dan nilai default
avg_amt = st.sidebar.number_input("💵 Rata-rata Jumlah Transaksi", min_value=0, 
                                  placeholder="Masukkan rata-rata transaksi")

# Jumlah Transaksi dengan placeholder dan nilai default
cnt_trans = st.sidebar.number_input("🔁 Jumlah Transaksi", min_value=0, 
                                    placeholder="Masukkan jumlah transaksi")

# Perbedaan Tahun dengan placeholder dan nilai default
year_diff = st.sidebar.number_input("📅 Lama berlangganan Tahun", min_value=0,
                                    placeholder="Masukkan perbedaan tahun")

# Catatan dengan placeholder
catatan = st.sidebar.text_area("📝 Catatan Tambahan",
                               placeholder="Masukkan catatan tambahan")

# Prediksi jika tombol ditekan
if st.sidebar.button("🔍 Prediksi Sekarang"):
    input_array = np.array([[avg_amt, cnt_trans, year_diff]])
    prediction = model.predict(input_array)[0]
    prob = model.predict_proba(input_array)[0][1]

    st.markdown(f"## 🔎 Hasil Prediksi untuk **{nama}** (ID: `{id_cust}`)")
    if prediction == 1:
        st.error(f"❌ Pelanggan diprediksi **CHURN** dengan probabilitas **{prob*100:.2f}%**.")
    else:
        st.success(f"✅ Pelanggan diprediksi **TIDAK CHURN** dengan probabilitas **{(1-prob)*100:.2f}%**.")

    # Visualisasi
    fig, ax = plt.subplots(figsize=(6, 3))
    sns.barplot(x=['Tidak Churn', 'Churn'], y=[1-prob, prob], palette='Blues')
    ax.set_title('📊 Probabilitas Prediksi')
    ax.set_ylabel('Probabilitas')
    ax.set_ylim(0, 1)
    st.pyplot(fig)

    # Menampilkan tabel detail input
    st.markdown("---")
    st.subheader("🧾 Rangkuman Input")
    df_input = pd.DataFrame({
        'Nama Pelanggan': [nama],
        'ID Pelanggan': [id_cust],
        'Jenis Kelamin': [gender],
        'Rata-rata Jumlah Transaksi': [avg_amt],
        'Jumlah Transaksi': [cnt_trans],
        'Lama berlangganan Tahun': [year_diff],
        'Catatan': [catatan],
        'Prediksi': ['Churn' if prediction == 1 else 'Tidak Churn'],
        'Probabilitas Churn (%)': [f"{prob*100:.2f}%"],
        'Waktu Prediksi': [datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
    })
    st.dataframe(df_input)

    # Opsi untuk download hasil prediksi
    csv = df_input.to_csv(index=False).encode('utf-8')
    st.download_button("⬇️ Unduh Hasil Prediksi", csv, file_name="hasil_prediksi_churn.csv", mime='text/csv')

    st.markdown("---")
    st.info("💡 Rekomendasi: Jika pelanggan churn, pertimbangkan menawarkan diskon atau program loyalitas.")
