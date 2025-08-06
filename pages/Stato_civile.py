"""
File: Stato_civileStreamlit.py
Author: Chiara Tirendi
Date: 13/11/2023
Description: Grafici statistiche stato civile
"""

#importa moduli e pacchetti di python
import numpy as np
import pandas as pd
from pandas import DataFrame
from matplotlib import pyplot as plt
import streamlit as st
import plotly.express as px
import squarify
import altair as alt
import seaborn as sb



RapportoAbSCivS=pd.read_csv("./Destinazione/CSV/RapportoAbSCiv.csv")
SLEtaS=pd.read_csv("./Destinazione/CSV/SLEta.csv")
SLEta017GS=pd.read_csv("./Destinazione/CSV/SLEta017G.csv")
SLEta1864GS=pd.read_csv("./Destinazione/CSV/SLEta1864G.csv")
SLEta65GS=pd.read_csv("./Destinazione/CSV/SLEta65G.csv")
QuartieriSLS=pd.read_csv("./Destinazione/CSV/QuartieriSL.csv")
SoloQuartieriS=pd.read_csv("./Destinazione/CSV/SoloQuartieri.csv")


#set pagina su tutta l'ampiezza
st.set_page_config(layout="wide")
#set titolo applicazione
st.title("StatiX")
st.write("App per la visualizzazione dei dati statistici relativi al Comune di Lecco (minori, adulti e over 65 anni, scuole e asili) - statistiche a cura dell'ufficio SIT - aggiornate il 31/07/2025")
#crea il markdown minori
st.markdown("# Stato civile libero")
st.write("Per stato civile libero si intende: nubili/celibi, vedovi, divorziati")

#crea la sidebar con i markdown
st.sidebar.markdown("# Stato civile libero")

colorFasce= ["#6b007b", "#70B0E0","#9B0065"]


primaRiga = st.container()
with primaRiga:
    #configura numero colonne
    colpr1, colpr2 = st.columns(2, gap="large")
    with colpr1:
        #GRAFICO RAPPORTO TRA ABITANI DI STATO LIBERO E TOTALE ABITANTI
        st.subheader("Rapporto (%) tra abitanti stato libero e totale abitanti")
        st.write(RapportoAbSCivS)
        #crea grafico
        RAB= alt.Chart(RapportoAbSCivS).mark_bar(color="#990066").encode(alt.X("Tipologia"), alt.Y("Percentuale"))
        #label
        textRAB = RAB.mark_text(align="center", baseline="bottom").encode(text="Percentuale")
        #stampa grafico + label
        st.altair_chart(RAB+textRAB, use_container_width=True)
    with colpr2:
        #GRAFICO RAPPORTO TRA STATO E FASCE DI ETA'
        st.subheader("Rapporto (%) tra abitanti stato libero e fasce di età")
        st.write(SLEtaS)
        figSLE, axesSLE = plt.subplots()
        axesSLE.pie(x=SLEtaS["Percentuale"], autopct='%1.1f%%', pctdistance=1.24, colors= colorFasce,wedgeprops={"edgecolor": "white", "linewidth": 1})
        axesSLE.axis('equal')  # Rispetto dell'aspect ratio
        axesSLE.legend(ncol=1, labels=SLEtaS["Fascia"], title="Legenda", bbox_to_anchor=(1, 1), loc="upper left")
        st.pyplot(figSLE, use_container_width=True)

secondaRiga = st.container()
with secondaRiga:
    #configura numero colonne
    colsc1, colsc2, colsc3 = st.columns(3, gap="medium")
    with colsc1:
        # GRAFICO STATO LIBERO DA 0 A 17 ANNI
        st.subheader("Stato libero da 0 a 17 anni")
        figSL017 = px.bar(SLEta017GS, x="Stato civile", y="Percentuale", color="Stato civile", barmode='group', height=400,
                         text="Percentuale", color_discrete_sequence=("#B6B0FF", "#70B0E0", "#9B0065"))
        figSL017.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
        figSL017.update_layout(barmode="stack")
        figSL017.update_xaxes(tickangle=90)
        st.plotly_chart(figSL017, use_container_width=True)
        with st.expander("Tabella stato libero da 0 a 17 anni"):
            st.write(SLEta017GS)
    with colsc2:
        # GRAFICO STATO LIBERO DA 18 A 64 ANNI
        st.subheader("Stato libero da 18 a 64 anni")
        figSL1864 = px.bar(SLEta1864GS, x="Stato civile", y="Percentuale", color="Stato civile", barmode='group',
                          height=400,
                          text="Percentuale", color_discrete_sequence=("#B6B0FF", "#70B0E0", "#9B0065"))
        figSL1864.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
        figSL1864.update_layout(barmode="stack")
        figSL1864.update_xaxes(tickangle=90)
        st.plotly_chart(figSL1864, use_container_width=True)
        with st.expander("Tabella stato libero da 18 a 64 anni"):
            st.write(SLEta1864GS)
    with colsc3:
        # GRAFICO STATO LIBERO OVER 65 ANNI
        st.subheader("Stato libero over 65 anni")
        figSL65 = px.bar(SLEta65GS, x="Stato civile", y="Percentuale", color="Stato civile", barmode='group',
                          height=400,
                          text="Percentuale", color_discrete_sequence=("#B6B0FF", "#70B0E0", "#9B0065"))
        figSL65.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
        figSL65.update_layout(barmode="stack")
        figSL65.update_xaxes(tickangle=90)
        st.plotly_chart(figSL65, use_container_width=True)
        with st.expander("Tabella stato libero over 65 anni"):
            st.write(SLEta65GS)

terzaRiga = st.container()
with (terzaRiga):
    #configura numero colonne
    coltz1, coltz2 = st.columns(2, gap="medium")
    with coltz1:
        # GRAFICO STATO LIBERO DA 0 A 17 ANNI
        st.subheader("Distribuzione (%) dei minori nei quartieri")
        figQUA = px.bar(QuartieriSLS, x="Quartiere", y="Percentuale", color="Stato civile", labels={"value": "Percentuale"}, height=450,
                           text_auto=True, color_discrete_sequence=("#B6B0FF", "#70B0E0", "#9B0065"))
        figQUA.update_layout(legend=dict(x=0, y=1.2), legend_orientation="h")
        figQUA.update_xaxes(tickangle=270)
        st.plotly_chart(figQUA, use_container_width=True)

        with coltz2:
            # DISTRIBUZIONE FAMIGLIE CON UN SOLO COMPONENTE
            st.subheader("Distribuzione (%) famiglie con un solo componente nei quartieri")

            figFAM1C = px.bar(SoloQuartieriS, x="Quartiere", y=["Percentuale 0-17 anni", "Percentuale 18-64 anni",
                                                                 "Percentuale sopra 65 anni"],
                               color_discrete_sequence=(colorFasce), labels={"value": "Percentuale"}, height=450,
                               text_auto=True)
            # Imposta barmode su "group" per avere colonne affiancate
            figFAM1C.update_layout(barmode="group", bargap=0.1, legend=dict(x=0, y=1.2), legend_orientation="h")

            # Allarga le dimensioni delle barre
            figFAM1C.update_traces(width=0.30)


            figFAM1C.update_xaxes(tickangle=270)
            st.plotly_chart(figFAM1C, use_container_width=True)


