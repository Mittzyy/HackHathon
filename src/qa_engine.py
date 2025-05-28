# src/qa_engine.py
import logging

def get_answer(query: str) -> str:
    q = query.lower()
    faq = {
        # Matematika
        "apa itu matematika": "Matematika adalah ilmu yang mempelajari bilangan, struktur, ruang, dan perubahan.",
        "rumus luas persegi": "Rumus luas persegi adalah sisi × sisi.",
        "rumus luas segitiga": "Rumus luas segitiga adalah ½ × alas × tinggi.",
        "berapa hasil 7 kali 8": "7 kali 8 adalah 56.",
        "apa itu aljabar": "Aljabar adalah cabang matematika yang mempelajari simbol dan aturan operasi pada simbol tersebut.",

        # AI dan teknologi
        "apa itu ai": "AI adalah teknologi yang memungkinkan komputer melakukan tugas yang biasanya membutuhkan kecerdasan manusia.",
        "contoh ai": "Contoh AI adalah chatbot, asisten virtual, sistem rekomendasi, dan kendaraan otonom.",
        "bahaya ai": "Bahaya AI muncul jika teknologi digunakan tanpa kontrol, misal privasi terganggu atau keputusan tidak adil.",
        "apa itu machine learning": "Machine learning adalah bagian dari AI yang memungkinkan komputer belajar dari data tanpa diprogram secara eksplisit.",

        # Pemrograman
        "apa itu python": "Python adalah bahasa pemrograman yang mudah dipelajari dan banyak digunakan dalam AI dan web development.",
        "siapa pembuat python": "Python dibuat oleh Guido van Rossum pada tahun 1991.",
        "apa itu coding": "Coding adalah proses menulis instruksi untuk komputer agar bisa melakukan tugas tertentu.",

        # Literasi digital
        "apa itu internet": "Internet adalah jaringan global yang menghubungkan komputer di seluruh dunia.",
        "cara aman di internet": "Jangan bagikan data pribadi, gunakan password kuat, dan hati-hati terhadap tautan mencurigakan.",
        "apa itu hoaks": "Hoaks adalah informasi palsu yang sengaja disebarkan agar orang percaya dan menyebarkannya lagi.",

        # Sains & lingkungan
        "apa itu pemanasan global": "Pemanasan global adalah peningkatan suhu bumi akibat emisi gas rumah kaca.",
        "cara menjaga lingkungan": "Hemat listrik, kurangi sampah plastik, tanam pohon, dan gunakan kendaraan ramah lingkungan.",

        # Motivasi belajar
        "cara rajin belajar": "Buat jadwal, cari tempat tenang, beri reward pada diri, dan istirahat cukup.",
        "pentingnya sekolah": "Sekolah membuka kesempatan mendapatkan ilmu, teman, dan masa depan lebih cerah.",

        # Bahasa Inggris
        "apa arti hello": "Hello artinya halo, salam sapaan dalam bahasa Inggris.",
        "apa arti thank you": "Thank you artinya terima kasih.",

        # Sosial dan budaya
        "apa itu toleransi": "Toleransi adalah sikap menghargai perbedaan pendapat, suku, agama, dan budaya.",
        "apa itu gotong royong": "Gotong royong adalah kerja bersama untuk mencapai tujuan bersama.",

        # EduLocal khusus
        "apa itu daerah 3t": "Daerah 3T adalah wilayah Terdepan, Terpencil, dan Tertinggal yang sering kekurangan fasilitas pendidikan dan teknologi.",
        "manfaat teknologi di daerah 3t": "Memudahkan akses pendidikan, informasi, dan komunikasi meski daerah sulit dijangkau.",

        # Hiburan & interaksi lucu
        "siapa orang terganteng": "Yang terganteng sudah pasti MIMIT! 😉",
        "siapa orang tercantik": "Yang terganteng sudah pasti Della DONKKK! 😉",
        "kamu siapa": "Aku EduLocal AI, teman belajar digital kamu.",
        "kamu bisa apa": "Aku bisa jawab pertanyaan tentang matematika, AI, teknologi, dan bantu belajar.",
        "terima kasih": "Sama-sama! Semoga harimu menyenangkan!",

        # Tambahan penting lainnya
        "apa itu blockchain": "Blockchain adalah teknologi buku besar digital terdesentralisasi yang aman dan transparan.",
        "apa itu cryptocurrency": "Cryptocurrency adalah mata uang digital yang menggunakan teknologi blockchain.",
        "apa itu internet of things": "Internet of Things (IoT) adalah jaringan perangkat yang saling terhubung dan dapat bertukar data.",
        "apa itu cloud computing": "Cloud computing adalah penyimpanan dan pengolahan data melalui internet tanpa harus punya server fisik sendiri.",
    }

    for k, v in faq.items():
        if k in q:
            return v

    return (
        "Maaf, aku masih belajar dan belum mengerti pertanyaanmu. "
        "Coba tanya tentang matematika, AI, Python, teknologi, atau tips belajar."
    )
