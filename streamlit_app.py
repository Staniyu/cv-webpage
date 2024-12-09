import streamlit as st

st.title(" My new app🔥" , anchor=False)
st.header("Ich bin eine neue Überschrift👻" , anchor=False)
st.subheader("Noch eine kleiner Überschrift😼" , anchor=False)
st.write("das ist meine streamlit app")

st.markdown("<p>Ich bin ein Text </p>" , unsafe_allow_html=True)

st.header("IT-Kompetenz", anchor=False, divider="blue")

st.write("""
            - 🌐Webentwicklung: Fundierte Grundkenntnisse in HTML, CSS und Streamlit (Fullstack-Framework)
            - 🤖Programmierung: Praktische Erfahrung in Python, Entwicklung kleiner Anwendungen und Skripte
            - 🏢Office-Suite: Versierter Umgang mit Microsoft Word, Excel und PowerPoint
            - 🚧Eigene Projekte: Konzeption und Umsetzung verschiedener Projekte inklusive Hosting
            - 🏫Schulprojekte: Erstellung datenbasierter Präsentationen und interaktiver Tabellenkalkulationen
            """, unsafe_allow_html=True)

st.header("Schulbildung", anchor=False, divider="blue")

st.subheader("Fachmittelschule Schaumburgergasse, Wien")

st.write("""
        - 🎒Schwerpunkt: Intensive IT-Spezialisierung, Fokus auf modernen Webtechnologien und Wirtschaft
        - 🎒Zeitraum: September 2024 - Juli 2025
        - 🎒Derzeitiger Notenschnitt: 1,5
         """, unsafe_allow_html=True)

st.subheader("Mittelschule Kayniongasse, Wien")

st.write("""
        - ⏱️Zeitraum: September 2020 – Juli 2024
        - ⏱️Abschluss-Notendurchschnitt: 1,7
         """, unsafe_allow_html=True)

st.header("Arbeitserfahrung" , anchor=False, divider="blue")

st.write("""
        - 🈺Berufspraktische Tage 1: Bei XYZ von 18. bis 22. Nov. 2024
        - 🈺Berufspraktische Tage 2: Bei XYZ von 24. bis 28. Feb. 2025
         """, unsafe_allow_html=True)

st.header("Zusätzliche Qualifikationen" , anchor=False , divider="blue")

st.write("""
        - ⏩Schnelle Auffassungsgabe für neue Softwareanwendungen und Technologien
        - ⏫Großes Interesse an der kontinuierlichen Weiterentwicklung im IT-Bereich
        - 🥇Teamfähigkeit und Kommunikationsstärke bei gemeinsamen Coding-Projekten
         """, unsafe_allow_html=True)

st.header("Interessen und Hobbys" , anchor=False , divider="blue")

st.write("""
        - ⚽Fußball: Mitglied in einem Fußball-Klub
        - 📖Lesen: Begeisterte Leserin verschiedenster Literatur
        - ♟️Schach: Engagiert im Schachklub
         """, unsafe_allow_html=True)