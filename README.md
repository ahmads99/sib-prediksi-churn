# Data Analyst Project: Business Decision Research

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis data pelanggan dan memprediksi kemungkinan **churn** (pelanggan yang berhenti berlangganan) menggunakan teknik data science dan machine learning. Data yang digunakan berisi informasi tentang pelanggan seperti **gender**, **tenure**, **service** yang digunakan, dan **monthly charges**.

## Tujuan
- Menganalisis faktor-faktor yang mempengaruhi churn pelanggan.
- Menerapkan teknik machine learning untuk memprediksi churn.
- Membantu perusahaan dalam pengambilan keputusan bisnis terkait **customer retention**.

## Langkah-langkah Proyek
1. **Pembersihan Data**: Membersihkan data dari nilai yang hilang dan mengubah kolom-kolom tertentu.
2. **Exploratory Data Analysis (EDA)**: Melakukan analisis eksplorasi untuk melihat distribusi data dan hubungan antar fitur.
3. **Feature Engineering**: Menambahkan fitur baru untuk meningkatkan performa model.
4. **Pemodelan**: Menggunakan algoritma seperti Logistic Regression dan Random Forest untuk memprediksi churn.
5. **Evaluasi Model**: Mengukur akurasi model dan mengevaluasi dengan confusion matrix.

## Insight Hasil Analisis
- **Akurasi Model**: Logistic Regression menghasilkan akurasi yang cukup baik dalam memprediksi churn.
- **Fitur Penting**: Tenure pelanggan, jenis layanan, dan biaya bulanan adalah faktor yang signifikan dalam memprediksi churn.
- **Imbalance Dataset**: Data yang tidak seimbang mengharuskan penggunaan teknik SMOTE untuk oversampling kelas minoritas.

## Cara Menjalankan Proyek
1. Clone repositori ini:
   ```bash
   git clone https://github.com/username/Data-Analyst-Project-Business-Decision-Research.git
   ```
2. Instal semua dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Jalankan notebook Jupyter untuk analisis:
   ```bash
   jupyter notebook notebooks/analysis_notebook.ipynb
   ```

## Lisensi
[MIT License](LICENSE)
