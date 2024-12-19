import streamlit as st
from pathlib import Path

st.markdown("<style> .stAppHeader {display:none;} ul {list-style-type: none; } </style>", unsafe_allow_html=True)

def get_file_content_as_bytes(file_path):
    with open(file_path, "rb") as file:
        return file.read()

# Pfad zur PDF-Datei
file_path = 'Lebenslaufstani.pdf'

# Lese den Inhalt der PDF-Datei als Bytes
file_bytes = get_file_content_as_bytes(file_path)

left, right = st.columns(2)

left.image("images.jpg" , width=250)

with right:
        st.markdown("""
                <h3>Stanislaw Berndl</h3>
            <em>Ich finde KI ganz cool weil es immer für einen da ist.
                und es mir auch oft hilft :)</em>
               """, unsafe_allow_html=True)

        st.download_button(
                label="📄 Download Lebenslauf",
                data=file_bytes,
                file_name=file_path,
                mime='application/pdf'
    )
        st.write("📩", "stanislaw05042005@gmail.com")

st.header("IT-Kompetenz", anchor=False, divider="violet")

st.write("""
        - 🔝Office: Guter Umgang mit Word, Powerpoint und Excel
        - 💯Programmieren: Basics auswendig gelernt
        - 🏫Schule: Fach Bereich IT mit positivem Erfolg
        - 🤖Programmier Sprachen: HTML, CSS und Python
         
            """, unsafe_allow_html=True)

st.header("Schulbildung", anchor=False, divider="violet")

st.subheader("Fachmittelschule Schaumburgergasse, Wien")

st.write("""
        - 🐍Schwerpunkt: Intensive IT-Spezialisierung, Fokus auf modernen Webtechnologien und Wirtschaft
        - ⏱️Zeitraum: September 2024 - Juli 2025
         """, unsafe_allow_html=True)

st.subheader("MSI Wiesberggasse, Wien")

st.write("""
        - ⏱️Zeitraum: Februar 2024 – Juli 2024
         """, unsafe_allow_html=True)

st.subheader("Gymnasium Rosasgasse, Wien")

st.write("""
        - ⏱️Zeitraum: september 2020 – jänner 2024
         """, unsafe_allow_html=True)


st.header("Arbeitserfahrung" , anchor=False, divider="violet")

st.write("""
        - 🈺Berufspraktische Tage 1: Himmelblau Architektur 1120
        - 🈺Berufspraktische Tage 2: H&M Auhof
         """, unsafe_allow_html=True)

st.header("Skills", anchor=False, divider="violet")

st.subheader("Soft Skills")

st.write("""
        - 🛡️Leicht verständlich
        - 🤼Teamarbeit
        - ⌛Pünktlich
        - 🙂Freundlich
        - ❗Konzetriert
         """)

st.subheader("Sprachkenntnise")

st.write("""
                           - Russisch in Wort und Schrift
                           - Ukrainisch in Wort und Schrift
                           - Polnisch in Wort
                           - Deutsch in Wort und Schrift
                           - English in Wort und Schrift
                        
         """)





st.header("Interessen und Hobbys" , anchor=False , divider="violet")

st.write("""
        - 🎮video spiele spielen: einer der Haupt Sachen die ich in meiner Freizeit tuhe
        - 📖Lesen: tuhe ich in der Freizeit
        - 🚶raus gehen: Zum sozial bleiben
        - 🍳Kochkünste
         """, unsafe_allow_html=True)