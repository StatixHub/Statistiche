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



SInfanziaPS = pd.read_csv("./Destinazione/CSV/SInfanziaP.csv")
SPrimariePS = pd.read_csv("./Destinazione/CSV/SPrimarieP.csv")
SSecondarieIGradoPS = pd.read_csv("./Destinazione/CSV/SSecondarieIGradoP.csv")
ISTLecco1S = pd.read_csv("./Destinazione/CSV/ISTLecco1.csv")
ISTLecco2S = pd.read_csv("./Destinazione/CSV/ISTLecco2.csv")
ISTLecco3S = pd.read_csv("./Destinazione/CSV/ISTLecco3.csv")
SoloInfanziaConcS = pd.read_csv("./Destinazione/CSV/SoloInfanziaConc.csv")
SoloPrimariaConcS = pd.read_csv("./Destinazione/CSV/SoloPrimariaConc.csv")
SoloSecondariaConcS = pd.read_csv("./Destinazione/CSV/SoloSecondariaConc.csv")
RapportoScuoleStaParIS = pd.read_csv("./Destinazione/CSV/RapportoScuoleStaParI.csv")
RapportoScuoleStaParPS = pd.read_csv("./Destinazione/CSV/RapportoScuoleStaParP.csv")
RapportoScuoleStaParSS = pd.read_csv("./Destinazione/CSV/RapportoScuoleStaParS.csv")
RapportoParitarieStataliS = pd.read_csv("./Destinazione/CSV/RapportoParitarieStatali.csv")
RapportoAsiloMinoriS = pd.read_csv("./Destinazione/CSV/RapportoAsiloMinori.csv")
ANAmmessiS = pd.read_csv("./Destinazione/CSV/ANAmmessi.csv")
ANAttesaS = pd.read_csv("./Destinazione/CSV/ANAttesa.csv")

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
        #GRAFICO ISCRITTI ALLA SCUOLA DELL'INFANZIA
        st.subheader("Iscritti (%) alle scuole dell'infanzia paritarie")
        # crea grafico
        SIPS = alt.Chart(SInfanziaPS).mark_bar(color="#70B0E0").encode(alt.X("PLESSO"), alt.Y("Percentuale"))
        # label
        textSIPS = SIPS.mark_text(align="center", baseline="bottom").encode(text="Percentuale")
        # stampa grafico + label
        st.altair_chart(SIPS + textSIPS, use_container_width=True)
        with st.expander("Tabella iscritti alla scuole dell'infanzia paritarie"):
            st.write(SInfanziaPS)
    with colpr2:
        #GRAFICO ISCRITTI ALLA SCUOLA PRIMARIA PARITARIA
        st.subheader("Iscritti (%) alle scuole primarie paritarie")
        # crea grafico
        SPPS = alt.Chart(SPrimariePS).mark_bar(color="#9B0065").encode(alt.X("PLESSO"), alt.Y("Percentuale"))
        # label
        textSPPS = SPPS.mark_text(align="center", baseline="bottom").encode(text="Percentuale")
        # stampa grafico + label
        st.altair_chart(SPPS + textSPPS, use_container_width=True)
        with st.expander("Tabella iscritti alle scuole primarie paritarie"):
            st.write(SPrimariePS)
    with colpr3:
        # GRAFICO ISCRITTI ALLA SCUOLA SECONDARIA DI SECONDO GRADO
        st.subheader("Iscritti (%) alle scuole secondarie di secondo grado paritarie")
        # crea grafico
        SSIGSP = alt.Chart(SSecondarieIGradoPS).mark_bar(color="#B6B0FF").encode(alt.X("PLESSO"), alt.Y("Percentuale"))
        # label
        textSSIGSP = SSIGSP.mark_text(align="center", baseline="bottom").encode(text="Percentuale")
        # stampa grafico + label
        st.altair_chart(SSIGSP + textSSIGSP, use_container_width=True)
        with st.expander("Tabella iscritti alle scuole secondarie di secondo grado paritarie"):
            st.write(SSecondarieIGradoPS)

secondaRiga = st.container()
with secondaRiga:
    #configura numero colonne
    colsc1, colsc2, colsc3 = st.columns(3, gap="medium")
    with colpr1:
        #GRAFICO ISCRITTI ALL'ISTITUTO COMPRENSIVO LECCO 1
        st.subheader("Iscritti (%) all'Istituto Comprensivo Lecco 1")
        figIST1 = px.bar(ISTLecco1S, x="PLESSO", y="Percentuale", color="TIPOLOGIA", barmode='group', height=400,
                         text="Percentuale", color_discrete_sequence=("#B6B0FF", "#70B0E0", "#9B0065"))
        figIST1.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
        figIST1.update_layout(barmode="stack")
        figIST1.update_xaxes(tickangle=90)
        st.plotly_chart(figIST1, use_container_width=True)
        with st.expander("Tabella iscritti all'Istituto Comprensivo Lecco 1"):
            st.write(ISTLecco1S)
    with colpr2:
        #GRAFICO ISCRITTI ALL'ISTITUTO COMPRENSIVO LECCO 2
        st.subheader("Iscritti (%) all'Istituto Comprensivo Lecco 2")
        figIST2 = px.bar(ISTLecco2S, x="PLESSO", y="Percentuale", color="TIPOLOGIA", barmode='group', height=400,
                         text="Percentuale", color_discrete_sequence=("#B6B0FF", "#70B0E0", "#9B0065"))
        figIST2.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
        figIST2.update_layout(barmode="stack")
        figIST2.update_xaxes(tickangle=90)
        st.plotly_chart(figIST2, use_container_width=True)
        with st.expander("Tabella iscritti all'Istituto Comprensivo Lecco 2"):
            st.write(ISTLecco2S)
    with colpr3:
        #GRAFICO ISCRITTI ALL'ISTITUTO COMPRENSIVO LECCO 3
        st.subheader("Iscritti (%) all'Istituto Comprensivo Lecco 3")
        figIST3 = px.bar(ISTLecco3S, x="PLESSO", y="Percentuale", color="TIPOLOGIA", barmode='group', height=400,
                         text="Percentuale", color_discrete_sequence=("#B6B0FF", "#70B0E0", "#9B0065"))
        figIST3.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
        figIST3.update_layout(barmode="stack")
        figIST3.update_xaxes(tickangle=90)
        st.plotly_chart(figIST3, use_container_width=True)
        with st.expander("Tabella iscritti all'Istituto Comprensivo Lecco 3"):
            st.write(ISTLecco3S)

terzaRiga = st.container()
with terzaRiga:
    #configura numero colonne
    coltz1, coltz2, coltz3 = st.columns(3, gap="medium")
    with coltz1:
        # GRAFICO ISCRITTI ALLA SCUOLA PER L'INFANZIA STATALE
        st.subheader("Iscritti (%) alla scuola per l'infanzia statale")
        # crea grafico
        SoloINFConc = alt.Chart(SoloInfanziaConcS).mark_line(point=alt.OverlayMarkDef(filled=True, fill="#70B0E0"),
                                                     strokeWidth=2.5, color="#70B0E0"
                                                     ).encode(alt.X("PLESSO"), alt.Y("Percentuale")).interactive()
        text = SoloINFConc.mark_text(
            align="center",
            baseline="middle",
            dy=-7).encode(text="Percentuale")
        # stampa grafico + label
        st.altair_chart(SoloINFConc+text, use_container_width=True)
        with st.expander("Tabella iscritti alla scuola per l'infanzia statale"):
            st.write(SoloInfanziaConcS )
    with coltz2:
        # GRAFICO ISCRITTI ALLA SCUOLA PRIMARIA STATALE
        st.subheader("Iscritti (%) alla scuola per l'infanzia statale")
        # crea grafico
        SoloPRIMConc = alt.Chart(SoloPrimariaConcS).mark_line(point=alt.OverlayMarkDef(filled=True, fill="#9B0065"),
                                                             strokeWidth=2.5, color="#9B0065"
                                                             ).encode(alt.X("PLESSO"),
                                                                      alt.Y("Percentuale")).interactive()
        text = SoloPRIMConc.mark_text(
            align="center",
            baseline="middle",
            dy=-7).encode(text="Percentuale")
        # stampa grafico + label
        st.altair_chart(SoloPRIMConc+text, use_container_width=True)
        with st.expander("Tabella iscritti alla scuola per l'infanzia statale"):
            st.write(SoloPrimariaConcS)
    with coltz3:
        # GRAFICO ISCRITTI ALLA SCUOLA SECONDARIA STATALE
        st.subheader("Iscritti (%) alla scuola secondaria di I grado statale")
        # crea grafico
        SoloSECConc = alt.Chart(SoloSecondariaConcS).mark_line(point=alt.OverlayMarkDef(filled=True, fill="#B6B0FF"),
                                                              strokeWidth=2.5, color="#B6B0FF"
                                                              ).encode(alt.X("PLESSO"),
                                                                       alt.Y("Percentuale")).interactive()
        text = SoloSECConc.mark_text(
            align="center",
            baseline="middle",
            dy=-7).encode(text="Percentuale")
        # stampa grafico + label
        st.altair_chart(SoloSECConc+text, use_container_width=True)
        with st.expander("Tabella iscritti alla scuola secondaria di I grado statale"):
            st.write(SoloSecondariaConcS)

quartaRiga = st.container()
with quartaRiga:
    #configura numero colonne
    colqr1, colqr2, colqr3, colqr4 = st.columns(4, gap="medium")
    with colqr1:
        # GRAFICO RAPPORTO TRA SCUOLE PARITARIE E STATALI
        st.subheader("Rapporto iscritti (%) tra le scuole paritarie e quelle statali")
        figRapp, axesRapp = plt.subplots()
        axesRapp.pie(x=RapportoParitarieStataliS["Percentuale"], autopct='%1.1f%%', colors=colorFasce, pctdistance=1.14,
                     wedgeprops={"edgecolor": "white", "linewidth": 1})
        axesRapp.axis('equal')  # Rispetto dell'aspect ratio
        axesRapp.legend(ncol=1, labels=RapportoParitarieStataliS["Tipologia"], title="Legenda", bbox_to_anchor=(1, 1),
                        loc="upper left")
        st.pyplot(figRapp, use_container_width=True)
        with st.expander("Tabella rapporto (%) tra scuole paritarie e statali"):
            st.write(RapportoScuoleStaParIS)

    with colqr2:
        # GRAFICO RAPPORTO TRA SCUOLA INFANZIA STATALE E PARITARIA
        st.subheader("Rapporto (%) tra la scuola infanzia statale e quella paritaria")
        figRapp2, axesRapp2 = plt.subplots()
        axesRapp2.pie(x=RapportoScuoleStaParIS["Percentuale"], autopct='%1.1f%%', colors=colorFasceDue, pctdistance=1.14,
                     wedgeprops={"edgecolor": "white", "linewidth": 1})
        axesRapp2.axis('equal')  # Rispetto dell'aspect ratio
        axesRapp2.legend(ncol=1, labels=RapportoScuoleStaParIS["Tipologia"], title="Legenda", bbox_to_anchor=(1, 1),
                        loc="upper left")
        st.pyplot(figRapp2, use_container_width=True)
        with st.expander("Tabella rapporto (%) tra scuola infanzia statale e paritaria"):
            st.write(RapportoScuoleStaParIS)
    with colqr3:
        # GRAFICO RAPPORTO TRA SCUOLA PRIMARIA STATALE E PARITARIA
        st.subheader("Rapporto (%) tra la scuola primaria statale e quella paritaria")
        figRapp, axesRapp = plt.subplots()
        axesRapp.pie(x=RapportoScuoleStaParPS["Percentuale"], autopct='%1.1f%%', colors=colorFasceDue, pctdistance=1.14,
                     wedgeprops={"edgecolor": "white", "linewidth": 1})
        axesRapp.axis('equal')  # Rispetto dell'aspect ratio
        axesRapp.legend(ncol=1, labels=RapportoScuoleStaParPS["Tipologia"], title="Legenda", bbox_to_anchor=(1, 1),
                        loc="upper left")
        st.pyplot(figRapp, use_container_width=True)
        with st.expander("Tabella rapporto (%) tra scuola primaria statale e paritaria"):
            st.write(RapportoScuoleStaParPS)
    with colqr4:
        # GRAFICO RAPPORTO TRA SCUOLA SECONDARIA DI I GRADO STATALE E PARITARIA
        st.subheader("Rapporto (%) tra scuola sec. di I grado statale e paritaria")
        figRapp, axesRapp = plt.subplots()
        axesRapp.pie(x=RapportoScuoleStaParSS["Percentuale"], autopct='%1.1f%%', colors=colorFasceDue, pctdistance=1.14,
                     wedgeprops={"edgecolor": "white", "linewidth": 1})
        axesRapp.axis('equal')  # Rispetto dell'aspect ratio
        axesRapp.legend(ncol=1, labels=RapportoScuoleStaParSS["Tipologia"], title="Legenda", bbox_to_anchor=(1, 1),
                        loc="upper left")
        st.pyplot(figRapp, use_container_width=True)
        with st.expander("Tabella rapport (%) tra scuola sec. di I grado statale e paritaria"):
            st.write(RapportoScuoleStaParSS)


quintaRiga = st.container()
with quintaRiga:
    colqn1, colqn2 = st.columns(2)
    with colqn1:
        st.subheader("***Asili***")

sestaRiga = st.container()
with sestaRiga:
    #configura numero colonne
    colst1, colst2 = st.columns(2, gap="medium")
    with colst1:
        # GRAFICO RAPPORTO ISCRITTI AL NIDO
        st.subheader("Rapporto (%) iscritti al nido")
        figRapp, axesRapp = plt.subplots()
        axesRapp.pie(x=ANAmmessiS["Percentuale"], autopct='%1.1f%%', colors=colorFasce, pctdistance=1.14,
                     wedgeprops={"edgecolor": "white", "linewidth": 1})
        axesRapp.axis('equal')  # Rispetto dell'aspect ratio
        axesRapp.legend(ncol=1, labels=ANAmmessiS["Nido"], title="Legenda", bbox_to_anchor=(1, 1),
                        loc="upper left")
        st.pyplot(figRapp, use_container_width=True)
        with st.expander("Tabella rapporto iscritti al nido"):
            st.write(ANAmmessiS)

    with colst2:
        # GRAFICO RAPPORTO AMMESSI AL NIDO
        st.subheader("Rapporto (%) ammessi al nido")
        figRapp2, axesRapp2 = plt.subplots()
        axesRapp2.pie(x=ANAttesaS["Percentuale"], autopct='%1.1f%%', colors=colorFasce, pctdistance=1.14,
                     wedgeprops={"edgecolor": "white", "linewidth": 1})
        axesRapp2.axis('equal')  # Rispetto dell'aspect ratio
        axesRapp2.legend(ncol=1, labels=ANAttesaS["Nido"], title="Legenda", bbox_to_anchor=(1, 1),
                        loc="upper left")
        st.pyplot(figRapp2, use_container_width=True)
        with st.expander("Tabella rapporto ammessi al nido"):
            st.write(ANAttesaS)
