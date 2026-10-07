import streamlit as st

# ==============================
# CONFIGURATION
# ==============================
st.set_page_config(
    page_title="LanguaBot",
    page_icon="🤖",
    layout="wide"
)

# ==============================
# STYLE
# ==============================
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #07152f, #0b1f3f);
        color: white;
    }

    [data-testid="stSidebar"] {
        background: #06142d;
    }

    .title {
        font-size: 42px;
        font-weight: 800;
        color: white;
    }

    .subtitle {
        font-size: 19px;
        color: #b8c7e6;
    }

    .hero {
        padding: 35px;
        border-radius: 25px;
        background: linear-gradient(135deg, #087cff, #14b8e8);
        margin-bottom: 25px;
    }

    .card {
        padding: 22px;
        border-radius: 18px;
        background: #10264a;
        border: 1px solid #234674;
        margin-bottom: 15px;
    }

    .bot {
        padding: 18px;
        border-radius: 18px;
        background: #10264a;
        margin: 10px 0;
    }

    .user {
        padding: 18px;
        border-radius: 18px;
        background: #087cff;
        margin: 10px 0;
        text-align: right;
    }

    .language {
        font-size: 20px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# ==============================
# LANGUES
# ==============================
languages = {
    "🇫🇷 Français": {
        "hello": "Bonjour 👋",
        "welcome": "Je suis ton assistant pour apprendre le français.",
        "example": "Bonjour ! Comment ça va ?"
    },
    "🇬🇧 Anglais": {
        "hello": "Hello 👋",
        "welcome": "I am your assistant for learning English.",
        "example": "Hello! How are you?"
    },
    "🇪🇸 Espagnol": {
        "hello": "¡Hola! 👋",
        "welcome": "Soy tu assistant para aprender español.",
        "example": "¡Hola! ¿Cómo estás?"
    },
    "🇩🇪 Allemand": {
        "hello": "Hallo 👋",
        "welcome": "Ich bin dein Assistent zum Deutschlernen.",
        "example": "Hallo! Wie geht es dir?"
    },
    "🇮🇹 Italien": {
        "hello": "Ciao 👋",
        "welcome": "Sono il tuo assistente per imparare l'italiano.",
        "example": "Ciao! Come stai?"
    },
    "🇸🇦 Arabe": {
        "hello": "مرحبا 👋",
        "welcome": "أنا مساعدك لتعلم اللغة العربية.",
        "example": "مرحبا! كيف حالك؟"
    },
    "🇨🇳 Chinois": {
        "hello": "你好 👋",
        "welcome": "我是你的中文学习助手。",
        "example": "你好！你好吗？"
    },
    "🇯🇵 Japonais": {
        "hello": "こんにちは 👋",
        "welcome": "日本語を学ぶためのアシスタントです。",
        "example": "こんにちは！元気ですか？"
    },
    "🇵🇹 Portugais": {
        "hello": "Olá 👋",
        "welcome": "Sou o seu assistente para aprender português.",
        "example": "Olá! Como você está?"
    }
}

# ==============================
# SIDEBAR
# ==============================
with st.sidebar:

    st.markdown("## 🤖 LanguaBot")

    st.caption("Apprends des langues avec ton assistant IA !")

    st.markdown("---")

    st.markdown("### 🏠 Accueil")
    st.markdown("### 📚 Apprendre une langue")
    st.markdown("### 📊 Mes progrès")
    st.markdown("### ⚙️ Paramètres")

    st.markdown("---")

    st.markdown("### 🌍 Langues disponibles")

    for language in languages:
        st.markdown(f"**{language}**")

    st.markdown("---")

    st.info(
        "🎯 Chaque mot appris est "
        "une nouvelle porte vers le monde ! 🌍"
    )

# ==============================
# CHOIX DE LANGUE
# ==============================
st.markdown("""
<div class="hero">
    <div class="title">🤖 Bonjour ! Je suis LanguaBot</div>
    <div class="subtitle">
        Ton assistant pour apprendre des langues facilement
        et à ton rythme !
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.success("🧠 Pratique")

with col2:
    st.info("📖 Interactif")

with col3:
    st.warning("⭐ Personnalisé")

with col4:
    st.error("❤️ Amusant")

st.markdown("### 🌍 Choisis une langue")

language = st.selectbox(
    "Langue",
    list(languages.keys())
)

data = languages[language]

# ==============================
# CHATBOT
# ==============================
st.markdown("### 💬 Conversation")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "bot",
            "text": f"{data['hello']} ! {data['welcome']}"
        }
    ]

# Affichage
for message in st.session_state.messages:

    if message["role"] == "bot":
        st.markdown(
            f"""
            <div class="bot">
                🤖 <b>LanguaBot</b><br><br>
                {message["text"]}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:
        st.markdown(
            f"""
            <div class="user">
                👤 {message["text"]}
            </div>
            """,
            unsafe_allow_html=True
        )

# ==============================
# MESSAGE
# ==============================
message = st.chat_input(
    "Écris ton message..."
)

if message:

    st.session_state.messages.append({
        "role": "user",
        "text": message
    })

    # Réponse simple du chatbot
    response = (
        f"Très bien ! 😊 Tu apprends le {language}. "
        f"Voici une phrase à pratiquer : "
        f"<b>{data['example']}</b>"
    )

    st.session_state.messages.append({
        "role": "bot",
        "text": response
    })

    st.rerun()

# ==============================
# PROGRESSION
# ==============================
st.markdown("---")

st.markdown("### 📊 Ton apprentissage")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Mots appris", "25", "+5")

with col2:
    st.metric("Leçons", "8", "+2")

with col3:
    st.metric("Progression", "65%", "+10%")

st.progress(0.65)

st.markdown(
    "<center>🌍 LanguaBot • Apprendre aujourd'hui, parler demain 🚀</center>",
    unsafe_allow_html=True
)
