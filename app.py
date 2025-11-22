from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Carga el CSV
df = pd.read_csv('data/mediana_ngreso_mensual_real_ocupados_stps_2dotrim2025.csv')

# Obtener las opciones únicas para los dropdowns
entidades = df['entidad_federativa'].unique()
sexos = df['sexo'].unique()
periodos = df['periodo'].unique()

app = Dash(__name__)
app.layout = html.Div([
    html.H1("Dashboard Analítico de Ingresos"),

    html.Div([
        html.Label("Entidad Federativa:"),
        dcc.Dropdown(
            id='dropdown-entidad',
            options=[{'label': ent, 'value': ent} for ent in entidades],
            value=entidades[0]
        )
    ], style={'width': '30%', 'display': 'inline-block'}),

    html.Div([
        html.Label("Sexo:"),
        dcc.Dropdown(
            id='dropdown-sexo',
            options=[{'label': sx, 'value': sx} for sx in sexos],
            value=sexos[0]
        )
    ], style={'width': '30%', 'display': 'inline-block', 'marginLeft': '2%'}),

    # Aquí agregas ambas gráficas
    dcc.Graph(id="grafico-linea", className="my-graph"),
    dcc.Graph(id="grafico-barras", className="my-graph")
], className="dbc-container")


@callback(
    Output("grafico-linea", "figure"),
    Input("dropdown-entidad", "value"),
    Input("dropdown-sexo", "value"),
)
def actualizar_linea(entidad_seleccionada, sexo_seleccionado):
    dff = df[
        (df['entidad_federativa'] == entidad_seleccionada) &
        (df['sexo'] == sexo_seleccionado)
    ]
    fig = px.line(
        dff,
        x="periodo",
        y="mediana_ingreso_mensual_real_ocupados",
        title=f"Ingreso real: {entidad_seleccionada} / {sexo_seleccionado}",
        labels={"periodo": "Año", "mediana_ingreso_mensual_real_ocupados": "Ingreso real (mediana)"}
    )
    return fig


@callback(
    Output("grafico-barras", "figure"),
    Input("dropdown-entidad", "value"),
    Input("dropdown-sexo", "value")
)

def actualizar_barras(entidad_seleccionada, sexo_seleccionado):
    # Filtra según entidad y sexo
    dff = df[
        (df['entidad_federativa'].str.lower() == entidad_seleccionada.lower()) &
        (df['sexo'] == sexo_seleccionado)
    ]
    print("dff para barras:", dff.head(), "¿vacío?", dff.empty)

    if dff.empty:
        fig = px.bar(x=[], y=[])
        fig.update_layout(title="No hay datos para esta combinación")
        return fig

    # Agrupa por periodo (año)
    agg = dff.groupby("periodo", as_index=False).median(numeric_only=True)

    print("agg agrupado:", agg.head())

    fig = px.bar(
        agg,
        x="periodo",
        y="mediana_ingreso_nominal_ocupados",
        title=f"Mediana nominal ingreso: {entidad_seleccionada} / {sexo_seleccionado}",
        labels={
            "mediana_ingreso_nominal_ocupados": "Ingreso nominal mediana",
            "periodo": "Año"
        }
    )

    return fig

if __name__ == '__main__':
    app.run(debug=True)