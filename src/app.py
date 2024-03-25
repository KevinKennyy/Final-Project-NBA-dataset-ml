import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

#Cargar modelo
with open("..\\models\\xgbclassifier_lr-0.5_md-6_subsample_0.6.pkl" ,'rb') as md:
    model = pickle.load(md)
#Cargar dataset
total_data = pd.read_csv("..\\data\\processed\\total_data_final.csv")


def main():
    st.title("Predicciones NBA")

    st.sidebar.header("Selecciona tus parametros")

    #Creamos listas de los equipos y sus abreviaciones
    team_list = total_data["team_name_home"].to_list()
    team_abb_list = total_data["team_abbreviation_home"].to_list()

    #Creamos una lista para mostrar al equipo y su abreviatura juntas
    complete_team_list = []
    for index, row in total_data.iterrows():
        equipo = f"{row['team_name_home']} ({row['team_abbreviation_home']})"
        complete_team_list.append(equipo)

    #Con las listas anteriores creamos un Dataframe para agrupar todos los valores
    team_df = pd.DataFrame({'team_abbreviation_home': team_abb_list, 'team_name_home': team_list, 'final_team_home': complete_team_list})
    team_df= team_df.drop_duplicates()

    #Lista final de equipos
    final_team_list = team_df['final_team_home']
    input_team_list = st.sidebar.selectbox("Selecciona tu Equipo", final_team_list)

    #Localizar valores en funcion del equipo que ha sido seleccionado
    valor_abb = team_df.loc[team_df['final_team_home'] == input_team_list, 'team_abbreviation_home'].iloc[0]
    valor_team = team_df.loc[team_df['final_team_home'] == input_team_list, 'team_name_home'].iloc[0]
    team_id_home = total_data.loc[total_data['team_name_home'] == valor_team, 'team_id_home'].iloc[0]
    
    #Lista de Matches
    matchup_data = total_data['matchup_home']
    matchup_data = matchup_data.drop_duplicates()
    matchup_list = matchup_data.to_list()
    local_matches = [element for element in matchup_list if element.startswith(valor_abb)]
    match_team_input = st.sidebar.selectbox("Selecciona tu Match", local_matches)

    #Lista de Fechas
    game_date = total_data['game_date']
    game_date = game_date.drop_duplicates()
    game_list = total_data.loc[total_data['matchup_home'] == match_team_input, 'game_date'].tolist()
    game_date_input = st.sidebar.selectbox("Selecciona tu Fecha", game_list)
    
    #Localizar el game_id una vez se especifica la fecha
    game_id = total_data.loc[total_data['game_date'] == game_date_input, 'game_id'].iloc[0]

    #Lista de Temporadas
    season_list = total_data["season_type"].to_list()
    season_list_clean = set(season_list)
    season_list_f = list(season_list_clean)
    input_season_list = st.sidebar.selectbox("Temporada", season_list_f)
    season_id = total_data.loc[total_data['game_date'] == game_date_input, 'season_id'].iloc[0]

    #Creamos un diccionario con los datos categoricos introducidos por el usuario

    data_cat = {'season_id': season_id, 'team_id_home': team_id_home, 'team_abbreviation_home': valor_abb, 
    'team_name_home': valor_team, 'game_id': game_id, 'game_date': game_date_input,
    'matchup_home' : match_team_input, 
    'season_type': input_season_list }
    
    #Convertimos este diccionario en un dataframe para luego preprocesarlos
    data_cat_df = pd.DataFrame(data_cat, index =[0])

    # Preprocesamiento de datos categóricos

    #Primero una lista con las columnas categoricas que estamos manejando
    categorical_cols = ['season_id', 'team_id_home', 'team_abbreviation_home', 'team_name_home', 'game_id', 'game_date', 'matchup_home', 'season_type']

    with open("..\\data\\processed\\encode_data.pkl", 'rb') as f:
        encoding_info = pickle.load(f)

    # Aplicar el 
    data_cat_encoded = data_cat_df.copy()
    for col in categorical_cols:
    # Map labels from encoding information to the new data
        data_cat_encoded[col] = data_cat_encoded[col].map(lambda x: encoding_info[col].tolist().index(x) if x in encoding_info[col] else -1)

    #Empezamos con la insercion de datos numericos

    st.subheader("Equipo local")
    
    fga_home = st.number_input("Tiros de campo intentados en casa", min_value=0)
    fg3a_home = st.number_input("Tiros de campo de tres puntos intentados en casa", min_value=0)
    fta_home = st.number_input("Tiros de campo libres intentados en casa", min_value=0)
    oreb_home = st.number_input("Rebotes Ofensivos en casa", min_value=0)
    dreb_home = st.number_input("Rebotes Defensivos en casa", min_value=0)
    ast_home = st.number_input("Asistencias en casa", min_value=0)
    stl_home = st.number_input("Robos en casa", min_value=0)
    blk_home = st.number_input("Bloqueos en casa", min_value=0)
    tov_home = st.number_input("Perdidas de balón en casa", min_value=0)

    st.subheader("Equipo Visitante")

    fga_away = st.number_input("Tiros de campo intentados visitante", min_value=0)
    fg3a_away = st.number_input("Tiros de campo de tres puntos intentados visitante", min_value=0)
    fta_away = st.number_input("Tiros de campo libres intentados visitante", min_value=0)
    oreb_away = st.number_input("Rebotes Ofensivos visitante", min_value=0)
    dreb_away = st.number_input("Rebotes Defensivos visitante", min_value=0)
    ast_away = st.number_input("Asistencias visitante", min_value=0)
    stl_away = st.number_input("Robos visitante", min_value=0)
    blk_away = st.number_input("Bloqueos visitante", min_value=0)
    tov_away = st.number_input("Perdidas de balón visitante", min_value=0)

    fg_pct_home= st.slider("% de tiros realizados (local)", min_value=0, max_value=100)
    fg_pct_home = fg_pct_home/100
    
    fg_pct_away= st.slider("% de tiros realizados (visitante)", min_value=0, max_value=100)
    fg_pct_away = fg_pct_away/100

    fg3_pct_home= st.slider("% de tiros de 3 puntos (local)", min_value=0, max_value=100)
    fg3_pct_home = fg3_pct_home/100
    
    fg3_pct_away= st.slider("% de tiros de 3 puntos (visitante)", min_value=0, max_value=100)
    fg3_pct_away = fg3_pct_away/100
    
    ft_pct_home= st.slider("% de tiros libres (local)", min_value=0, max_value=100)
    ft_pct_home = ft_pct_home/100
    
    ft_pct_away= st.slider("% de tiros libres (visitante)", min_value=0, max_value=100)
    ft_pct_away = ft_pct_away/100

    #Creamos un diccionario y un DataFrame de los datos numericos
    data_num = {'fga_home': fga_home, 
    'fg3a_home': fg3a_home, 'fta_home' : fta_home, 'oreb_home': oreb_home, 'dreb_home': dreb_home, 
    'ast_home': ast_home, 'stl_home': stl_home, 'blk_home': blk_home, 'tov_home':tov_home, 
    'fga_away': fga_away, 'fg3a_away': fg3a_away, 'fta_away': fta_away, 'oreb_away': oreb_away, 'dreb_away': dreb_away,
    'ast_away': ast_away, 'stl_away': stl_away, 'blk_away': blk_away, 'tov_away': tov_away, 
    'fg_pct_home': fg_pct_home, 'fg_pct_away': fg_pct_away, 'fg3_pct_home': fg3_pct_home, 'fg3_pct_away': fg3_pct_away, 'ft_pct_home': ft_pct_home, 'ft_pct_away': ft_pct_away }
    
    st.warning("Por favor, llene todos los campos con valores numéricos diferentes de cero antes de generar el DataFrame.")

    

    button = st.button("Mostrar")


    if button:
        data_num_df = pd.DataFrame(data_num, index=[0])
        data_final = pd.concat([data_num_df, data_cat_encoded], axis=1)
        data_final = data_final.values.tolist()
        prediccion = model.predict(data_final)
        #predict_prob = model.predict_proba(data_final)
        
        # Mostrar los datos seleccionados y la predicción en Streamlit
        col1, col2 = st.columns(2)

        with col1:
            st.subheader('Prediccion')
            st.write(prediccion)
        #with col2:
            #st.subheader('Probabilidad de Prediccion')
            #st.write(predict_prob)
        
        if prediccion >= 0.50:
            st.subheader("Este equipo tiene muchas probabilidades de ganar")
        else:
            st.subheader('Este equipo tiene las de perder')

    else:
        st.write("Aqui aparecera la prediccion")

if __name__ == "__main__":
    main()