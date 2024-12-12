import streamlit as st

left, right = st.columns(2)

left.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSkGGYkd6sRsHNOMvn3NpC1LQf1sjFjuGZLXw&s")

right.header("Stanislaw Berndl")

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
        - 🎮video spiele spielen: einer der Hauptsachen die ich in meiner Freizeit tuhe
        - 📖Lesen: tuhe ich in der Freizeit
        - 🚶raus gehen: Zum sozial bleiben
        - 🍳Kochkünste
         """, unsafe_allow_html=True)