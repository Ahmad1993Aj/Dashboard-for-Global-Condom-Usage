import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import numpy as np

warnings.filterwarnings("ignore")

# Streamlit-Konfiguration
st.set_page_config(page_title="EDV-Ahmad", page_icon=":bar_chart:", layout="wide")
st.title("EDV - Exploratory Data Visualization")
st.header("Rich Global Condom Usage Dataset")

st.subheader("📄 Überblick")
st.write("""
Dieses Dataset enthält Informationen über die Kondomnutzung in verschiedenen Ländern und Regionen.
Es umfasst Merkmale wie Region, Land, Jahr, Verkaufszahlen, Marktumsätze, Aufklärungskampagnen und vieles mehr.
Diese App hilft, Trends und Zusammenhänge zu visualisieren und Erkenntnisse über sexuelle Gesundheit abzuleiten.
""")

# CSV-Pfad-Eingabe
st.subheader("📁 Lade deine CSV-Datei")
path = st.text_input("Gib den vollständigen Pfad zur CSV-Datei ein")

if path:
    try:
        @st.cache_data
        def load_data():
            return pd.read_csv(path)

        df = load_data()
        st.success("✅ Datei erfolgreich geladen!")

        tab1, tab2, tab3 = st.tabs(["📋 Vorschau", "📊 EDV", "📈 Korrelationen"])

        # Tab 1: Vorschau & Datenprüfung
        with tab1:
            st.subheader("🔍 Daten-Vorschau")
            st.dataframe(df.head())

            tab1_1, tab1_2, tab1_3 = st.tabs(["📄 Spalteninfos", "❌ Nullwerte", "🔁 Duplikate"])
            with tab1_1:
                st.write(df.dtypes)
                st.write(f"🧮 Anzahl Zeilen: {df.shape[0]} | 🧾 Spalten: {df.shape[1]}")
            with tab1_2:
                st.write(df.isnull().sum())
            with tab1_3:
                st.write(f"🔁 Duplikate: {df.duplicated().sum()}")

        # Tab 2: EDV
        with tab2:
            st.subheader("📊 Explorative Datenanalyse")
            numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
            cat_cols = df.select_dtypes(exclude=np.number).columns.tolist()

            # Boxplots
            st.write("📦 Boxplots (Numerische Ausreißer)")
            for col in numeric_cols:
                fig, ax = plt.subplots()
                sns.boxplot(x=df[col], ax=ax)
                ax.set_title(f"Ausreißer in '{col}'")
                st.pyplot(fig)

            # value_counts
            st.write("📌 Häufigkeiten (Kategorische Spalten)")
            for col in cat_cols:
                st.markdown(f"**{col}**")
                st.dataframe(df[col].value_counts())

            # Mittelwerte
            st.write("📈 Mittelwerte (Numerische Spalten)")
            mean_values = df[numeric_cols].mean().round(2)
            st.dataframe(mean_values)

            # Histogramme
            st.write("📊 Histogramme (Numerische Verteilungen)")
            for col in numeric_cols:
                fig, ax = plt.subplots()
                df[col].hist(ax=ax, bins=20)
                ax.set_title(f"Histogramm von '{col}'")
                st.pyplot(fig)

            # Verteilung kategorischer Daten
            st.write("📊 Balkendiagramme (Kategorische Verteilungen)")
            for col in cat_cols:
                fig, ax = plt.subplots(figsize=(10, 4))
                sns.countplot(y=col, data=df, order=df[col].value_counts().index, palette="viridis", ax=ax)
                ax.set_title(f"Verteilung von '{col}'")
                st.pyplot(fig)

        # Tab 3: Korrelationen
        with tab3:
            st.subheader("📈 Korrelationen zwischen numerischen Spalten")
            corr = df[numeric_cols].corr()
            fig, ax = plt.subplots(figsize=(12, 8))
            sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
            st.pyplot(fig)

    except Exception as e:
        st.error(f"❌ Fehler beim Laden der Datei: {e}")
else:
    st.info("📌 Bitte gib den vollständigen Pfad zur CSV-Datei ein.")
