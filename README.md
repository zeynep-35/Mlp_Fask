# Makine Öğrenmesi  
## 3. Proje Ödevi – Ev Fiyat Tahmini

Bu proje, BLG-407 Makine Öğrenmesi dersi kapsamında gerçekleştirilmiş olup,
ev fiyatlarını tahmin etmek amacıyla bir **Makine Öğrenmesi modeli**
geliştirilmesini ve bu modelin bir **web arayüzü üzerinden sunulmasını**
amaçlamaktadır.

Proje sürecinde **Çoklu Doğrusal Regresyon (Multiple Linear Regression)**
algoritması kullanılmış ve model, **Flask tabanlı bir web uygulaması**
ile kullanıcı etkileşimine açılmıştır.

---

## 👤 Öğrenci Bilgileri

- **Adı:** Zeynep  
- **Soyadı:** Söylemez  
- **Okul Numarası:** 2212721031  
- **Ders:** BLG-407 Makine Öğrenmesi  

---

## 🎯 Projenin Amacı

Bu projenin temel amacı, geçmiş konut verilerini kullanarak bir evin
fiyatını etkileyen faktörleri analiz etmek ve bu faktörlere bağlı olarak
**yeni bir ev için fiyat tahmini yapabilen bir model** geliştirmektir.

Ayrıca geliştirilen modelin, teknik bilgisi olmayan kullanıcılar tarafından
da kullanılabilmesi için **web tabanlı bir arayüz** ile sunulması hedeflenmiştir.

---

## 📊 Kullanılan Veri Seti

Projede kullanılan veri seti **Kaggle** platformundan temin edilmiştir.
Veri seti; evlerin konumu, oda sayısı, metrekare bilgisi, bina yaşı gibi
fiyatı etkileyen çeşitli öznitelikleri içermektedir.

📌 Dataset linki:  
🔗 https://www.kaggle.com/datasets/prokshitha/home-value-insights

---

## 🔍 Veri Ön İşleme (Data Preprocessing)

Modelleme aşamasından önce veri seti üzerinde çeşitli ön işleme adımları
uygulanmıştır:

- Eksik (missing) verilerin kontrol edilmesi ve gerekli düzenlemelerin yapılması  
- Sayısal verilerin model için uygun hale getirilmesi  
- Bağımlı ve bağımsız değişkenlerin belirlenmesi  
- Model eğitimine uygun veri yapısının hazırlanması  

Bu adımlar sayesinde modelin daha doğru ve kararlı sonuçlar üretmesi
sağlanmıştır.

---

## 🤖 Kullanılan Model: Çoklu Doğrusal Regresyon

Proje kapsamında **Çoklu Doğrusal Regresyon** algoritması kullanılmıştır.
Bu yöntem, birden fazla bağımsız değişkenin, bağımlı değişken üzerindeki
etkisini aynı anda incelemeye olanak tanımaktadır.

Model:
- Eğitim verisi kullanılarak eğitilmiştir  
- Ev fiyatlarını tahmin etmek için kullanılmıştır  

---

## 📈 Model Performansı ve Değerlendirme

Modelin başarımı çeşitli hata metrikleri kullanılarak değerlendirilmiştir.
Gerçek değerler ile tahmin edilen değerler karşılaştırılarak modelin
genel performansı analiz edilmiştir.

Elde edilen sonuçlar, seçilen modelin ev fiyat tahmini problemi için
uygun olduğunu göstermektedir.

---

## 🌐 Web Arayüzü (Flask)

Geliştirilen makine öğrenmesi modeli, **Flask** kullanılarak oluşturulan
bir web arayüzüne entegre edilmiştir.

Web arayüzü sayesinde:
- Kullanıcı, ev özelliklerini forma girebilmektedir  
- Model, girilen değerlere göre fiyat tahmini yapmaktadır  
- Tahmin sonucu kullanıcıya anlık olarak gösterilmektedir  

Bu sayede model, teorik bir çalışmadan çıkarılarak **kullanılabilir bir
uygulama** haline getirilmiştir.

---

## ⚙️ Kullanılan Teknolojiler

- Python  
- NumPy  
- Pandas  
- Scikit-learn  
- Flask  
- Jupyter Notebook  

---

## ▶️ Projeyi Çalıştırma

1. Gerekli kütüphaneler yüklenir:
   ```bash
   pip install numpy pandas scikit-learn flask
   
