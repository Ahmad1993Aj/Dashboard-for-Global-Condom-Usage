import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

# Streamlit Konfiguration
st.set_page_config(page_title="EDV", page_icon=":bar_chart:", layout="wide")
st.title("EDV - Exploratory Data Visualization")
st.header("Rich Global Condom Usage Dataset")

st.subheader("Überblick")
st.write("""
Dieses Dataset enthält Informationen über die Kondomnutzung in verschiedenen Ländern und Regionen.
Es umfasst Merkmale wie Region, Land, Jahr, Verkaufszahlen, Marktumsätze, Aufklärungskampagnen und vieles mehr.
Diese App hilft, Trends und Zusammenhänge zu visualisieren und Erkenntnisse über sexuelle Gesundheit abzuleiten.
""")

# Eingabe des Dateipfads
st.subheader("📁 Lade deine CSV-Datei")
path = st.text_input("Gib den vollständigen Pfad zur CSV-Datei ein")

if path:
    try:
        @st.cache_data
        def load_data():
            return pd.read_csv(path)

        df = load_data()

        st.success("Datei erfolgreich geladen!")
        tab1, tab2, tab3 = st.tabs(["📋 Vorschau", "📊 Analyse nach Land", "📈 Korrelationen"])

        # TAB 1 – Vorschau
        with tab1:
            st.subheader("🔍 Datenvorschau")
            st.dataframe(df.head())

            st.subheader("📄 Spalteninformationen")
            st.write(df.dtypes)

        # TAB 2 – Filter & Visualisierung
        with tab2:
            st.subheader("🌍 Land auswählen")
            country = st.selectbox("Wähle ein Land", df["Country"].dropna().unique())
            filtered_df = df[df["Country"] == country].sort_values("Year")

            st.write(f"Datensätze für **{country}**:")
            st.dataframe(filtered_df)

            st.subheader("📈 Verkaufszahlen über die Jahre")
            if "Year" in filtered_df.columns and "Total Sales (Million Units)" in filtered_df.columns:
                filtered_df = filtered_df.dropna(subset=["Year", "Total Sales (Million Units)"])
                st.line_chart(
                    filtered_df.set_index("Year")["Total Sales (Million Units)"]
                )

            st.subheader("📊 Awareness Index im Zeitverlauf")
            if "Awareness Index (0-10)" in filtered_df.columns:
                st.bar_chart(
                    filtered_df.set_index("Year")["Awareness Index (0-10)"]
                )

        # TAB 3 – Korrelationsanalyse
        with tab3:
            st.subheader("📉 Korrelationen numerischer Werte")
            numeric_df = df.select_dtypes(include=[np.number])
            corr = numeric_df.corr()

            fig, ax = plt.subplots(figsize=(12, 8))
            sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
            st.pyplot(fig)

    except Exception as e:
        st.error(f"Fehler beim Laden der Datei: {e}")
else:
    st.info("Bitte gib den Pfad zur CSV-Datei ein.")
