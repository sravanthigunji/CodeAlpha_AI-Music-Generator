import streamlit as st
import os

st.set_page_config(page_title="AI Music Generator", page_icon="🎵", layout="wide")

st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #08001f, #16002e, #2b004f);
    color: white;
}

[data-testid="stHeader"] {
    background: transparent;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #120022, #1b1238);
}

h1 {
    text-align: center;
    font-size: 55px;
    background: linear-gradient(90deg, #c084fc, #60a5fa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

h2, h3, label {
    color: white !important;
}

p {
    color: #e5e7eb;
    text-align: center;
    font-size: 18px;
}

.music-card {
    background: rgba(255, 255, 255, 0.08);
    padding: 35px;
    border-radius: 20px;
    border: 1px solid rgba(192, 132, 252, 0.5);
    box-shadow: 0 0 25px rgba(168, 85, 247, 0.25);
}

.stButton>button {
    background: linear-gradient(90deg, #7c3aed, #d946ef);
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 260px;
    font-size: 18px;
    border: none;
}

.stDownloadButton>button {
    background: transparent;
    color: white;
    border: 2px solid #a855f7;
    border-radius: 12px;
    height: 3em;
    width: 260px;
    font-size: 18px;
}

.stSuccess {
    background-color: rgba(34, 197, 94, 0.18);
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.markdown("## 🎼 Options")
genre = st.sidebar.selectbox("Select Genre", ["Classical", "Piano", "Melody"])

st.sidebar.markdown("---")
st.sidebar.info("🎵 This AI model generates music using LSTM neural networks trained on MIDI datasets.")

st.markdown("<h1>🎵 AI Music Generator</h1>", unsafe_allow_html=True)

st.markdown(
    "<p>Generate AI-based music using an LSTM model trained on MIDI datasets.</p>",
    unsafe_allow_html=True
)

st.markdown(f"<p>Selected Genre: <b>{genre}</b></p>", unsafe_allow_html=True)

st.markdown("---")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    

    st.subheader("▶️ Generated Music")

    if st.button("✨ Generate Music"):
        os.system("python generate.py")
        st.success("🎶 AI-generated music created successfully!")

    if os.path.exists("generated_music.mid"):
        with open("generated_music.mid", "rb") as file:
            st.download_button(
                label="⬇️ Download Generated Music",
                data=file,
                file_name="generated_music.mid",
                mime="audio/midi"
            )

        st.caption("Download the generated MIDI music file.")
        st.success("🎶 AI-generated music file found!")
    else:
        st.warning("No generated music found. Click Generate Music first.")

    

st.markdown("<p>Made with ❤️ using Streamlit and TensorFlow</p>", unsafe_allow_html=True)