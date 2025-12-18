# BLG-407 Makine Öğrenmesi - 3. Proje Ödevi

[cite_start]Bu proje, ev fiyatlarını tahmin etmek amacıyla **Çoklu Doğrusal Regresyon (Multiple Linear Regression)** modeli kullanılarak geliştirilmiş ve **Flask** tabanlı bir web arayüzü (GUI) ile sunulmuştur[cite: 3, 28].

## 👤 Öğrenci Bilgileri
* [cite_start]**Adı:** Zeynep 
* [cite_start]**Soyadı:** Söylemez 
* [cite_start]**Okul Numarası:** 2212721031 

## 📝 Proje Özeti
Proje kapsamında seçilen veri seti üzerinde veri ön işleme, istatistiksel analiz ve modelleme çalışmaları yapılmıştır. [cite_start]Eğitilen model bir web arayüzü üzerinden kullanıcı girişlerine göre fiyat tahmini yapmaktadır[cite: 28].

## 🛠️ Uygulanan Adımlar

### [cite_start]1. Veri Ön İşleme (Data Preprocessing) [cite: 29]
* [cite_start]**Öznitelik Seçimi:** Model için en anlamlı olan maksimum 10 öznitelik seçilmiştir[cite: 30, 31].
* [cite_start]**Kayıp Veri Analizi:** Veri setindeki eksik değerler kontrol edilerek silme veya doldurma işlemleri uygulanmıştır[cite: 33, 35].
* [cite_start]**Kategorik Veriler:** Sayısal olmayan veriler Label Encoding veya One-Hot Encoding yöntemleriyle sayısal hale getirilmiştir[cite: 36, 37].

### [cite_start]2. Geriye Doğru Eleme (Backward Elimination) [cite: 41]
* [cite_start]İstatistiksel olarak anlamsız öznitelikleri belirlemek için Backward Elimination yöntemi uygulanmıştır[cite: 42].
* [cite_start]$p > 0.05$ olan değişkenler modelden arındırılarak en optimize model kurulmuştur[cite: 44].

### [cite_start]3. Model Kurulumu ve Değerlendirme [cite: 45]
* [cite_start]Çoklu doğrusal regresyon modeli eğitilmiş ve aşağıdaki metriklerle performans ölçümü yapılmıştır[cite: 46, 47]:
    * [cite_start]**$R^{2}$ (R Kare)** [cite: 48]
    * [cite_start]**MAE (Mean Absolute Error)** [cite: 49]
    * [cite_start]**MSE (Mean Squared Error)** [cite: 50]

### [cite_start]4. Flask Arayüzü [cite: 52]
* [cite_start]Eğitilen model `.pkl` formatında kaydedilerek Flask uygulamasında kullanılmıştır[cite: 53].
* [cite_start]Kullanıcının metrekare, oda sayısı gibi özellikleri girebileceği basit ve işlevsel bir form tasarlanmıştır[cite: 55, 56].

## [cite_start]📂 Dosya Yapısı [cite: 60]
* [cite_start]`MLP_Flask.ipynb`: Veri analizi ve model eğitim adımlarının bulunduğu dosya[cite: 61].
* [cite_start]`model.pkl`: Eğitilmiş ve kaydedilmiş regresyon modeli[cite: 62].
* [cite_start]`app.py`: Flask sunucu kodları ve web arayüzü yönetimi[cite: 63].
* `templates/index.html`: Web arayüzü tasarım dosyası.
* [cite_start]`README.md`: Proje dökümantasyonu.

## 🚀 Kurulum ve Çalıştırma
1. Gerekli kütüphaneleri yükleyin: `pip install flask pandas scikit-learn statsmodels`
2. Uygulamayı başlatın: `python app.py`
3. Tarayıcıdan `http://127.0.0.1:5000` adresine giderek tahmin panelini kullanın.
