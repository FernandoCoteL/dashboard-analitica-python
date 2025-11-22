# Dashboard Analítico en Python 📊

Mini proyecto de portafolio para visualización de datos con Python.

## 🎯 Objetivo

Este es un ejercicio básico en mi curva de aprendizaje de análisis y visualización de datos. El proyecto analiza datos de **ingresos mensuales de ocupados en México** (STPS - 2do Trimestre 2025).

## 🛠️ Tecnologías Aprendidas

- **Pandas**: Manipulación y análisis de datos
- **Plotly Express**: Creación de gráficos interactivos
- **Dash**: Framework para dashboards web interactivos
- **Python**: Lenguaje base del proyecto

## 📂 Estructura del Proyecto

```
dashboard-analitica-python/
├── app.py                 # Aplicación principal de Dash
├── requirements.txt       # Dependencias del proyecto
├── data/                  # Datos CSV
│   └── mediana_ngreso_mensual_real_ocupados_stps_2dotrim2025.csv
└── README.md
```

## 🚀 Instalación y Uso

1. **Clonar el repositorio**
```bash
git clone https://github.com/FernandoCoteL/dashboard-analitica-python.git
cd dashboard-analitica-python
```

2. **Crear entorno virtual**
```bash
python3 -m venv venv
source venv/bin/activate  # En Mac/Linux
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Ejecutar la aplicación**
```bash
python app.py
```

5. **Abrir en el navegador**
```
http://127.0.0.1:8050
```

## 📈 Características Actuales

- ✅ Carga de datos desde CSV
- ✅ Visualización interactiva con Plotly
- ✅ Dashboard web con Dash
- ✅ Análisis de ingresos por sexo

## 🔮 Mejoras Futuras (Roadmap)

- [ ] Agregar filtros por fecha
- [ ] Múltiples tipos de gráficos (barras, pie, scatter)
- [ ] Estadísticas descriptivas (media, desviación estándar)
- [ ] Comparación entre períodos
- [ ] Exportar reportes en PDF
- [ ] Estilizado personalizado con CSS
- [ ] Deploy en Heroku/Render

## 📚 Lo que Aprendí

- Importar y limpiar datos con Pandas
- Crear visualizaciones interactivas
- Construir aplicaciones web con Python
- Callbacks y reactividad en Dash
- Uso de Git y GitHub para control de versiones

## 📝 Notas

Este es un proyecto educativo en progreso. Cualquier sugerencia es bienvenida.

---

**Autor**: Fernando Cote  
**Año**: 2025  
**Licencia**: MIT
