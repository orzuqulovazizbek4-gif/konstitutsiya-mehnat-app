import streamlit as st
import pandas as pd

# ---------------------------------------------------------
# 1. PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Konstitutsiyaviy va Mehnat Huquqlari Tahlili",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# 2. APPLE LIQUID GLASS & DYNAMIC ANIMATIONS (HTML/CSS)
# ---------------------------------------------------------
st.markdown("""
<!-- REAL LIQUID ANIMATION CONTAINER -->
<div class="liquid-bg-container">
    <div class="liquid-orb orb-1"></div>
    <div class="liquid-orb orb-2"></div>
    <div class="liquid-orb orb-3"></div>
</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600&display=swap');

    html, body, [class*="stApp"] {
        font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Inter", sans-serif !important;
        background-color: #030712 !important;
        color: #f8fafc !important;
    }

    [data-testid="stAppViewContainer"] {
        background: #030712 !important;
    }

    [data-testid="stHeader"] {
        background: transparent !important;
    }

    /* 🌌 DYNAMIC LIQUID ORBS ANIMATION */
    .liquid-bg-container {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        overflow: hidden;
        z-index: 0;
        pointer-events: none;
    }

    .liquid-orb {
        position: absolute;
        border-radius: 50%;
        filter: blur(90px);
        opacity: 0.45;
        will-change: transform;
    }

    .orb-1 {
        top: -10%;
        left: 15%;
        width: 50vw;
        height: 50vw;
        background: radial-gradient(circle, #38bdf8 0%, #0284c7 60%, rgba(0,0,0,0) 100%);
        animation: orbFloat1 16s ease-in-out infinite alternate;
    }

    .orb-2 {
        bottom: -15%;
        right: 10%;
        width: 55vw;
        height: 55vw;
        background: radial-gradient(circle, #8b5cf6 0%, #6366f1 60%, rgba(0,0,0,0) 100%);
        animation: orbFloat2 20s ease-in-out infinite alternate;
    }

    .orb-3 {
        top: 40%;
        left: 45%;
        width: 35vw;
        height: 35vw;
        background: radial-gradient(circle, #ec4899 0%, #a855f7 60%, rgba(0,0,0,0) 100%);
        animation: orbFloat3 18s ease-in-out infinite alternate;
    }

    @keyframes orbFloat1 {
        0% { transform: translate3d(0, 0, 0) scale(1); }
        50% { transform: translate3d(140px, 90px, 0) scale(1.25); }
        100% { transform: translate3d(-80px, 120px, 0) scale(0.9); }
    }

    @keyframes orbFloat2 {
        0% { transform: translate3d(0, 0, 0) scale(1); }
        50% { transform: translate3d(-120px, -100px, 0) scale(1.2); }
        100% { transform: translate3d(60px, -50px, 0) scale(0.95); }
    }

    @keyframes orbFloat3 {
        0% { transform: translate3d(0, 0, 0) scale(0.9); }
        50% { transform: translate3d(-90px, 80px, 0) scale(1.3); }
        100% { transform: translate3d(100px, -70px, 0) scale(1); }
    }

    /* 🍏 APPLE PAGE TRANSITION ANIMATION */
    .main .block-container {
        position: relative;
        z-index: 2;
        max-width: 1200px;
        padding-top: 2rem;
        animation: appleEnter 0.65s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }

    @keyframes appleEnter {
        0% {
            opacity: 0;
            transform: translateY(30px) scale(0.97);
            filter: blur(12px);
        }
        100% {
            opacity: 1;
            transform: translateY(0) scale(1);
            filter: blur(0px);
        }
    }

    /* 🍏 APPLE GLASSMORPHIC CARDS */
    .main-header {
        background: rgba(255, 255, 255, 0.04) !important;
        backdrop-filter: blur(35px) saturate(210%) !important;
        -webkit-backdrop-filter: blur(35px) saturate(210%) !important;
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        border-top: 1px solid rgba(255, 255, 255, 0.3) !important;
        padding: 2.2rem 2.5rem;
        border-radius: 28px;
        margin-bottom: 2rem;
        box-shadow: 0 30px 60px rgba(0, 0, 0, 0.4);
    }

    .main-header h1 {
        background: linear-gradient(135deg, #ffffff 0%, #e2e8f0 50%, #38bdf8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
        font-size: 2.2rem;
        letter-spacing: -0.02em;
        margin-bottom: 0.6rem;
    }

    .main-header p {
        color: #94a3b8 !important;
        font-size: 1.1rem;
        margin: 0;
    }

    .legal-card {
        background: rgba(255, 255, 255, 0.035) !important;
        backdrop-filter: blur(30px) saturate(200%) !important;
        -webkit-backdrop-filter: blur(30px) saturate(200%) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-top: 1px solid rgba(255, 255, 255, 0.22) !important;
        border-radius: 24px;
        padding: 1.8rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.35);
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .legal-card:hover {
        transform: translateY(-6px) scale(1.01);
        background: rgba(255, 255, 255, 0.06) !important;
        border-color: rgba(56, 189, 248, 0.5) !important;
        box-shadow: 0 30px 60px rgba(0, 0, 0, 0.5), 0 0 30px rgba(56, 189, 248, 0.25);
    }

    .legal-card h3 {
        color: #ffffff !important;
        font-weight: 600;
        font-size: 1.25rem;
        margin: 0;
    }

    .badge-citizen {
        background: rgba(56, 189, 248, 0.18) !important;
        color: #38bdf8 !important;
        padding: 0.4rem 1rem;
        border-radius: 999px;
        font-weight: 600;
        font-size: 0.82rem;
        border: 1px solid rgba(56, 189, 248, 0.4);
    }

    .badge-everyone {
        background: rgba(52, 211, 153, 0.18) !important;
        color: #34d399 !important;
        padding: 0.4rem 1rem;
        border-radius: 999px;
        font-weight: 600;
        font-size: 0.82rem;
        border: 1px solid rgba(52, 211, 153, 0.4);
    }

    .norm-box {
        background: rgba(15, 23, 42, 0.55) !important;
        backdrop-filter: blur(15px) !important;
        border-left: 4px solid #38bdf8 !important;
        padding: 1.2rem;
        border-radius: 14px;
        margin: 1.2rem 0;
        color: #f1f5f9 !important;
    }

    .code-badge {
        font-weight: 600;
        color: #38bdf8 !important;
        background: rgba(56, 189, 248, 0.15) !important;
        padding: 4px 10px;
        border-radius: 8px;
        border: 1px solid rgba(56, 189, 248, 0.3);
    }

    section[data-testid="stSidebar"] {
        background: rgba(10, 15, 30, 0.65) !important;
        backdrop-filter: blur(35px) saturate(200%) !important;
        -webkit-backdrop-filter: blur(35px) saturate(200%) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.1) !important;
        z-index: 3;
    }

    div[data-testid="stSidebar"] div[role="radiogroup"] > label {
        background: rgba(255, 255, 255, 0.03) !important;
        border: 1px solid rgba(255, 255, 255, 0.06) !important;
        padding: 0.75rem 1rem !important;
        border-radius: 16px !important;
        margin-bottom: 0.6rem !important;
        transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1) !important;
        cursor: pointer !important;
    }

    div[data-testid="stSidebar"] div[role="radiogroup"] > label:hover {
        background: rgba(255, 255, 255, 0.12) !important;
        border-color: rgba(56, 189, 248, 0.5) !important;
        transform: translateX(6px) scale(1.02);
    }

    div[data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.035) !important;
        backdrop-filter: blur(25px) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-top: 1px solid rgba(255, 255, 255, 0.2) !important;
        padding: 1.2rem;
        border-radius: 20px;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 3. VERIFIED LEGAL DATABASE & DATASTRUCTURES
# ---------------------------------------------------------

ARTICLES_DATA = {
    36: {
        "title": "36-modda. Jamiyat va davlat ishlarini boshqarishda ishtirok etish",
        "category": "Faqat Fuqarolarga",
        "badge_class": "badge-citizen",
        "text": "Oʻzbekiston Respublikasining fuqarolari jamiyat va davlat ishlarini boshqarishda bevosita hamda oʻz vakillari orqali ishtirok etish huquqiga ega...",
        "applicability": "Faqat Oʻzbekiston Respublikasi fuqarolariga tatbiq etiladi.",
        "non_applicability": "Chet el fuqarolari va fuqaroligi boʻlmagan shaxslarga tatbiq etilmaydi.",
        "reasoning": "Davlat suverenitetini amalga oshirish va davlat hokimiyati organlarini shakllantirish siyosiy huquq bo'lib, u shaxs va davlat o'rtasidagi siyosiy-huquqiy bog'liqlikni (fuqarolikni) talab etadi.",
        "related_laws": "'Chet el fuqarolarining va fuqaroligi bo'lmagan shaxslarning huquqiy holati to'g'risida'gi Qonun (O'RQ-692) 26-28-moddalari"
    },
    37: {
        "title": "37-modda. Davlat xizmatiga kirishdagi tenglik",
        "category": "Faqat Fuqarolarga",
        "badge_class": "badge-citizen",
        "text": "Oʻzbekiston Respublikasining fuqarolari davlat xizmatiga kirishda teng huquqqa egadirlar. Davlat xizmatini oʻtash bilan bogʻliq cheklovlar qonun bilan belgilanadi.",
        "applicability": "Faqat Oʻzbekiston Respublikasi fuqarolariga tatbiq etiladi.",
        "non_applicability": "Chet el fuqarolari va fuqaroligi boʻlmagan shaxslarga tatbiq etilmaydi.",
        "reasoning": "Davlat xizmatchilari davlat funksiyalarini bajaradi va davlat siri bilan ishlaydi. Bu davlatga nisbatan huquqiy va siyosiy sodiqlikni talab etadi.",
        "related_laws": "'Davlat fuqarolik xizmati to'g'risida'gi Qonun (O'RQ-788) 27 va 28-moddalari"
    },
    38: {
        "title": "38-modda. Tinch yig'ilishlar va namoyishlar erkinligi",
        "category": "Faqat Fuqarolarga",
        "badge_class": "badge-citizen",
        "text": "Fuqarolar oʻz ijtimoiy faolliklarini Oʻzbekiston Respublikasi qonunlariga muvofiq mitinglar, yigʻilishlar va namoyishlar shaklida amalga oshirish huquqiga ega...",
        "applicability": "Faqat Oʻzbekiston Respublikasi fuqarolariga tatbiq etiladi.",
        "non_applicability": "Chet el fuqarolariga va fuqaroligi boʻlmagan shaxslarga tatbiq etilmaydi.",
        "reasoning": "Mamlakatning ichki siyosiy va ijtimoiy hayotiga nisbatan iroda bildirish siyosiy huquq sanaladi.",
        "related_laws": "MJtK 201-modda, JK 217-modda"
    },
    39: {
        "title": "39-modda. Birlashish va siyosiy partiyalarga a'zolik huquqi",
        "category": "Faqat Fuqarolarga (Siyosiy partiyalar bo'yicha)",
        "badge_class": "badge-citizen",
        "text": "Oʻzbekiston Respublikasi fuqarolari kasaba uyushmalariga, siyosiy partiyalarga va boshqa jamoat birlashmalariga uyushish huquqiga egadirlar...",
        "applicability": "Siyosiy partiyalarga a'zo bo'lish va faoliyat yuritish faqat fuqarolarga tegishli.",
        "non_applicability": "Chet el fuqarolarining siyosiy partiyalarga a'zo bo'lishi taqiqlanadi.",
        "reasoning": "Siyosiy partiyalar davlat hokimiyatini shakllantirishda ishtirok etadi. Tinchlik va xavfsizlik nuqtai nazaridan ajnabiy shaxslarga bu huquq berilmaydi.",
        "related_laws": "'Siyosiy partiyalar to'g'risida'gi Qonun 8-modda"
    },
    40: {
        "title": "40-modda. Davlat organlariga murojaat qilish huquqi",
        "category": "Har Kimga",
        "badge_class": "badge-everyone",
        "text": "Har kim bevosita oʻzi va boshqalar bilan birgalikda davlat organlariga hamda tashkilotlariga... murojaat qilish huquqiga ega.",
        "applicability": "O'zbekiston fuqarolari, chet el fuqarolari va fuqaroligi bo'lmagan shaxslarga.",
        "non_applicability": "Cheklov yo'q.",
        "reasoning": "Shaxsiy huquq va qonuniy manfaatlarni davlat idoralari orqali himoya qilish universal insoniy kafolatdir.",
        "related_laws": "'Jismoniy va yuridik shaxslarning murojaatlari to'g'risida'gi Qonun (O'RQ-378)"
    },
    41: {
        "title": "41-modda. Mulkdor bo'lish va meros huquqi",
        "category": "Har Kimga",
        "badge_class": "badge-everyone",
        "text": "Har bir shaxs mulkdor boʻlishga haqli. Bank operatsiyalarining sir tutilishi va meros huquqi qonun bilan kafolatlanadi.",
        "applicability": "Barcha jismoniy shaxslarga (fuqarolikka bog'liq emas).",
        "non_applicability": "Cheklov yo'q.",
        "reasoning": "Mulk va meros huquqi insonning iqtisodiy erkinligini ta'minlovchi fundamental huquqdir.",
        "related_laws": "O'zR Fuqarolik Kodeksi 164 va 1112-moddalari"
    },
    42: {
        "title": "42-modda. Munosib mehnat sharoiti va adolatli haq olish",
        "category": "Har Kimga",
        "badge_class": "badge-everyone",
        "text": "Har kim munosib mehnat qilish, kasb va faoliyat turini erkin tanlash, xavfsizlik va gigiyena talablariga javob beradigan qulay mehnat sharoitlarida ishlash...",
        "applicability": "O'zbekiston hududida mehnat qilayotgan barcha shaxslarga.",
        "non_applicability": "Cheklov yo'q.",
        "reasoning": "Xavfsiz va munosib mehnat sharoitiga ega bo'lish insoniy qadr-qimmat va jismoniy daxlsizlik kafolatidir.",
        "related_laws": "Yangi Mehnat Kodeksi 5, 119 va 343-moddalari"
    },
    43: {
        "title": "43-modda. Bandlik va ishsizlikdan himoyalanish",
        "category": "Faqat Fuqarolarga (Ijtimoiy nafaqalar bo'yicha)",
        "badge_class": "badge-citizen",
        "text": "Davlat fuqarolarning bandligini taʼminlash, ularni ishsizlikdan himoya qilish choralarini koʻradi...",
        "applicability": "Davlat byudjeti hisobidan ijtimoiy yordam va ishsizlik nafaqasi birinchi navbatda fuqarolarga beriladi.",
        "non_applicability": "Chet el fuqarolariga davlat byudjetidan ishsizlik nafaqasi to'lanmaydi.",
        "reasoning": "Ijtimoiy ta'minot davlatning o'z fuqarolari oldidagi konstitutsiyaviy majburiyatidir.",
        "related_laws": "'Aholi bandligi to'g'risida'gi Qonun (O'RQ-642)"
    },
    44: {
        "title": "44-modda. Majburiy mehnat va bolalar mehnatini taqiqlash",
        "category": "Har Kimga",
        "badge_class": "badge-everyone",
        "text": "Sud qarori bilan tayinlangan jazoni ijro etish tartibidan tashqari majburiy mehnat va bolalar mehnati taqiqlanadi...",
        "applicability": "O'zbekiston hududidagi barcha shaxslarga.",
        "non_applicability": "Cheklov yo'q (Mutloq taqiq).",
        "reasoning": "Insonni erksizlantirish va majburan ishlatish xalqaro huquqda insoniy qadr-qimmatni toptash deb baholanadi.",
        "related_laws": "Yangi Mehnat Kodeksi 7-modda, MJtK 51-modda, JK 148²-modda"
    }
}

LIABILITY_DATA = [
    {
        "const_art": "42-modda",
        "right": "Munosib va xavfsiz mehnat sharoiti, adolatli haq olish",
        "violation": "Xodimlarga xavfsizlik va sanitariya talablariga javob bermaydigan ish joyini taqdim etish yoki ish haqini to'lamaslik.",
        "mk": "Yangi MK 343-modda (Mehnatni muhofaza qilish) & 253-modda (Ish haqini to'lash)",
        "mjtk": "MJtK 49-modda (Mehnat qonunchiligini buzish)",
        "jk": "JK 257-modda (Mehnatni muhofaza qilish qoidalarini buzish - og'ir oqibat tug'dirsa)"
    },
    {
        "const_art": "42 & 43-modda",
        "right": "Kamsitishga yo'l qo'ymaslik, bandlik kafolati",
        "violation": "Homilador ayolni yoki yosh bolali shaxsni ishga olishni asossiz rad etish yoki ishdan bo'shatish.",
        "mk": "Yangi MK 5-modda (Kamsitish taqiqlanishi) & 119, 403-moddalar",
        "mjtk": "MJtK 50-modda (Aholi bandligi qonunchiligini buzish)",
        "jk": "JK 148¹-modda (Homilador yoki yosh bolali ayolni ishga olishni rad etish yoki bo'shatish)"
    },
    {
        "const_art": "44-modda",
        "right": "Majburiy mehnat va bolalar mehnatini taqiqlash",
        "violation": "Xodimlarni uning roziligisiz mehnat shartnomasida bo'lmagan xizmatlarga majburan jalb etish.",
        "mk": "Yangi MK 7-modda (Majburiy mehnat taqiqlanishi)",
        "mjtk": "MJtK 51-modda (Mehnatga ma'muriy tarzda majburlash)",
        "jk": "JK 148²-modda (Mehnatga ma'muriy tarzda majburlash - takroran sodir etilsa)"
    },
    {
        "const_art": "45-modda",
        "right": "Dam olish huquqi",
        "violation": "Haftalik ish vaqti normasi (40 soat)ni oshirish, har yilgi mehnat ta'tilini asossiz bermaslik.",
        "mk": "Yangi MK 181-modda (Normal ish vaqti) & 216-modda (Har yilgi ta'til majburiyligi)",
        "mjtk": "MJtK 49-modda (Mehnat qonunchiligini buzish)",
        "jk": "Nizolashib g'arazli ravishda bo'shatilsa: JK 148-modda"
    }
]

# ---------------------------------------------------------
# 4. SIDEBAR NAVIGATION
# ---------------------------------------------------------
st.sidebar.image("https://img.icons8.com/color/96/scales.png", width=70)
st.sidebar.title("Huquqiy Tahlil")
st.sidebar.caption("Apple Dynamic Liquid Edition")

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
- Yangi Mehnat Kodeksi (2023)
- Davlat fuqarolik xizmati t.g. Qonun (O'RQ-788)
- MJtK va Jinoyat Kodeksi
""")

# ---------------------------------------------------------
# 5. MAIN CONTENT HEADER
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
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px;">
                <h3>{data['title']}</h3>
                <span class="{data['badge_class']}">{data['category']}</span>
            </div>
            <div class="norm-box">
                <em>"{data['text']}"</em>
            </div>
            <div style="margin-top: 14px; line-height: 1.65;">
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
        * **Sohaviy Qonun:** "Davlat fuqarolik xizmati to'g'risida"gi Qonun (O'RQ-788) 27-28-moddalari va "Siyosiy partiyalar to'g'risida"gi Qonun 8-moddasi.
        * **Sabab:** Davlat suvereniteti va xavfsizligini ta'minlash.
        """)
    elif scenario.startswith("2."):
        st.warning("⚠️ **Majburiy Mehnat!** Xodimni shartnomadan tashqari ishga majburlash qonunga zid.")
        st.markdown("""
        * **Konstitutsiyaviy Asos:** 44-modda (Majburiy mehnat taqiqi - Har kimga tegishli).
        * **Yangi Mehnat Kodeksi:** 7-modda (Majburiy mehnat taqiqlanishi).
        * **Javobgarlik:** MJtK 51-moddasi (Ma'muriy jarima). Agar ma'muriy jazodan keyin takroran sodir etilsa — **JK 148²-modda**.
        """)
    elif scenario.startswith("3."):
        st.error("🚨 **Og'ir Huquqbuzarlik!** Homilador ayolning mehnat huquqini kamsitish.")
        st.markdown("""
        * **Konstitutsiyaviy Asos:** 42-modda (Munosib mehnat va kamsitmaslik kafolati).
        * **Yangi Mehnat Kodeksi:** 5, 119 va 403-moddalar.
        * **Javobgarlik:** Bevosita **JK 148¹-moddasi** bo'yicha jinoiy javobgarlik kelib chiqadi.
        """)
    elif scenario.startswith("4."):
        st.warning("⚠️ **Dam olish va mehnat sharoiti huquqi buzilishi.**")
        st.markdown("""
        * **Konstitutsiyaviy Asos:** 42-modda va 45-modda (Dam olish va munosib mehnat sharoiti).
        * **Yangi Mehnat Kodeksi:** 181-modda (Haftasiga maks. 40 soat) va 216-modda (Ta'til majburiyligi).
        * **Javobgarlik:** **MJtK 49-moddasi** (Mehnat qonunchiligini buzish).
        """)
