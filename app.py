# Autores: 
# Victor Sánchez - 20-70-7342
# Arquimedes Moran - 8-991-1628
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# 1. CARGA Y LIMPIEZA DE DATOS
print("Cargando datos... (esto puede tardar unos segundos)")
df = pd.read_csv('data/2025.csv') 

# amputamos las columnas basura
df = df.drop(columns=['M_FLAG', 'Q_FLAG', 'S_FLAG', 'OBS_TIME'], errors='ignore')

# filtramos solo elementos climáticos principales
df = df[df['ELEMENT'].isin(['TMAX', 'TMIN', 'PRCP'])]

# Convertimos la fecha a formato de calendario
df['DATE'] = pd.to_datetime(df['DATE'], format='%Y%m%d', errors='coerce')

# 2. INICIALIZACIÓN DE LA APP
app = dash.Dash(__name__)

# 3. DISEÑO DE LA PÁGINA
app.layout = html.Div([
    html.H1("Dashboard Climático Global 2025 (NOAA)", style={'textAlign': 'center', 'fontFamily': 'Arial'}),
    
    # Seleccionar Elemento Climático
    html.Div([
        html.Label("1. Selecciona la Variable Climática:"),
        dcc.Dropdown(
            id='filtro-elemento',
            options=[
                {'label': 'Temperatura Máxima (TMAX)', 'value': 'TMAX'},
                {'label': 'Temperatura Mínima (TMIN)', 'value': 'TMIN'},
                {'label': 'Precipitación / Lluvia (PRCP)', 'value': 'PRCP'}
            ],
            value='TMAX',
            clearable=False
        )
    ], style={'width': '48%', 'display': 'inline-block', 'padding': '10px'}),

    # Seleccionar Cantidad de Muestras
    html.Div([
        html.Label("2. Límite de registros a mostrar:"),
        dcc.Dropdown(
            id='filtro-limite',
            options=[
                {'label': '1,000 registros (Recomendado)', 'value': 1000},
                {'label': '5,000 registros', 'value': 5000},
                {'label': '10,000 registros', 'value': 10000}
            ],
            value=1000,
            clearable=False
        )
    ], style={'width': '48%', 'display': 'inline-block', 'padding': '10px'}),
    
    html.Hr(),

    # Los 4 espacios para nuestras gráficas
    html.Div([
        dcc.Graph(id='grafica-1', style={'width': '50%', 'display': 'inline-block'}),
        dcc.Graph(id='grafica-2', style={'width': '50%', 'display': 'inline-block'})
    ]),
    
    html.Div([
        dcc.Graph(id='grafica-3', style={'width': '50%', 'display': 'inline-block'}),
        dcc.Graph(id='grafica-4', style={'width': '50%', 'display': 'inline-block'})
    ])
])

# 4. CALLBACKS 

@app.callback(
    [Output('grafica-1', 'figure'),
     Output('grafica-2', 'figure'),
     Output('grafica-3', 'figure'),
     Output('grafica-4', 'figure')],
    [Input('filtro-elemento', 'value'),
     Input('filtro-limite', 'value')]
)
def actualizar_graficas(elemento_seleccionado, limite_seleccionado):
    
    df_filtrado = df[df['ELEMENT'] == elemento_seleccionado].sample(n=limite_seleccionado, random_state=42)
    
    # Gráfica 1: Línea de tiempo
    df_tiempo = df_filtrado.groupby('DATE', as_index=False)['DATA_VALUE'].mean()
    
    fig1 = px.line(df_tiempo, x='DATE', y='DATA_VALUE', 
                   title=f'Tendencia Temporal Promedio Global ({elemento_seleccionado})',
                   markers=True) # Ponemos puntitos en la línea para que se vea más pro
    fig1.update_traces(line_color='darkorange', line_width=2)
    
    # Gráfica 2: Histograma
    fig2 = px.histogram(df_filtrado, x='DATA_VALUE', nbins=30, 
                        title=f'Distribución de Valores ({elemento_seleccionado})',
                        color_discrete_sequence=['indianred'])
    
    # Gráfica 3: Box Plot
    fig3 = px.box(df_filtrado, y='DATA_VALUE', 
                  title=f'Rango y Dispersión ({elemento_seleccionado})',
                  color_discrete_sequence=['lightseagreen'])
    
    # Gráfica 4: Scatter Plot
    fig4 = px.scatter(df_filtrado, x='ID', y='DATA_VALUE', color='DATA_VALUE',
                      title=f'Mediciones por Estación ID ({elemento_seleccionado})')
    
    return fig1, fig2, fig3, fig4

# 5. ENCENDIDO DEL SERVIDOR
if __name__ == '__main__':
    app.run(debug=True)