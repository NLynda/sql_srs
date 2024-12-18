import streamlit as st
import pandas as pd
import duckdb



# Créer un DataFrame
data = {
    'colonne1': [1, 2, 3],
    'colonne2': ['A', 'B', 'C']
}
df = pd.DataFrame(data)

# Connexion to duckdb
conn = duckdb.connect()

#Creation des onglets
tab1, tab2, tab3 = st.tabs(['cat', 'dog', 'owl'])
# Contenu des onglets
with tab1:
    # Creer chmps de saisie des requettes SQL dans 
    # streamlit
    sql_input = st.text_area("Inserer votre requette SQL", \
        'SELECT colonne2 FROM df')

    # Afficher le dataframe dans streamlit
    st.dataframe(df)
    
    # Charger le dataframe dans duckdb
    st.write(conn.execute(sql_input))

with tab2:
    st.write("Hello world")

with tab3:
    st.write('bienvenu dans longlet 3')
