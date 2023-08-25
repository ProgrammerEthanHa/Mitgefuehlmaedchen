import streamlit as st
import pandas as pd
import altair as alt

st.header("Inwiefern stimmst du der Aussage 'Es macht mich traurig, wenn es anderen Kindern schlecht geht' zu? - Mädchen")
st.subheader("")

source = pd.DataFrame({
        'Anteil(%)': [3, 26, 71],
        ' ': ["Stimmt nicht", "Stimmt nur ein bisschen", "Stimmt"]
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x=' :O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Basis n=618; Deutschland; 2018 - 2019
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle:  V. Pawlik")