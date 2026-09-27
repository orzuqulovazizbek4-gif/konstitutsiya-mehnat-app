import streamlit as st
import pandas as pd

# ---------------------------------------------------------
# 1. PAGE CONFIGURATION & METADATA
# ---------------------------------------------------------
st.set_page_config(
    page_title="Konstitutsiyaviy va Mehnat Huquqlari Tahlili",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# 2. ADVANCED ANIMATED BACKGROUND & GLASSMORPHISM CSS
# ---------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* 🌌 ANIMATED MULTI-LAYER GRADIENT BACKGROUND */
    .stApp {
        background: linear-gradient(-45deg, #070a12, #0f172a, #1e1b4b, #091e3a, #0b1329);
        background-size: 400% 400%;
        animation: gradientBG 18s ease infinite;
        position: relative;
        overflow-x: hidden;
    }

    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* 🔮 FLOATING NEON GLOW SPHERE 1 */
    .stApp::before {
        content: '';
        position: fixed;
        top: -15%;
        left: -10%;
        width: 50vw;
        height: 50vw;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(59, 130, 246, 0.3) 0%, rgba(0,0,0,0) 70%);
        animation: floatOrb1 12s ease-in-out infinite alternate;
        pointer-events: none;
        z-index: 0;
    }

    /* 🔮 FLOATING NEON GLOW SPHERE 2 */
    .stApp::after {
        content: '';
        position: fixed;
        bottom: -20%;
        right: -10%;
        width: 60vw;
        height: 60vw;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(99, 102, 241, 0.25) 0%, rgba(0,0,0,0) 70%);
        animation: floatOrb2 15s ease-in-out infinite alternate;
        pointer-events: none;
        z-index: 0;
    }

    @keyframes floatOrb1 {
        0% { transform: translate(0, 0) scale(1); }
        100% { transform: translate(120px, 80px) scale(1.25); }
    }

    @keyframes floatOrb2 {
        0% { transform: translate(0, 0) scale(1); }
        100% { transform: translate(-100px, -90px) scale(1.3); }
    }

    /* 💎 GLASSMORPHISM HEADER */
    .main-header {
        background: rgba(15, 23, 42, 0.75) !important;
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.12);
        padding: 2.2rem;
        border-radius: 20px;
        color: #ffffff !important;
        margin-bottom: 2rem;
        box-shadow: 0 20px 40px rgba(0,0,0,0.4);
        position: relative;
        z-index: 1;
    }
    
    .main-header h1 {
        color: #ffffff !important;
        font-weight: 700;
        margin-bottom: 0.5rem;
        text-shadow: 0 2px 10px rgba(0,0,0,0.5);
    }
    
    .main-header p {
        color: #93c5fd !important;
        font-size: 1.1rem;
        margin: 0;
    }

    /* 🃏 GLASSMORPHIC LEGAL CARDS WITH HOVER ANIMATION */
    .legal-card {
        background: rgba(30, 41, 59, 0.65) !important;
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 16px;
        padding: 1.6rem;
        margin-bottom: 1.4rem;
        color: #f8fafc !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        z-index: 1;
    }

    .legal-card:hover {
        transform: translateY(-6px) scale(1.01);
        box-shadow: 0 16px 40px 0 rgba(59, 130, 246, 0.3);
        border: 1px solid rgba(96, 165, 250, 0.5) !important;
    }

    .legal-card h3 {
        color: #ffffff !important;
        margin: 0;
    }

    .legal-card p, .legal-card div, .legal-card em, .legal-card strong {
        color: #cbd5e1 !important;
    }
    
    .badge-citizen {
        background: rgba(30, 58, 138, 0.8) !important;
        color: #93c5fd !important;
        padding: 0.35rem 0.9rem;
        border-radius: 9999px;
        font-weight: 600;
        font-size: 0.85rem;
        display: inline-block;
        border: 1px solid #3b82f6;
        box-shadow: 0 0 12px rgba(59, 130, 246, 0.4);
    }

    .badge-everyone {
        background: rgba(6, 78, 59, 0.8) !important;
        color: #6ee7b7 !important;
        padding: 0.35rem 0.9rem;
        border-radius: 9999px;
        font-weight: 600;
        font-size: 0.85rem;
        display: inline-block;
        border: 1px solid #10b981;
        box-shadow: 0 0 12px rgba(16, 185, 129, 0.4);
    }

    .norm-box {
        background: rgba(15, 23, 42, 0.7) !important;
        border-left: 4px solid #3b82f6 !important;
        padding: 1.1rem;
        border-radius: 0 10px 10px 0;
        margin: 1rem 0;
        color: #e2e8f0 !important;
        backdrop-filter: blur(8px);
    }

    .norm-box em {
        color: #93c5fd !important;
    }

    .code-badge {
        font-weight: 700;
        color: #38bdf8 !important;
        background: rgba(15, 23, 42, 0.8) !important;
        padding: 5px 10px;
        border-radius: 6px;
        border: 1px solid #0284c7;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 3. DATABASE & LEGAL CONTENT DATASTRUCTURES
# ---------------------------------------------------------

ARTICLES_DATA = {
    36: {
        "title": "36-modda. Jamiyat va davlat ishlarini boshqarishda ishtirok etish",
        "category": "Faqat Fuqarolarga",
        "badge_class": "badge-citizen",
        "text": "Oʻzbekiston Respublikasining fuqarolari jamiyat va davlat ishlarini boshqarishda bevosita hamda oʻz vakillari orqali ishtirok etish huquqiga ega...",
        "applicability": "Faqat Oʻzbekiston Respublikasi fuqarolariga tatbiq etiladi.",
        "non_applicability": "Chet el fuqarolari va fuqaroligi boʻlmagan shaxslarga tatbiq etilmaydi.",
        "reasoning": "Davlat suverenitetini amalga oshirish va davlat hokimiyati organlarini demokratik shakllantirish siyosiy huquq bo'lib, u bevosita shaxs va davlat o'rtasidagi siyosiy-huquqiy bog'liqlikni (fuqarolikni) talab etadi.",
        "related_laws": "O'zR 'Chet el fuqarolarining va fuqaroligi bo'lmagan shaxslarning huquqiy holati to'g'risida'gi Qonunining 26-moddasi."
    },
    37: {
        "title": "37-modda. Davlat xizmatiga kirishdagi tenglik",
        "category": "Faqat Fuqarolarga",
        "badge_class": "badge-citizen",
        "text": "Oʻzbekiston Respublikasining fuqarolari davlat xizmatiga kirishda teng huquqqa egadirlar. Davlat xizmatini oʻtash bilan bogʻliq cheklovlar qonun bilan belgilanadi.",
        "applicability": "Faqat Oʻzbekiston Respublikasi fuqarolariga tatbiq etiladi.",
        "non_applicability": "Chet el fuqarolari va fuqaroligi boʻlmagan shaxslarga tatbiq etilmaydi.",
        "reasoning": "Davlat xizmatchilari davlat funksiyalari va vakolatlarini bajaradi. Bu davlat sirlari bilan ishlash hamda davlatga bo'lgan mutloq siyosiy sodiqlikni taqazo etadi.",
        "related_laws": "'Davlat fuqarolik xizmati to'g'risida'gi Qonunning 19-moddasi."
    },
    38: {
        "title": "38-modda. Tinch yig'ilishlar va namoyishlar erkinligi",
        "category": "Faqat Fuqarolarga",
        "badge_class": "badge-citizen",
        "text": "Fuqarolar oʻz ijtimoiy faolliklarini Oʻzbekiston Respublikasi qonunlariga muvofiq mitinglar, yigʻilishlar va namoyishlar shaklida amalga oshirish huquqiga ega...",
        "applicability": "Faqat Oʻzbekiston Respublikasi fuqarolariga tatbiq etiladi.",
        "non_applicability": "Chet el fuqarolariga va fuqaroligi boʻlmagan shaxslarga tatbiq etilmaydi.",
        "reasoning": "Mamlakatning ichki siyosiy muhitiga nisbatan iroda bildirish va ijtimoiy-siyosiy talablar surish siyosiy subyektlikni, ya'ni fuqarolikni talab qiladi.",
        "related_laws": "MJtK 201-modda, JK 217-modda."
    },
    39: {
        "title": "39-modda. Birlashish va siyosiy partiyalarga a'zolik huquqi",
        "category": "Faqat Fuqarolarga (Siyosiy partiyalar bo'yicha)",
        "badge_class": "badge-citizen",
        "text": "Oʻzbekiston Respublikasi fuqarolari kasaba uyushmalariga, siyosiy partiyalarga va boshqa jamoat birlashmalariga uyushish, ommaviy harakatlarda ishtirok etish huquqiga egadirlar...",
        "applicability": "Siyosiy partiyalarga a'zolik va siyosiy harakatlarda ishtirok etish faqat fuqarolarga tegishli.",
        "non_applicability": "Chet el fuqarolari siyosiy partiyalarga a'zo bo'lishi taqiqlanadi.",
        "reasoning": "Siyosiy partiyalar davlat hokimiyatini egallash yoki unda ishtirok etish uchun kurashadi. Ajnabiy shaxslarning partiyalarga kirishi davlatning ichki ishlariga aralashish xavfini tug'diradi.",
        "related_laws": "'Siyosiy partiyalar to'g'risida'gi Qonun 8-modda."
    },
    40: {
        "title": "40-modda. Davlat organlariga murojaat qilish huquqi",
        "category": "Har Kimga",
        "badge_class": "badge-everyone",
        "text": "Har kim bevosita oʻzi va boshqalar bilan birgalikda davlat organlariga hamda tashkilotlariga, fuqarolarning oʻzini oʻzi boshqarish organlariga... murojaat qilish huquqiga ega.",
        "applicability": "O'zbekiston fuqarolari, chet el fuqarolari va fuqaroligi bo'lmagan har bir shaxsga.",
        "non_applicability": "Cheklov yo'q. Barcha shaxslarga teng tatbiq etiladi.",
        "reasoning": "Inson huquq va erkinliklarini, qonuniy manfaatlarini davlat idoralari orqali himoya qilish har bir shaxsning universal kafolatidir.",
        "related_laws": "'Jismoniy va yuridik shaxslarning murojaatlari to'g'risida'gi Qonun."
    },
    41: {
        "title": "41-modda. Mulkdor bo'lish va meros huquqi",
        "category": "Har Kimga",
        "badge_class": "badge-everyone",
        "text": "Har bir shaxs mulkdor boʻlishga haqli. Bank operatsiyalarining, omonatlarning va hisobvaraqlarning sir tutilishi, shuningdek meros huquqi qonun bilan kafolatlanadi.",
        "applicability": "Har bir jismoniy shaxsga (fuqaroligi bo'lishidan qat'i nazar).",
        "non_applicability": "Cheklov yo'q.",
        "reasoning": "Mulk huquqi insonning iqtisodiy erkinligi va shaxsiy daxlsizligining poydevori bo'lib, fuqarolikka bog'liq bo'lmagan fundamental huquqdir.",
        "related_laws": "O'zbekiston Respublikasi Fuqarolik Kodeksi."
    },
    42: {
        "title": "42-modda. Munosib mehnat sharoiti va adolatli haq olish",
        "category": "Har Kimga",
        "badge_class": "badge-everyone",
        "text": "Har kim munosib mehnat qilish, kasb va faoliyat turini erkin tanlash, xavfsizlik va gigiyena talablariga javob beradigan qulay mehnat sharoitlarida ishlash...",
        "applicability": "O'zbekiston hududida mehnat faoliyatini olib borayotgan barcha shaxslarga.",
        "non_applicability": "Cheklov yo'q.",
        "reasoning": "Mehnat qilish, xavfsiz sharoitda bo'lish va mehnatiga yarasha haq olish insonning jismoniy va ijtimoiy yashash huquqi bilan bog'liq xalqaro inson huquqidir.",
        "related_laws": "Mehnat Kodeksi 11-modda, MJtK 49-modda, JK 257-modda."
    },
    43: {
        "title": "43-modda. Bandlik va ishsizlikdan himoyalanish",
        "category": "Faqat Fuqarolarga (Ijtimoiy kafolat va nafaqalar bo'yicha)",
        "badge_class": "badge-citizen",
        "text": "Davlat fuqarolarning bandligini taʼminlash, ularni ishsizlikdan himoya qilish, shuningdek kambagʻallikni qisqartirish choralarini koʻradi...",
        "applicability": "Davlatning ijtimoiy-iqtisodiy majburiyatlari va nafaqa/yordamlari birinchi navbatda fuqarolarga tatbiq etiladi.",
        "non_applicability": "Chet el fuqarolariga davlat byudjeti hisobidan ishsizlik nafaqasi to'lanmaydi.",
        "reasoning": "Ijtimoiy muhofaza va kambag'allikni qisqartirish davlatning o'z fuqarolari oldidagi ijtimoiy shartnomasidan kelib chiqadigan majburiyatidir.",
        "related_laws": "'Aholini bandlik bilan ta'minlash to'g'risida'gi Qonun."
    },
    44: {
        "title": "44-modda. Majburiy mehnat va bolalar mehnatini taqiqlash",
        "category": "Har Kimga",
        "badge_class": "badge-everyone",
        "text": "Sud qarori bilan tayinlangan jazoni ijro etish tartibidan yoxud qonunda nazarda tutilgan boshqa hollardan tashqari majburiy mehnat taqiqlanadi...",
        "applicability": "O'zbekiston hududidagi barcha shaxslarga va bolalarga.",
        "non_applicability": "Cheklov yo'q (Mutloq taqiq).",
        "reasoning": "Insonni erksizlantirish, majburiy mehnatga va bolalarning rivojlanishiga zarar yetkazuvchi mehnatga jalb etish inson qadr-qimmatiga qarshi og'ir g'ayriinsoniy holatdir.",
        "related_laws": "MK 5-modda, MJtK 51-modda, JK 148²-modda."
    }
}

LIABILITY_DATA = [
    {
        "const_art": "42-modda",
        "right": "Munosib va xavfsiz mehnat sharoiti, adolatli haq olish",
        "violation": "Xodimlarga xavfsizlik va sanitariya talablariga javob bermaydigan ish joyini taqdim etish yoki ish haqini o'z vaqtida to'lamaslik.",
        "mk": "21-modda (Mehnatni muhofaza qilish) & 244-modda (Ish haqini to'lash muddatlari)",
        "mjtk": "49-modda (Mehnat va mehnatni muhofaza qilish to'g'risidagi qonunchilikni buzish)",
        "jk": "257-modda (Mehnatni muhofaza qilish qoidalarini buzish - og'ir oqibatlarga olib kelsa)"
    },
    {
        "const_art": "42 & 43-modda",
        "right": "Kamsitishga yo'l qo'ymaslik, bandlik kafolati",
        "violation": "Ayolni homiladorligi yoki yosh bolasi borligi sababli ishga olishni rad etish yoki noqonuniy ishdan bo'shatish.",
        "mk": "4-modda (Kamsitishni taqiqlash) & 119-modda (Ishga qabulni asossiz rad etmaslik)",
        "mjtk": "50-modda (Aholini bandlik bilan ta'minlash qonunchiligini buzish)",
        "jk": "148¹-modda (Homilador yoki yosh bolali ayolni ishga olishni rad etish yoki bo'shatish)"
    },
    {
        "const_art": "44-modda",
        "right": "Majburiy mehnat va bolalar mehnatini taqiqlash",
        "violation": "Xodimlarni (o'qituvchi, shifokor va h.k.) uning roziligisiz shartnomada bo'lmagan xizmatlarga majburan jalb etish.",
        "mk": "5-modda (Majburiy mehnatni taqiqlash) & 115-modda (Shartnomadan tashqari ish taqiqi)",
        "mjtk": "51-modda (Mehnatga ma'muriy tarzda majburlash)",
        "jk": "148²-modda (Mehnatga ma'muriy tarzda majburlash - ma'muriy jazodan so'ng takroran sodir etilsa)"
    },
    {
        "const_art": "45-modda",
        "right": "Dam olish huquqi",
        "violation": "Haftalik ish vaqti me'yorini (40 soat) noqonuniy oshirish, ta'til berishdan asossiz bosh tortish.",
        "mk": "181-modda (Ish vaqtining normal davomiyligi) & 216-modda (Har yilgi ta'til majburiyligi)",
        "mjtk": "49-modda (Mehnat to'g'risidagi qonunchilikni buzish)",
        "jk": "Nizolashgan holatda bo'shatilsa: JK 148-modda (G'arazli ravishda ishdan bo'shatish)"
    }
]

# ---------------------------------------------------------
# 4. SIDEBAR NAVIGATION
# ---------------------------------------------------------
st.sidebar.image("https://img.icons8.com/color/96/scales.png", width=80)
st.sidebar.title("Huquqiy Tahlil Markazi")
st.sidebar.caption("Konstitutsiyaviy va Sohaviy Qonunchilik Birligi")

nav_option = st.sidebar.radio(
    "Bo'limni tanlang:",
    [
        "🏛️ Subyektlar bo'yicha tasnif (36-44)",
        "⚖️ Uch bosqichli javobgarlik (42-45)",
        "🔍 Kazus Simulyatori"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("""
**Manbalar:**
- O'zR Konstitutsiyasi (2023)
- Mehnat Kodeksi (2023)
- Ma'muriy Javobgarlik t.g. Kodeks
- Jinoyat Kodeksi
""")

# ---------------------------------------------------------
# 5. HEADER SECTION
# ---------------------------------------------------------
st.markdown("""
<div class="main-header">
    <h1>Oʻzbekiston Respublikasi Konstitutsiyasi va Sohaviy Qonunchilik Tahlili</h1>
    <p>Inson huquqlari, fuqarolik maqomi va mehnat huquqlarini muhofaza qilishning kompleks tizimi</p>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# TAB 1: 36-44 MODDALAR TASNIFI
# ---------------------------------------------------------
if nav_option == "🏛️ Subyektlar bo'yicha tasnif (36-44)":
    st.subheader("Konstitutsiyaning 36–44-moddalari Subyektlar Bo'yicha Tasnifi")
    st.write("Ushbu bo'limda huquqlarning kimgaligi (faqat fuqaro yoki har kim) va ularning mantiqiy-huquqiy asoslari keltirilgan.")

    col1, col2, col3 = st.columns(3)
    col1.metric("Tahlil qilingan moddalar", "9 ta")
    col2.metric("Faqat Fuqarolarga tegishli", "5 ta", delta="Siyosiy & Ijtimoiy kafolat")
    col3.metric("Har kimga tegishli", "4 ta", delta="Insoniy fundamental")

    st.markdown("---")

    filter_type = st.selectbox(
        "Kategoriyani saralang:",
        ["Barcha moddalar", "Faqat Fuqarolarga", "Har Kimga"]
    )

    for art_num, data in ARTICLES_DATA.items():
        if filter_type == "Faqat Fuqarolarga" and "Faqat" not in data["category"]:
            continue
        if filter_type == "Har Kimga" and "Har Kimga" not in data["category"]:
            continue

        st.markdown(f"""
        <div class="legal-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                <h3>{data['title']}</h3>
                <span class="{data['badge_class']}">{data['category']}</span>
            </div>
            <div class="norm-box">
                <em>"{data['text']}"</em>
            </div>
            <div style="margin-top: 12px; line-height: 1.6;">
                <p><strong>✅ Qaysi shaxslarga tatbiq etiladi:</strong> {data['applicability']}</p>
                <p><strong>❌ Qaysi shaxslarga tatbiq etilmaydi:</strong> {data['non_applicability']}</p>
                <p><strong>🧠 Mantiqiy-huquqiy asos va sababi:</strong> {data['reasoning']}</p>
                <p><strong>📜 Boshqa qonunlardagi asosi:</strong> <span class="code-badge">{data['related_laws']}</span></p>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------------
# TAB 2: MEHNAT HUQUQLARI VA JAVOBGARLIK (42-45)
# ---------------------------------------------------------
elif nav_option == "⚖️ Uch bosqichli javobgarlik (42-45)":
    st.subheader("Mehnat Huquqlari Buzilishining Uch Bosqichli Asoslanishi")
    st.write("Konstitutsiyaviy normalarning Mehnat Kodeksi (MK), Ma'muriy Javobgarlik (MJtK) va Jinoyat Kodeksi (JK) bilan mantiqiy bog'liqligi.")

    df_liability = pd.DataFrame(LIABILITY_DATA)
    df_liability.columns = [
        "Konstitutsiya", "Kafolatlangan Huquq", "Huquqbuzarlik Holati",
        "Mehnat Kodeksi (MK)", "Ma'muriy Kodeks (MJtK)", "Jinoyat Kodeksi (JK)"
    ]

    st.dataframe(df_liability, use_container_width=True, hide_index=True)

    st.markdown("### 🔍 Har bir holat bo'yicha mukammal asoslama:")

    for item in LIABILITY_DATA:
        with st.expander(f"📌 {item['const_art']} — {item['right']}"):
            st.markdown(f"**Huquqbuzarlik shakli:** {item['violation']}")
            st.markdown(f"- **Mehnat Kodeksi qoidasi:** `{item['mk']}`")
            st.markdown(f"- **Ma'muriy Javobgarlik (MJtK):** `{item['mjtk']}`")
            st.markdown(f"- **Jinoyat Javobgarligi (JK):** `{item['jk']}`")
            
            st.info("""
            **Chegara va Mantiqiy Asos:**
            Fuqaroning mehnat huquqi buzilganda dastlab **MJtK** bo'yicha ma'muriy jarima qo'llaniladi. 
            Agar huquqbuzarlik takroran sodir etilsa, shaxsga og'ir moddiy/jismoniy zarar yetsa yoki maxsus toifa (homilador ayol, voyaga yetmaganlar) huquqi poymol etilsa, javobgarlik **JK** doirasida malakalanadi.
            """)

# ---------------------------------------------------------
# TAB 3: KAZUS SIMULYATORI
# ---------------------------------------------------------
elif nav_option == "🔍 Kazus Simulyatori":
    st.subheader("Amaliy Huquqiy Holatlar va Kazuslar Simulyatori")
    st.write("Muayyan amaliy vaziyatni tanlang va tizim uning qaysi moddalar bo'yicha malakalanishini avtomatik ko'rsatib beradi.")

    scenario = st.selectbox(
        "Amaliy vaziyatni tanlang:",
        [
            "--- Vaziyatni tanlang ---",
            "1. Chet el fuqarosi O'zbekistonda siyosiy partiyaga a'zo bo'lmoqchi va davlat organiga ishga kirmoqchi.",
            "2. Ish beruvchi o'qituvchini uning roziligisiz ko'cha supirishga va obodonlashtirishga majburlamoqda.",
            "3. Homilador ayol ishga kirish uchun suhbatdan o'tdi, lekin homiladorligi sababli rad javobi berildi.",
            "4. Tashkilot xodimiga 2 yildan beri har yilgi mehnat ta'tili berilmayapti va haftasiga 50 soatdan ishlatilmoqda."
        ]
    )

    if scenario.startswith("1."):
        st.error("❌ **Taqiq mavjud!** Chet el fuqarosi siyosiy partiyaga a'zo bo'la olmaydi va davlat xizmatiga qabul qilinmaydi.")
        st.markdown("""
        * **Konstitutsiyaviy Asos:** 37-modda va 39-modda (Faqat O'zbekiston fuqarolariga tegishli huquq).
        * **Sohaviy Qonun:** "Siyosiy partiyalar to'g'risida"gi Qonun 8-modda, "Davlat fuqarolik xizmati to'g'risida"gi Qonun 19-modda.
        * **Sabab:** Davlat suvereniteti va xavfsizligini ta'minlash.
        """)
    elif scenario.startswith("2."):
        st.warning("⚠️ **Majburiy Mehnat!** Xodimni shartnomadan tashqari ishga majburlash qonunga zid.")
        st.markdown("""
        * **Konstitutsiyaviy Asos:** 44-modda (Majburiy mehnat taqiqi - Har kimga tegishli).
        * **Mehnat Kodeksi:** 5-modda va 115-modda.
        * **Javobgarlik:** MJtK 51-moddasi (Ma'muriy jarima). Agar ma'muriy jazodan keyin takroran sodir etilsa — **JK 148²-modda**.
        """)
    elif scenario.startswith("3."):
        st.error("🚨 **Og'ir Huquqbuzarlik!** Homilador ayolning mehnat huquqini kamsitish.")
        st.markdown("""
        * **Konstitutsiyaviy Asos:** 42-modda 3-qism (Homiladorligi sababli ishga olishni rad etish taqiqlanadi).
        * **Mehnat Kodeksi:** 4-modda, 119-modda va 403-modda.
        * **Javobgarlik:** Bevosita **JK 148¹-moddasi** bo'yicha jinoiy javobgarlik kelib chiqadi.
        """)
    elif scenario.startswith("4."):
        st.warning("⚠️ **Dam olish va mehnat sharoiti huquqi buzilishi.**")
        st.markdown("""
        * **Konstitutsiyaviy Asos:** 42-modda va 45-modda (Dam olish va munosib mehnat sharoiti).
        * **Mehnat Kodeksi:** 181-modda (Haftasiga maks. 40 soat) va 216-modda (Ta'til majburiyligi).
        * **Javobgarlik:** **MJtK 49-moddasi** (Mehnat qonunchiligini buzish).
        """)
