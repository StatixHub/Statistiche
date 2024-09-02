"""
File: StatiX8_MinoriStreamlit.py
Author: Chiara Tirendi
Date: 13/11/2023
Description: Grafici statistiche minori
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


#importa i db dai csv
RapportoAbMinS = pd.read_csv("Destinazione/CSV/RapportoAbMin.csv")
TotaleNuoviNatiPDS = pd.read_csv("Destinazione/CSV/TotaleNuoviNatiPD.csv")
NuoviNatiQuarS = pd.read_csv("Destinazione/CSV/NuoviNatiQuar.csv")
Minori017QuartS = pd.read_csv("Destinazione/CSV/Minori017Quart.csv")
FamiglieS= pd.read_csv("Destinazione/CSV/Famiglie.csv")
MF017S = pd.read_csv("Destinazione/CSV/MF017.csv")
MQuartieriS=pd.read_csv("Destinazione/CSV/MQuartieri.csv")
FQuartieriS=pd.read_csv("Destinazione/CSV/FQuartieri.csv")
MFQuartieriS=pd.read_csv("Destinazione/CSV/MFQuartieri.csv")
MF02S=pd.read_csv("Destinazione/CSV/MF02.csv")
MF35S=pd.read_csv("Destinazione/CSV/MF35.csv")
MF69S=pd.read_csv("Destinazione/CSV/MF69.csv")
MF1013S=pd.read_csv("Destinazione/CSV/MF1013.csv")
MF1417S=pd.read_csv("Destinazione/CSV/MF1417.csv")
MinoriFasceS=pd.read_csv("Destinazione/CSV/MinoriFasce.csv")
DistrFasceS=pd.read_csv("Destinazione/CSV/DistrFasce.csv")
RapportoStrMinS= pd.read_csv("Destinazione/CSV/RapportoStrMin.csv")
Stranieri017QuartS= pd.read_csv("Destinazione/CSV/Stranieri017Quart.csv")
StranieriFasceS= pd.read_csv("Destinazione/CSV/StranieriFasce.csv")
DistrFasceSTRS= pd.read_csv("Destinazione/CSV/DistrFascSTR.csv")

#Ordine FamiglieS per grafico
FamiglieS= FamiglieS.sort_values(by="Percentuale", ascending=True)


#set pagina su tutta l'ampiezza
st.set_page_config(layout="wide")
#set titolo applicazione
st.title("StatiX")
st.write("App per la visualizzazione dei dati statistici relativi al Comune di Lecco (minori, adulti e over 65 anni, scuole e asili) - statistiche a cura dell'ufficio SIT - aggiornate il 31/08/2024")
#crea il markdown minori
st.markdown("# Minori")
#crea la sidebar con i markdown
st.sidebar.markdown("# Minori")

#colori
colorQuart= ["#FF0066", "#FF6699", "#CC3366", "#993333", "#CC3333", "#990000", "#660000", "#993300", "#CC6633", "#CC9933", "#FFCC33", "#999900", "#666600", "#669900", "#339966"]
colorMF= ["#FF0066", "#33CCCC"]
colorFasce= ["#D69EC4", "#B772A1", "#C42B91", "#912F70", "#990066"]
colorFasceSTR= ["#C0E8FB", "#6ECFF6", "#0093D7", "#0072B9", "#214297"]

#contenitore prima riga
primaRiga = st.container()
with ((primaRiga)):
    #configura numero colonne
    colpr1, colpr2, colpr3 = st.columns(3, gap="medium")
    with colpr1:
        #GRAFICO RAPPORTO TRA MINORI E TOTALE ABITANTI
        st.subheader("Rapporto (%) tra minori e totale abitanti")
        st.write(RapportoAbMinS)
        #crea grafico
        RAM= alt.Chart(RapportoAbMinS).mark_bar(color="#990066").encode(alt.X("Tipologia"), alt.Y("Percentuale"))
        #label
        textRAM = RAM.mark_text(align="center", baseline="bottom").encode(text="Percentuale")
        #stampa grafico + label
        st.altair_chart(RAM+textRAM, use_container_width=True)

    with colpr2:
        #NUOVI NATI NELL'ANNO
        st.subheader("Nuovi nati nell'anno e residenti a Lecco")
        st.write(TotaleNuoviNatiPDS)
        #DISTRIBUZIONE MINORI NATI NEI QUARTIERI
        st.subheader("Distribuzione (%) nei quartieri")
        figNat, axesNat = plt.subplots()
        axesNat.pie(x=NuoviNatiQuarS["Percentuale"], autopct='%1.1f%%', colors=colorQuart, pctdistance=1.14, wedgeprops={"edgecolor": "white","linewidth": 1})
        axesNat.axis('equal')  # Rispetto dell'aspect ratio
        axesNat.legend(ncol=1, labels=NuoviNatiQuarS["Quartiere"], title="Legenda", bbox_to_anchor=(1,1), loc="upper left")
        st.pyplot(figNat, use_container_width=True)
    with colpr3:
        #GRAFICO DISTRIBUZIONE MINORI NEI QUARTIERI
        st.subheader("Distribuzione (%) dei minori nei quartieri")
        # crea grafico
        M017Q = alt.Chart(Minori017QuartS).mark_bar(color="#990066").encode(alt.X("Quartiere"), alt.Y("Percentuale")).interactive()
        #precedente grafico in linea e non bar
        # M017Q = alt.Chart(Minori017QuartS).mark_line(point=alt.OverlayMarkDef(filled=True, fill="#990066"), strokeWidth=2.5, color="#990066"
        #                                              ).encode(alt.X("Quartiere"), alt.Y("Percentuale")).interactive()
        text = M017Q.mark_text(
            align="center",
            baseline="middle",
            dy=-7).encode(text="Percentuale")

        # stampa grafico + label
        st.altair_chart(M017Q + text, use_container_width=True)
        with st.expander("Tabella distribuzione (%) minori quartieri"):
            st.write(Minori017QuartS)

secondaRiga = st.container()
with secondaRiga:
    colsr1, colsr2, colsr3, colsr4 = st.columns(4, gap="large")
    with colsr1:
        #GRAFICO MASCHI E FEMMINE
        st.subheader("Maschi e Femmine")
        st.write(MF017S)
        figMF, axesMF = plt.subplots()
        axesMF.pie(x=MF017S["Percentuale"], autopct='%1.1f%%', pctdistance=1.24, colors= colorMF,wedgeprops={"edgecolor": "white", "linewidth": 1})
        axesMF.axis('equal')  # Rispetto dell'aspect ratio
        axesMF.legend(ncol=1, labels=MF017S["Sesso"], title="Legenda", bbox_to_anchor=(1, 1), loc="upper left")
        st.pyplot(figMF, use_container_width=True)
    with colsr2:
        # GRAFICO DISTRIBUZIONE FEMMINE NEI QUARTIERI
        st.subheader("Distribuzione (%) femmine nei quartieri")
        # crea grafico
        FQ017 = alt.Chart(FQuartieriS).mark_bar(color="#FF0066").encode(alt.X("Quartiere"),
                                                                        alt.Y("Percentuale femmine")).interactive()
        # label
        text = FQ017.mark_text(
            align="center",
            baseline="middle",
            dy=-7).encode(text="Percentuale femmine")
        # stampa grafico + label
        st.altair_chart(FQ017+text, use_container_width=True)
    with colsr3:
        # GRAFICO DISTRIBUZIONE MASCHI NEI QUARTIERI
        st.subheader("Distribuzione (%) maschi nei quartieri")
        MQ017 = alt.Chart(MQuartieriS).mark_bar(color="#33CCCC").encode(alt.X("Quartiere"),
                                                                        alt.Y("Percentuale maschi")).interactive()
        text = MQ017.mark_text(
            align="center",
            baseline="middle",
            dy=-7).encode(text="Percentuale maschi")
        # stampa grafico + label
        st.altair_chart(MQ017+text, use_container_width=True)
    with colsr4:
        # GRAFICO RAPPORTO MASCHI E FEMMINE NEI QUARTIERI
        st.subheader("Rapporto (%) maschi e femmine nei quartieri")
        figMFQ017 = px.bar(MFQuartieriS, x="Quartiere",
                         y=["Percentuale maschi", "Percentuale femmine"],
                         color_discrete_sequence=(colorMF), labels={"value": "Percentuale"}, text_auto=True)
        figMFQ017.update_layout(legend=dict(x=0, y=1.3), legend_orientation="h")
        figMFQ017.update_xaxes(tickangle=270)

        st.plotly_chart(figMFQ017, use_container_width=True)

terzaRiga = st.container()
with (terzaRiga):
    st.subheader("Rapporto (%) maschi e femmine per fasce di età")
    coltr1, coltr2, coltr3, coltr4, coltr5 = st.columns(5, gap="small")
    with coltr1:
        st.write("Maschi e femmine dagli 0 ai 2 anni")
        chart02 = (
            alt.Chart(MF02S)
            .mark_bar()
            .properties(
                height=270
            )
            .encode(
                alt.X('Sesso'),
                alt.Y("Percentuale da 0 a 2 anni"),
                color=alt.condition(
                    alt.datum.Sesso == "M",  # If the year is 1810 this test returns True,
                    alt.value("#33CCCC"),  # which sets the bar orange.
                    alt.value("#FF0066")  # And if it's not true it sets the bar steelblue.
                ))
            .interactive()
        )
        # label
        textchart02 = chart02.mark_text(align="center", baseline="bottom").encode(text="Percentuale da 0 a 2 anni")
        st.altair_chart(chart02 + textchart02, use_container_width=True)
    with coltr2:
        st.write("Maschi e femmine dai 3 ai 5 anni")
        chart35 = (
            alt.Chart(MF35S)
            .mark_bar()
            .properties(
                height=270
            )
            .encode(
                alt.X("Sesso"),
                alt.Y("Percentuale da 3 a 5 anni"),
                color=alt.condition(
                    alt.datum.Sesso == "M",  # If the year is 1810 this test returns True,
                    alt.value("#33CCCC"),  # which sets the bar orange.
                    alt.value("#FF0066")  # And if it's not true it sets the bar steelblue.
                ))
            .interactive()
        )
        textchart35 = chart35.mark_text(align="center", baseline="bottom").encode(text="Percentuale da 3 a 5 anni")
        st.altair_chart(chart35 + textchart35,use_container_width=True)
    with coltr3:
        st.write("Maschi e femmine dai 6 ai 9 anni")
        chart69 = (
            alt.Chart(MF69S)
            .mark_bar()
            .properties(
                height=270
            )
            .encode(
                alt.X("Sesso"),
                alt.Y("Percentuale da 6 a 9 anni"),
                color=alt.condition(
                    alt.datum.Sesso == "M",  # If the year is 1810 this test returns True,
                    alt.value("#33CCCC"),  # which sets the bar orange.
                    alt.value("#FF0066")  # And if it's not true it sets the bar steelblue.
                ))
            .interactive()
        )
        textchart69 = chart69.mark_text(align="center", baseline="bottom").encode(text="Percentuale da 6 a 9 anni")
        st.altair_chart(chart69 + textchart69, use_container_width=True)
    with coltr4:
        st.write("Maschi e femmine dai 10 a 13 anni")
        chart1013 = (
            alt.Chart(MF1013S)
            .mark_bar()
            .properties(
                height=270
            )
            .encode(
                alt.X("Sesso"),
                alt.Y("Percentuale da 10 a 13 anni"),
                color=alt.condition(
                    alt.datum.Sesso == "M",  # If the year is 1810 this test returns True,
                    alt.value("#33CCCC"),  # which sets the bar orange.
                    alt.value("#FF0066")  # And if it's not true it sets the bar steelblue.
                ))
            .interactive()
        )
        textchart1013 = chart1013.mark_text(align="center", baseline="bottom").encode(text="Percentuale da 10 a 13 anni")
        st.altair_chart(chart1013 + textchart1013, use_container_width=True)
    with coltr5:
        st.write("Maschi e femmine dai 14 ai 17 anni")
        chart1417 = (
            alt.Chart(MF1417S)
            .mark_bar()
            .properties(
                height=270
            )
            .encode(
                alt.X("Sesso"),
                alt.Y("Percentuale da 14 a 17 anni"),
                color=alt.condition(
                    alt.datum.Sesso == "M",  # If the year is 1810 this test returns True,
                    alt.value("#33CCCC"),  # which sets the bar orange.
                    alt.value("#FF0066")  # And if it's not true it sets the bar steelblue.
                ))
            .interactive()
        )
        textchart1417 = chart1417.mark_text(align="center", baseline="bottom").encode(text="Percentuale da 14 a 17 anni")
        st.altair_chart(chart1417+textchart1417, use_container_width=True)

quartaRiga = st.container()
with quartaRiga:
    colqr1, colqr2, colqr3 = st.columns(3, gap="medium")
    with colqr1:
        # GRAFICO MINORI SUDDIVISI PER FASCE DI ETA'
        st.subheader("Minori (%) suddivisi in fasce di età")
        figFasc, axesFasc = plt.subplots()
        axesFasc.pie(x=MinoriFasceS["Percentuale fasce di età"], autopct='%1.1f%%', colors= colorFasce, pctdistance=1.14,
                    wedgeprops={"edgecolor": "white", "linewidth": 1})
        axesFasc.axis('equal')  # Rispetto dell'aspect ratio
        axesFasc.legend(ncol=1, labels=MinoriFasceS["Fasce"], title="Legenda", bbox_to_anchor=(1, 1),
                       loc="upper left")
        st.pyplot(figFasc, use_container_width=True)

        with st.expander("Tabella minori (%) suddivisi in fasce di età"):
            st.write(MinoriFasceS)
    with colqr2:
        #  GRAFICO MINORI SUDDIVISI PER FASCE DI ETA' E QUARTIERI
        st.subheader("Minori (%) suddivisi in fasce di età e quartieri")
        figDFas = px.bar(DistrFasceS, x="Quartiere", y=["Percentuale 0-2 anni", "Percentuale 3-5 anni", "Percentuale 6-9 anni", "Percentuale 10-13 anni", "Percentuale 14-17 anni"],
                        color_discrete_sequence=(colorFasce), labels={"value": "Percentuale"}, text_auto=True)
        figDFas.update_layout(legend=dict(x=0, y=1.3), legend_orientation="h")
        figDFas.update_xaxes(tickangle=270)

        st.plotly_chart(figDFas, use_container_width=True)
        with st.expander("Tabella minori (%) suddivisi in fasce di età e quartieri"):
            st.write(DistrFasceS)
    with colqr3:
        #GRAFICO DISTRIBUZIONE FAMIGLIE CON ALMENO UN MINORE
        st.subheader("Distribuzione (%) famiglie con almeno 1 minore")

        figFam, axesFam = plt.subplots()
        squarify.plot(sizes=FamiglieS["Percentuale"], label=[f'{Quartiere}\n{Percentuale}' for Quartiere, Percentuale in zip(FamiglieS.Quartiere, FamiglieS.Percentuale)], ec = "white", color = sb.color_palette("magma",len(FamiglieS["Quartiere"])), alpha = 0.7, text_kwargs={"fontsize": 9, "color": "#3a3a3a"})

        st.pyplot(figFam)

        with st.expander("Tabella distribuzione (%) famiglie con almeno un minore"):
            st.write(FamiglieS)

quintaRiga = st.container()
with quintaRiga:
    #configura numero colonne
    colqn1, colqn2, colqn3 = st.columns(3, gap="medium")
    with colqn1:
        #GRAFICO RAPPORTO TRA STRANIERI E TOTALE MINORI
        st.subheader("Rapporto (%) tra stranieri e totale minori")
        st.write(RapportoStrMinS)
        # crea grafico
        RSTRM = alt.Chart(RapportoStrMinS).mark_bar(color="#3399FF").encode(alt.X("Tipologia"), alt.Y("Percentuale"))
        # label
        textRSTRM = RSTRM.mark_text(align="center", baseline="bottom").encode(text="Percentuale")
        # stampa grafico + label
        st.altair_chart(RSTRM + textRSTRM, use_container_width=True)

    with colqn2:
        #DISTRIBUZIONE DEGLI STRANIERI NEI QUARTIERI
        st.subheader("Distribuzione (%) degli stranieri nei quartieri")
        # crea grafico
        STRQ017 = alt.Chart(Stranieri017QuartS).mark_bar(color="#3399FF").encode(alt.X("Quartiere"),
                                                                            alt.Y("Percentuale")).interactive()
        #VECCHIO grafico a linea
        # STRQ017 = alt.Chart(Stranieri017QuartS).mark_line(point=alt.OverlayMarkDef(filled=True, fill="#3399FF"),
        #                                          strokeWidth=2, color="#3399FF"
        #                                          ).encode(alt.X("Quartiere"),
        #                                                   alt.Y("Percentuale")).interactive()
        text = STRQ017.mark_text(
            align="center",
            baseline="middle",
            dy=-7).encode(text="Percentuale")
        st.altair_chart(STRQ017+text, use_container_width=True)
        with st.expander("Tabella distribuzione (%) degli stranieri nei quartieri"):
            st.write(Stranieri017QuartS)

    with colqn3:
        # GRAFICO DISTRIBUZIONE MINORI NEI QUARTIERI
        st.subheader("Stranieri (%) suddivisi per fasce di età")
        figFascSTR, axesFascSTR = plt.subplots()
        axesFascSTR.pie(x=StranieriFasceS["Percentuale fasce di età"], autopct='%1.1f%%', colors=colorFasceSTR, pctdistance=1.14,
                     wedgeprops={"edgecolor": "white", "linewidth": 1})
        axesFascSTR.axis('equal')  # Rispetto dell'aspect ratio
        axesFascSTR.legend(ncol=1, labels=StranieriFasceS["Fasce"], title="Legenda", bbox_to_anchor=(1, 1),
                        loc="upper left")
        st.pyplot(figFascSTR)

sestariga = st.container()
with sestariga:
    colst1, colst2 = st.columns(2)
    with colst1:
        #  GRAFICO STRANIERI SUDDIVISI PER FASCE DI ETA' E QUARTIERI
        st.subheader("Stranieri (%) suddivisi in fasce di età e quartieri")

        figDFasST = px.bar(DistrFasceSTRS, x="Quartiere", y=["Percentuale 0-2 anni", "Percentuale 3-5 anni",
                                                       "Percentuale 6-9 anni", "Percentuale 10-13 anni",
                                                       "Percentuale 14-17 anni"],
                        color_discrete_sequence=(colorFasceSTR), labels={"value": "Percentuale"}, height=450, text_auto=True)
        figDFasST.update_layout(legend=dict(x=0, y=1.2), legend_orientation="h")
        figDFasST.update_xaxes(tickangle=270)
        st.plotly_chart(figDFasST, use_container_width=True)

