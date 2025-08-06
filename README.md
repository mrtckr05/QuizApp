# QuizApp Python (Flask)

Bir Flask tabanlı web bilgi yarışması uygulaması. Adam asmaca tarzı yanlış cevap takibi, çoktan seçmeli sorular ve AI destekli İngilizce kategori içerir.

## Özellikler

- Birden fazla kategori (Fen, Tarih, Coğrafya, İngilizce-AI)
- Sorular SQLite veritabanından veya İngilizce için Gemini AI ile dinamik üretilir
- Adam asmaca tarzı yanlış cevap görselleştirme
- Soru başına zamanlayıcı ve ipucu (AI-powered Hint, 3 hak)
- Responsive tasarım (Bootstrap)
- Kategoriye göre zorluk seviyeli soru dağılımı

## Kurulum

1. **Bağımlılıkları yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Gemini API anahtarınızı ekleyin:**
   - `app.py` dosyasındaki `key = "your-api-key-here"` satırını kendi anahtarınızla değiştirin.

3. **Uygulamayı başlatın:**
   ```bash
   python app.py
   ```

4. **Tarayıcıda açın:**
   ```
   http://127.0.0.1:5000
   ```

## Oynanış

1. İsim girin ve kategori seçin
2. Soruları tek tek cevaplayın
3. Her yanlış cevap adam asmaca görselini ilerletir
4. 3 kez AI destekli ipucu alabilirsiniz
5. Tüm soruları tamamlayın veya maksimum yanlış sayısına ulaşınca oyun biter

## Klasör Yapısı

```
QuizApp/
├── app.py
├── requirements.txt
├── static/
│   └── img/              # Adam asmaca görselleri
├── templates/            # HTML şablonları
│   ├── index.html
│   ├── quiz.html
│   └── result.html
└── questions/
    ├── questions.db      # SQLite veritabanı
    ├── questions.py      # Soru tanımları
    └── write_questions_to_db.py  # Veritabanı doldurma scripti
```

## Kategoriler

- **Fen (Science):** Veritabanından
- **Tarih (History):** Veritabanından
- **Coğrafya (Geography):** Veritabanından
- **İngilizce-AI Sana Sorsun:** Gemini AI ile dinamik, seviyeli İngilizce sorular

## Notlar

- İngilizce kategorisinde sorular ve cevaplar AI tarafından anlık üretilir, internet bağlantısı ve geçerli bir Gemini API anahtarı gereklidir.
- AI ipucu özelliği tüm kategorilerde kullanılabilir (3 hak).
