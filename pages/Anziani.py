"""
File: StatiX_AnzianiStreamlit.py
Author: Chiara Tirendi
Date: 13/11/2023
Description: Grafici statistiche anziani
"""

#importa moduli e pacchetti di python
import numpy as np
import pandas as pd
from pandas import DataFrame
from matplotlib import pyplot as plt
import streamlit as st
import plotly as px
import squarify
import seaborn as sb
import altair as alt

#importa i db dai csv
RapportoAbAnzS= pd.read_csv("./Destinazione/CSV/RapportoAbAnz.csv")
AnzianiQuartS= pd.read_csv("./Destinazione/CSV/AnzianiQuart.csv")
MF65S = pd.read_csv("./Destinazione/CSV/MF65.csv")
MQuartieri65S = pd.read_csv("./Destinazione/CSV/MQuartieri65.csv")
FQuartieri65S = pd.read_csv("./Destinazione/CSV/FQuartieri65.csv")
MFQuartieri65S = pd.read_csv("./Destinazione/CSV/MFQuartieri65.csv")
RapportoStrAnzS = pd.read_csv("./Destinazione/CSV/RapportoStrAnz.csv")
StranieriQuart65S = pd.read_csv("./Destinazione/CSV/StranieriQuart65.csv")

#set pagina su tutta l'ampiezza
st.set_page_config(layout="wide")
#set titolo applicazione
st.title("StatiX")
st.write("App per la visualizzazione dei dati statistici relativi al Comune di Lecco (minori, adulti e over 65 anni, scuole e asili)")
#crea il markdown minori
st.markdown("# Adulti")
#crea la sidebar con i markdown
st.sidebar.markdown("# Adulti")

#colori
colorQuart= ["#FF0066", "#FF6699", "#CC3366", "#993333", "#CC3333", "#990000", "#660000", "#993300", "#CC6633", "#CC9933", "#FFCC33", "#999900", "#666600", "#669900", "#339966"]
colorMF= ["#33CCCC", "#FF0066"]
colorFasce= ["#D69EC4", "#B772A1", "#C42B91", "#912F70", "#990066"]
colorFasceSTR= ["#C0E8FB", "#6ECFF6", "#0093D7", "#0072B9", "#214297"]

#contenitore prima riga
primaRiga = st.container()
with primaRiga:
    #configura numero colonne
    colpr1, colpr2 = st.columns(2, gap="medium")
    with colpr1:
        #GRAFICO RAPPORTO TRA ANZIANI E TOTALE ABITANTI
        st.subheader("Rapporto (%) tra over 65 e totale abitanti")
        st.write(RapportoAbAnzS)
        #st.bar_chart(RapportoAbAnzS, x="Tipologia", y="Percentuale", color="#990066")
        # crea grafico
        RAAN = alt.Chart(RapportoAbAnzS).mark_bar(color="#990066").encode(alt.X("Tipologia"), alt.Y("Percentuale"))
        # label
        textRAAN = RAAN.mark_text(align="center", baseline="bottom").encode(text="Percentuale")
        # stampa grafico + label
        st.altair_chart(RAAN + textRAAN, use_container_width=True)

    with colpr2:
    #GRAFICO DISTRIBUZIONE ANZIANI NEI QUARTIERI
        st.subheader("Distribuzione (%) degli over 65 nei quartieri")
        ANQ = alt.Chart(AnzianiQuartS).mark_line(point=alt.OverlayMarkDef(filled=True, fill="#990066"),
                                                strokeWidth=2, color="#990066"
                                                ).encode(alt.X("Quartiere"), alt.Y("Percentuale")).interactive()

        text = ANQ.mark_text(
            align="center",
            baseline="middle",
            dy=-7).encode(text="Percentuale")
        # stampa grafico + label
        st.altair_chart(ANQ+text, use_container_width=True)
        with st.expander("Tabella distribuzione (%) over 65 nei quartieri"):
            st.write(AnzianiQuartS)

secondaRiga = st.container()
with secondaRiga:
    colsr1, colsr2, colsr3, colsr4 = st.columns(4, gap="large")
    with colsr1:
        # GRAFICO MASCHI E FEMMINE
        st.subheader("Maschi e Femmine")
        st.write(MF65S)
        figMF, axesMF = plt.subplots()
        axesMF.pie(x=MF65S["Percentuale"], autopct='%1.1f%%', pctdistance=1.24, colors=colorMF,
                   wedgeprops={"edgecolor": "white", "linewidth": 1})
        axesMF.axis('equal')  # Rispetto dell'aspect ratio
        axesMF.legend(ncol=1, labels=MF65S["Sesso"], title="Legenda", bbox_to_anchor=(1, 1), loc="upper left")
        st.pyplot(figMF, use_container_width=True)
    with colsr2:
        # GRAFICO DISTRIBUZIONE FEMMINE NEI QUARTIERI
        st.subheader("Distribuzione (%) delle femmine nei quartieri")
        FANQ = alt.Chart(FQuartieri65S).mark_line(point=alt.OverlayMarkDef(filled=True, fill="#FF0066"),
                                                    strokeWidth=2, color="#FF0066"
                                                    ).encode(alt.X("Quartiere"),
                                                             alt.Y("Percentuale femmine")).interactive()

        text = FANQ.mark_text(
            align="center",
            baseline="middle",
            dy=-7).encode(text="Percentuale femmine")
        # stampa grafico + label
        st.altair_chart(FANQ+text, use_container_width=True)
    with colsr3:
        # GRAFICO DISTRIBUZIONE MASCHI NEI QUARTIERI
        st.subheader("Distribuzione (%) dei maschi nei quartieri")
        MANQ = alt.Chart(MQuartieri65S).mark_line(point=alt.OverlayMarkDef(filled=True, fill="#33CCCC"),
                                                    strokeWidth=2, color="#33CCCC"
                                                    ).encode(alt.X("Quartiere"),
                                                             alt.Y("Percentuale maschi")).interactive()

        text = MANQ.mark_text(
            align="center",
            baseline="middle",
            dy=-7).encode(text="Percentuale maschi")
        # stampa grafico + label
        st.altair_chart(MANQ+text, use_container_width=True)
    with colsr4:
        # GRAFICO RAPPORTO MASCHI E FEMMINE NEI QUARTIERI
        st.subheader("Rapporto (%) maschi e femmine nei quartieri")
        MFQAN1 = alt.Chart(MFQuartieri65S).mark_line(point=alt.OverlayMarkDef(filled=True, fill="#33CCCC"),
                                                    strokeWidth=2, color="#33CCCC"
                                                    ).encode(alt.X("Quartiere"),
                                                             alt.Y("Percentuale maschi")).interactive()
        MFQAN2 = alt.Chart(MFQuartieri65S).mark_line(point=alt.OverlayMarkDef(filled=True, fill="#FF0066"),
                                                    strokeWidth=2, color="#FF0066"
                                                    ).encode(alt.X("Quartiere"),
                                                             alt.Y("Percentuale femmine")).interactive()
        # stampa grafico + label
        st.altair_chart(MFQAN1 + MFQAN2, use_container_width=True)
        # figMFQAN = px.bar(MFQuartieri65S, x="Quartiere", y=["Percentuale maschi", "Percentuale femmine"],
        #                 color_discrete_sequence=(colorMF), height=350,
        #                 labels={"value": "Percentuale"}, text_auto=True)
        # figMFQAN.update_layout(legend=dict(x=0, y=2), legend_orientation="h")
        # figMFQAN.update_xaxes(tickangle=270)
        # st.plotly_chart(figMFQAN, use_container_width=True)
terzaRiga = st.container()
with terzaRiga:
    #configura numero colonne
    coltz1, coltz2 = st.columns(2, gap="medium")
    with coltz1:
        #GRAFICO RAPPORTO TRA STRANIERI E TOTALE MINORI
        st.subheader("Rapporto (%) tra stranieri e totale adulti")
        st.write(RapportoStrAnzS)
        # crea grafico
        RSTRAN = alt.Chart(RapportoStrAnzS).mark_bar(color="#3399FF").encode(alt.X("Tipologia"), alt.Y("Percentuale"))
        # label
        textRSTRAN = RSTRAN.mark_text(align="center", baseline="bottom").encode(text="Percentuale")
        # stampa grafico + label
        st.altair_chart(RSTRAN + textRSTRAN, use_container_width=True)

    with coltz2:
        #DISTRIBUZIONE DEGLI STRANIERI NEI QUARTIERI
        st.subheader("Distribuzione (%) degli stranieri nei quartieri")
        SANQ = alt.Chart(StranieriQuart65S).mark_line(point=alt.OverlayMarkDef(filled=True, fill="#3399FF"),
                                                        strokeWidth=2, color="#3399FF"
                                                        ).encode(alt.X("Quartiere"),
                                                                 alt.Y("Percentuale")).interactive()

        text = SANQ.mark_text(
            align="center",
            baseline="middle",
            dy=-7).encode(text="Percentuale")
        # stampa grafico + label
        st.altair_chart(SANQ+text, use_container_width=True)

        with st.expander("Tabella distribuzione (%) degli stranieri nei quartieri"):
            st.write(StranieriQuart65S)
