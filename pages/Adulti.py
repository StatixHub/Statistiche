"""
File: StatiX8_AdultiStreamlit.py
Author: Chiara Tirendi
Date: 13/11/2023
Description: Grafici statistiche adulti
"""

#importa moduli e pacchetti di python
import numpy as np
import pandas as pd
from pandas import DataFrame
from matplotlib import pyplot as plt
import streamlit as st
import plotly.express as px
import squarify
import seaborn as sb
import altair as alt
alt.renderers.set_embed_options(renderer="svg")


#importa i db dai csv
RapportoAbAduS = pd.read_csv("./Destinazione/CSV/RapportoAbAdu.csv")
AdultiQuartS = pd.read_csv("./Destinazione/CSV/AdultiQuart.csv")
MF1864S = pd.read_csv("./Destinazione/CSV/MF1864.csv")
MQuartieri1864S = pd.read_csv("./Destinazione/CSV/MQuartieri1864.csv")
FQuartieri1864S = pd.read_csv("./Destinazione/CSV/FQuartieri1864.csv")
MFQuartieri1864S = pd.read_csv("./Destinazione/CSV/MFQuartieri1864.csv")
RapportoStrAduS = pd.read_csv("./Destinazione/CSV/RapportoStrAdu.csv")
StranieriQuart1864S = pd.read_csv("./Destinazione/CSV/StranieriQuart1864.csv")

#set pagina su tutta l'ampiezza
st.set_page_config(layout="wide")
#set titolo applicazione
st.title("StatiX")
st.write("App per la visualizzazione dei dati statistici relativi al Comune di Lecco (minori, adulti e over 65 anni, scuole e asili) - statistiche a cura dell'ufficio SIT - aggiornate il 30/06/2025")
#crea il markdown adulti
st.markdown("# Adulti")
#crea la sidebar con i markdown
st.sidebar.markdown("# Adulti")

#colori
colorQuart= ["#FF0066", "#FF6699", "#CC3366", "#993333", "#CC3333", "#990000", "#660000", "#993300", "#CC6633", "#CC9933", "#FFCC33", "#999900", "#666600", "#669900", "#339966"]
colorMF= ["#FF0066", "#33CCCC"]
colorFasce= ["#D69EC4", "#B772A1", "#C42B91", "#912F70", "#990066"]
colorFasceSTR= ["#C0E8FB", "#6ECFF6", "#0093D7", "#0072B9", "#214297"]

#contenitore prima riga
primaRiga = st.container()
with primaRiga:
    #configura numero colonne
    colpr1, colpr2 = st.columns(2, gap="medium")
    with colpr1:
        df = pd.DataFrame({'Tipologia': ['A', 'B', 'C'], 'Percentuale': [10, 20, 30]})

    chart = alt.Chart(df).mark_bar(color="#FF3366").encode(
        x=alt.X('Tipologia:N'),
        y=alt.Y('Percentuale:Q')
    )

    st.altair_chart(chart, use_container_width=True)

    st.write("Tabella dati")
    st.write(df)

    with colpr2:
    #GRAFICO DISTRIBUZIONE ADULTI NEI QUARTIERI
        st.subheader("Distribuzione (%) degli adulti nei quartieri")
        # crea grafico
        ADQ = alt.Chart(AdultiQuartS).mark_bar(color="#990066").encode(alt.X("Quartiere"),
                                                                        alt.Y("Percentuale")).interactive()
        #PRECEDENTE GRAFICO A LINEA
        # ADQ = alt.Chart(AdultiQuartS).mark_line(point=alt.OverlayMarkDef(filled=True, fill="#990066"),
        #                                      strokeWidth=2, color="#990066"
        #                                      ).encode(alt.X("Quartiere"), alt.Y("Percentuale")).interactive()

        text = ADQ.mark_text(
            align="center",
            baseline="middle",
            dy=-7).encode(text="Percentuale")
        # stampa grafico + label
        st.altair_chart(ADQ+text, use_container_width=True)
        with st.expander("Tabella distribuzione (%) adulti nei quartieri"):
            st.write(AdultiQuartS)






secondaRiga = st.container()
with secondaRiga:
    colsr1, colsr2, colsr3, colsr4 = st.columns(4, gap="large")
    with colsr1:
        # GRAFICO MASCHI E FEMMINE
        st.subheader("Maschi e Femmine")
        st.write(MF1864S)
        figMF, axesMF = plt.subplots()
        axesMF.pie(x=MF1864S["Percentuale"], autopct='%1.1f%%', pctdistance=1.24, colors=colorMF,
                   wedgeprops={"edgecolor": "white", "linewidth": 1})
        axesMF.axis('equal')  # Rispetto dell'aspect ratio
        axesMF.legend(ncol=1, labels=MF1864S["Sesso"], title="Legenda", bbox_to_anchor=(1, 1), loc="upper left")
        st.pyplot(figMF, use_container_width=True)
    with colsr2:
        # GRAFICO DISTRIBUZIONE FEMMINE NEI QUARTIERI
        st.subheader("Distribuzione (%) delle femmine nei quartieri")
        FADQ = alt.Chart(FQuartieri1864S).mark_bar(color="#FF0066").encode(alt.X("Quartiere"),
                                                                           alt.Y("Percentuale femmine")).interactive()

        text = FADQ.mark_text(
            align="center",
            baseline="middle",
            dy=-7).encode(text="Percentuale femmine")
        # stampa grafico + label
        st.altair_chart(FADQ+text, use_container_width=True)
    with colsr3:
        # GRAFICO DISTRIBUZIONE MASCHI NEI QUARTIERI
        st.subheader("Distribuzione (%) dei maschi nei quartieri")
        MADQ = alt.Chart(MQuartieri1864S).mark_bar(color="#33CCCC").encode(alt.X("Quartiere"),
                                                                           alt.Y("Percentuale maschi")).interactive()

        text = MADQ.mark_text(
            align="center",
            baseline="middle",
            dy=-7).encode(text="Percentuale maschi")
        # stampa grafico + label
        st.altair_chart(MADQ + text, use_container_width=True)
    with colsr4:
        # GRAFICO RAPPORTO MASCHI E FEMMINE NEI QUARTIERI
        st.subheader("Rapporto (%) maschi e femmine nei quartieri")
        figMFQ1864 = px.bar(MFQuartieri1864S, x="Quartiere",
                           y=["Percentuale maschi", "Percentuale femmine"],
                           color_discrete_sequence=(colorMF), labels={"value": "Percentuale"}, text_auto=True)
        figMFQ1864.update_layout(legend=dict(x=0, y=1.3), legend_orientation="h")
        figMFQ1864.update_xaxes(tickangle=270)

        st.plotly_chart(figMFQ1864, use_container_width=True)

terzaRiga = st.container()
with terzaRiga:
    #configura numero colonne
    coltz1, coltz2 = st.columns(2, gap="medium")
    with coltz1:
        #GRAFICO RAPPORTO TRA STRANIERI E TOTALE MINORI
        st.subheader("Rapporto (%) tra stranieri e totale adulti")
        st.write(RapportoStrAduS)
        # crea grafico
        RSTRAD = alt.Chart(RapportoStrAduS).mark_bar(color="#3399FF").encode(alt.X("Tipologia"), alt.Y("Percentuale"))
        # label
        textRSTRAD = RSTRAD.mark_text(align="center", baseline="bottom").encode(text="Percentuale")
        # stampa grafico + label
        st.altair_chart(RSTRAD + textRSTRAD, use_container_width=True)


    with coltz2:
        #DISTRIBUZIONE DEGLI STRANIERI NEI QUARTIERI
        st.subheader("Distribuzione (%) degli stranieri nei quartieri")
        SADQ = alt.Chart(StranieriQuart1864S).mark_bar(color="#3399FF").encode(alt.X("Quartiere"),
                                                                       alt.Y("Percentuale")).interactive()
        #VECCHIO GRAFICO IN LINEA
        # SADQ = alt.Chart(StranieriQuart1864S).mark_line(point=alt.OverlayMarkDef(filled=True, fill="#3399FF"),
        #                                             strokeWidth=2, color="#3399FF"
        #                                             ).encode(alt.X("Quartiere"),
        #                                                      alt.Y("Percentuale")).interactive()

        text = SADQ.mark_text(
            align="center",
            baseline="middle",
            dy=-7).encode(text="Percentuale")
        # stampa grafico + label
        st.altair_chart(SADQ + text, use_container_width=True)
        with st.expander("Tabella distribuzione (%) degli stranieri nei quartieri"):
            st.write(StranieriQuart1864S)



















