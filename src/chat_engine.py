# src/chat_engine.py

import logging, re
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from .translator import translate_to_id, translate_to_en, detect_language

# initialize ChatBot with SQLite storage
chatbot = ChatBot(
    'EduLocalChatter',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///data/chatbot.sqlite3',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ],
    read_only=True
)
trainer = ListTrainer(chatbot)

def train_if_needed():
    """
    Latih sekali dengan data bilingual kaya topik untuk 3T.
    """
    try:
        basic_data = [
            # School Subjects – Math
            "Kenapa kita perlu belajar matematika?", 
            "Matematika berguna dalam kehidupan sehari-hari, misalnya untuk menghitung uang, mengukur jarak atau waktu.",
            "Why do we need to learn math?", 
            "Math is useful in daily life, for example to count money, measure distance or time.",

            # Science
            "Kenapa langit berwarna biru?", 
            "Karena cahaya Matahari tersebar oleh udara di langit. Cahaya warna biru paling banyak tersebar, sehingga langit terlihat biru.",
            "Why is the sky blue?", 
            "Because sunlight is scattered by the air in the sky. Blue light scatters the most, so the sky appears blue.",

            # Social Studies
            "Apa tugas seorang kepala desa?", 
            "Kepala desa memimpin dan mengatur jalannya pemerintahan di desa. Ia melayani warga serta mengelola pembangunan dan keamanan di desa.",
            "What are the duties of a village head?", 
            "A village head leads and manages the administration in the village. They serve the residents and oversee development and security.",

            # Indonesian Language
            "Apa perbedaan huruf vokal dan huruf konsonan?", 
            "Huruf vokal adalah huruf yang bunyinya keluar lancar tanpa terhalang, contohnya a, e, i, o, u. "
            "Huruf konsonan bunyinya keluar dengan terhalang oleh lidah, gigi, atau bibir, jadi mencakup semua huruf selain vokal.",
            "What is the difference between vowels and consonants?", 
            "Vowels are letters whose sounds flow freely without being blocked (a, e, i, o, u). "
            "Consonants are letters whose sounds are blocked by the tongue, teeth, or lips—everything else.",

            # English Language
            "Apa manfaat belajar bahasa Inggris?", 
            "Bahasa Inggris adalah bahasa internasional. Dengan bisa berbahasa Inggris, kita dapat berkomunikasi dengan orang dari berbagai negara, mengakses lebih banyak ilmu, dan mendapatkan peluang lebih baik.",
            "What are the benefits of learning English?", 
            "English is an international language. By knowing English, we can communicate globally, access more knowledge, and gain better educational or job opportunities.",

            # Art
            "Kenapa kita belajar seni di sekolah?", 
            "Seni membantu kita menjadi kreatif dan mengekspresikan diri. Belajar seni juga melatih keterampilan motorik halus dan mengenal budaya.",
            "Why do we learn art at school?", 
            "Art helps us be creative and express ourselves. Learning art develops fine motor skills and cultural appreciation.",

            # Sports
            "Mengapa olahraga penting untuk kesehatan?", 
            "Olahraga membuat tubuh sehat dan kuat. Peredaran darah lancar, otot dan tulang kuat, dan kita memiliki lebih banyak energi.",
            "Why is exercise important for health?", 
            "Exercise makes our body healthy and strong. It improves blood circulation, strengthens muscles and bones, and boosts energy.",

            # Daily Life – Health
            "Kenapa kita harus mencuci tangan sebelum makan?", 
            "Karena tangan kita mungkin mengandung kuman. Mencuci tangan dengan sabun membersihkan kuman agar makanan aman.",
            "Why should we wash our hands before eating?", 
            "Because our hands might have germs. Washing with soap removes germs so our food is safe.",

            # Ethics
            "Mengapa kita harus bersikap jujur?", 
            "Jika kita jujur, orang lain akan percaya kepada kita. Bersikap jujur juga membuat hati tenang dan hubungan baik.",
            "Why should we be honest?", 
            "If we are honest, others will trust us. Honesty also brings peace of mind and builds good relationships.",

            # Safety – Earthquake
            "Apa yang harus dilakukan jika terjadi gempa bumi?", 
            "Saat gempa: berlindung di bawah meja kokoh atau menjauhi jendela. Setelah gempa: keluar ke tempat terbuka dengan tenang.",
            "What should be done if an earthquake happens?", 
            "During the quake: take cover under a sturdy table or stay away from windows. "
            "Afterwards: calmly move to an open area.",

            # Survival Skills
            "Apa saja yang perlu dibawa saat pergi ke hutan?", 
            "Bawa air minum, makanan ringan, senter, peluit, kompas atau peta—untuk bertahan jika terjadi hal tak terduga.",
            "What items should be brought when going to the forest?", 
            "Bring drinking water, snacks, a flashlight, a whistle, and a compass or map—for safety in unexpected situations.",

            # Digital Literacy
            "Bagaimana cara menggunakan internet dengan aman?", 
            "Jangan berikan info pribadi ke orang asing, pilih situs aman, dan beri tahu orang tua jika menemukan hal tidak pantas.",
            "How can we use the Internet safely?", 
            "Don’t share personal info with strangers, choose age-appropriate sites, and tell a parent or teacher if you see something uncomfortable.",

            # Local Wisdom
            "Apa itu gotong royong?", 
            "Gotong royong adalah kerja sama sukarela untuk kebaikan bersama, misalnya warga saling membantu tanpa mengharapkan imbalan.",
            "What is gotong royong?", 
            "Gotong royong is voluntary cooperation for the common good, like villagers helping one another without expecting payment.",

            # Environment – Conservation
            "Mengapa hutan perlu dilindungi?", 
            "Hutan adalah rumah bagi banyak hewan dan tumbuhan. Mereka juga membersihkan udara, mencegah banjir, dan menyediakan sumber daya.",
            "Why do forests need to be protected?", 
            "Forests are home to many species. They clean the air, prevent floods, and provide resources.",

            # Natural Resource Use
            "Bagaimana cara menghemat air di rumah?", 
            "Tutup keran saat tidak pakai, mandi dan cuci secukupnya, gunakan air bekas cucian untuk menyiram tanaman.",
            "How can we save water at home?", 
            "Turn off taps when not in use, bathe and wash sparingly, and reuse wash water for plants.",

            # Recycling
            "Apa itu daur ulang?", 
            "Daur ulang adalah mengubah sampah jadi barang baru, misalnya botol plastik menjadi pot tanaman.",
            "What is recycling?", 
            "Recycling is turning trash into new items, such as making plant pots from used plastic bottles.",

            # Humor
            "Siapa orang tertampan di dunia?",
            "Tentu saja,Miftah Donggg.",
            "Siapa orang tercantik?",
            "Incess Della lah,siapa lagi kocak",
            
            # Alternative Energy
            "Apa yang dimaksud dengan energi alternatif?", 
            "Energi alternatif adalah sumber selain minyak atau batu bara—misalnya matahari, angin, dan air.",
            "What is meant by alternative energy?", 
            "Alternative energy comes from sources other than oil or coal—such as the sun, wind, and water.",
        ]
        trainer.train(basic_data)

    except Exception as e:
        logging.getLogger("uvicorn.error").warning("Training skipped: %s", e)


train_if_needed()

def preprocess_text(text: str) -> str:
    """Clean input by removing extra punctuation."""
    return re.sub(r'[^\w\s?]', '', text).strip()

def get_response(text: str) -> str:
    """
    Auto-multilingual:
     - Detect language
     - If en: translate->answer->translate back
     - If id: answer directly
    """
    try:
        clean = preprocess_text(text)
        lang = detect_language(clean)

        if lang == 'en':
            # English flow
            in_id = translate_to_id(clean)
            resp_id = chatbot.get_response(in_id)
            return translate_to_en(str(resp_id))

        elif lang == 'id':
            # Bahasa Indonesia flow
            return str(chatbot.get_response(clean))

        else:
            return ("Maaf, bahasa tersebut belum didukung. "
                    "Silakan gunakan Bahasa Indonesia atau Inggris.")

    except Exception as err:
        logging.getLogger("uvicorn.error").exception(f"ChatEngine Error: {err}")
        return "Maaf, saya belum mengerti—coba pertanyaan lain, ya."

# Optional CLI test
if __name__ == "__main__":
    for q in [
        "What is mathematics?",
        "Apa itu AI?",
        "Bagaimana AI digunakan di dunia pendidikan?",
        "Who invented electricity?",
        "Bisakah kamu menghitung 10 tambah 15?"
    ]:
        print(f"Q: {q}\nA: {get_response(q)}\n")
