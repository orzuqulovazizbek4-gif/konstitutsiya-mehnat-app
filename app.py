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
# 2. REAL APPLE LIQUID GLASS & ANIMATED BACKGROUND (HTML/CSS)
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

    /* BASE ROOT & STREAMLIT OVERRIDES */
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

    /* 🌌 DYNAMIC LIQUID ORBS ANIMATION (REAL MOTION) */
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

    /* 🍏 APPLE PAGE TRANSITION ANIMATION (BO'LIMLAR O'TGANDA) */
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

    /* 🍏 APPLE HIGH-GLOSS LIQUID GLASS CARDS */
    .main-header {
        background: rgba(255, 255, 255, 0.04) !important;
        backdrop-filter: blur(35px) saturate(210%) !important;
        -webkit-backdrop-filter: blur(35px) saturate(210%) !important;
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
        border-top: 1px solid rgba(255, 255, 255, 0.3) !important;
        padding: 2.2rem 2.5rem;
        border-radius: 28px;
        margin-bottom: 2rem;
        box-shadow: 0 30px 60px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.2);
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
        animation: appleEnter 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
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
        box-shadow: 0 0 15px rgba(56, 189, 248, 0.2);
    }

    .badge-everyone {
        background: rgba(52, 211, 153, 0.18) !important;
        color: #34d399 !important;
        padding: 0.4rem 1rem;
        border-radius: 999px;
        font-weight: 600;
        font-size: 0.82rem;
        border: 1px solid rgba(52, 211, 153, 0.4);
        box-shadow: 0 0 15px rgba(52, 211, 153, 0.2);
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

    /* 🎛️ SIDEBAR & RADIO INTERACTION ANIMATIONS */
    section[data-testid="stSidebar"] {
        background: rgba(10, 15, 30, 0.65) !important;
        backdrop-filter: blur(35px) saturate(200%) !important;
        -webkit-backdrop-filter: blur(35px) saturate(200%) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.1) !important;
        z-index: 3;
    }

    /* APPLE MENU BUTTONS EFFECT */
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
        box-shadow: 0 10px 25px rgba(56, 189, 248, 0.2);
    }

    div[data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.035) !important;
        backdrop-filter: blur(25px) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-top: 1px solid rgba(255, 255, 255, 0.2) !important;
        padding: 1.2rem;
        border-radius: 20px;
        box-shadow: 0 15px 30px rgba(0,0,0,0.3);
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 3. DATABASE & LEGAL CONTENT
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
- Mehnat Kodeksi (2023)
- Ma'muriy Javobgarlik t.g. Kodeks
- Jinoyat Kodeksi
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
