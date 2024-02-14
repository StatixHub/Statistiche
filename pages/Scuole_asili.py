"""
File: Scuole_asiliStreamlit.py
Author: Chiara Tirendi
Date: 13/11/2023
Description: Grafici statistiche scuole e asili
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
import plotly.graph_objects as go


SInfanziaPS = pd.read_csv("../Destinazione/CSV/SInfanziaP.csv")
SPrimariePS = pd.read_csv("../Destinazione/CSV/SPrimarieP.csv")
SSecondarieIGradoPS = pd.read_csv("../Destinazione/CSV/SSecondarieIGradoP.csv")
ISTLecco1S = pd.read_csv("../Destinazione/CSV/ISTLecco1.csv")
ISTLecco2S = pd.read_csv("../Destinazione/CSV/ISTLecco2.csv")
ISTLecco3S = pd.read_csv("../Destinazione/CSV/ISTLecco3.csv")
SoloInfanziaConcS = pd.read_csv("../Destinazione/CSV/SoloInfanziaConc.csv")
SoloPrimariaConcS = pd.read_csv("../Destinazione/CSV/SoloPrimariaConc.csv")
SoloSecondariaConcS = pd.read_csv("../Destinazione/CSV/SoloSecondariaConc.csv")
RapportoScuoleStaParIS = pd.read_csv("../Destinazione/CSV/RapportoScuoleStaParI.csv")
RapportoScuoleStaParPS = pd.read_csv("../Destinazione/CSV/RapportoScuoleStaParP.csv")
RapportoScuoleStaParSS = pd.read_csv("../Destinazione/CSV/RapportoScuoleStaParS.csv")
RapportoParitarieStataliS = pd.read_csv("../Destinazione/CSV/RapportoParitarieStatali.csv")
RapportoAsiloMinoriS = pd.read_csv("../Destinazione/CSV/RapportoAsiloMinori.csv")
ANAmmessiS = pd.read_csv("../Destinazione/CSV/ANAmmessi.csv")
ANAttesaS = pd.read_csv("../Destinazione/CSV/ANAttesa.csv")

#set pagina su tutta l'ampiezza
st.set_page_config(layout="wide")
#set titolo applicazione
st.title("StatiX")
st.write("App per la visualizzazione dei dati statistici relativi al Comune di Lecco (minori, adulti e over 65 anni, scuole e asili)")
#crea il markdown minori
st.markdown("# Scuole e asili")
st.subheader("***Scuole***")
#crea la sidebar con i markdown
st.sidebar.markdown("# Scuole e asili")

colorFasce= ["#6b007b", "#70B0E0","#9B0065", "#B6B0FF"]
colorFasceDue= ["#70B0E0","#486871"]

primaRiga = st.container()
with primaRiga:
    #configura numero colonne
    colpr1, colpr2, colpr3 = st.columns(3, gap="medium")
    with colpr1:
        # GRAFICO ISCRITTI ALLA SCUOLA PER L'INFANZIA STATALE
        st.subheader("Iscritti (%) alle scuole per l'infanzia statali")
        # crea grafico
        SoloINFConc = alt.Chart(SoloInfanziaConcS).mark_bar(color="#70B0E0").encode(alt.X("PLESSO"), alt.Y("Percentuale"))
        # label
        textSoloINFConc = SoloINFConc.mark_text(align="center", baseline="bottom").encode(text="Percentuale")

        # stampa grafico + label
        st.altair_chart(SoloINFConc+textSoloINFConc, use_container_width=True)
        with st.expander("Tabella iscritti alle scuole per l'infanzia statali"):
            st.write(SoloInfanziaConcS )
    with colpr2:
        # GRAFICO ISCRITTI ALLA SCUOLA PRIMARIA STATALE
        st.subheader("Iscritti (%) alle scuole primarie statali")

        SoloPRIMConc= alt.Chart(SoloPrimariaConcS).mark_bar(color="#9B0065").encode(alt.X("PLESSO"), alt.Y("Percentuale"))
        # label
        textSoloPRIMConc = SoloPRIMConc.mark_text(align="center", baseline="bottom").encode(text="Percentuale")
        # stampa grafico + label
        st.altair_chart(SoloPRIMConc+textSoloPRIMConc, use_container_width=True)
        with st.expander("Tabella iscritti alle scuole primarie statali"):
            st.write(SoloPrimariaConcS)
    with colpr3:
        # GRAFICO ISCRITTI ALLA SCUOLA SECONDARIA STATALE
        st.subheader("Iscritti (%) alle scuole secondarie di I grado statali")
        # crea grafico


        SoloSECConc = alt.Chart(SoloSecondariaConcS).mark_bar(color="#B6B0FF").encode(alt.X("PLESSO"), alt.Y("Percentuale"))
        # label
        textSoloSECConc = SoloSECConc.mark_text(align="center", baseline="bottom").encode(text="Percentuale")
        # stampa grafico + label
        st.altair_chart(SoloSECConc+textSoloSECConc, use_container_width=True)
        with st.expander("Tabella iscritti alle scuole secondarie di I grado statali"):
            st.write(SoloSecondariaConcS)

