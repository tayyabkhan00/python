import streamlit as st
import requests
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import time

# Configure the page
st.set_page_config(
    page_title="Weather Forecasting Dashboard",
    page_icon="🌤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# WeatherAPI.com Configuration
API_KEY = "da1dfe2b85594ef389690955252111"
BASE_URL = "http://api.weatherapi.com/v1"

class WeatherDashboard:
    def __init__(self):
        self.api_key = API_KEY
    
    def get_current_weather(self, city):
        """Get current weather data for a city"""
        url = f"{BASE_URL}/current.json"
        params = {
            'key': self.api_key,
            'q': city,
            'aqi': 'no'
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            st.error(f"Error fetching current weather: {e}")
            return None
    
    def get_forecast(self, city, days=5):
        """Get weather forecast"""
        url = f"{BASE_URL}/forecast.json"
        params = {
            'key': self.api_key,
            'q': city,
            'days': days,
            'aqi': 'no',
            'alerts': 'no'
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            st.error(f"Error fetching forecast: {e}")
            return None

def display_current_weather(data):
    """Display current weather information"""
    if not data:
        return
    
    current = data['current']
    location = data['location']
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        temp = current['temp_c']
        st.metric("Temperature", f"{temp}°C")
    
    with col2:
        humidity = current['humidity']
        st.metric("Humidity", f"{humidity}%")
    
    with col3:
        pressure = current['pressure_mb']
        st.metric("Pressure", f"{pressure} hPa")
    
    with col4:
        wind_speed = current['wind_kph']
        st.metric("Wind Speed", f"{wind_speed} km/h")
    
    # Weather description
    weather_desc = current['condition']['text']
    st.write(f"**Condition:** {weather_desc}")

def create_temperature_chart(forecast_data):
    """Create temperature forecast chart"""
    if not forecast_data:
        return None
    
    times = []
    temps = []
    feels_like = []
    
    forecast_days = forecast_data['forecast']['forecastday']
    
    for day in forecast_days:
        for hour in day['hour'][:24:3]:  # Every 3 hours for first 24 hours
            times.append(pd.to_datetime(hour['time']))
            temps.append(hour['temp_c'])
            feels_like.append(hour['feelslike_c'])
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=times, y=temps,
        mode='lines+markers',
        name='Temperature',
        line=dict(color='red', width=3)
    ))
    
    fig.add_trace(go.Scatter(
        x=times, y=feels_like,
        mode='lines+markers',
        name='Feels Like',
        line=dict(color='orange', width=2, dash='dash')
    ))
    
    fig.update_layout(
        title="24-Hour Temperature Forecast",
        xaxis_title="Time",
        yaxis_title="Temperature (°C)",
        template="plotly_white"
    )
    
    return fig

def create_weather_metrics_chart(forecast_data):
    """Create chart for multiple weather metrics"""
    if not forecast_data:
        return None
    
    times = []
    humidity = []
    pressure = []
    wind_speed = []
    
    forecast_days = forecast_data['forecast']['forecastday']
    
    for day in forecast_days:
        for hour in day['hour'][:24:3]:  # Every 3 hours for first 24 hours
            times.append(pd.to_datetime(hour['time']))
            humidity.append(hour['humidity'])
            pressure.append(hour['pressure_mb'])
            wind_speed.append(hour['wind_kph'])
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=times, y=humidity,
        mode='lines+markers',
        name='Humidity (%)',
        yaxis='y1',
        line=dict(color='blue', width=2)
    ))
    
    fig.add_trace(go.Scatter(
        x=times, y=pressure,
        mode='lines+markers',
        name='Pressure (hPa)',
        yaxis='y2',
        line=dict(color='green', width=2)
    ))
    
    fig.add_trace(go.Scatter(
        x=times, y=wind_speed,
        mode='lines+markers',
        name='Wind Speed (km/h)',
        yaxis='y3',
        line=dict(color='purple', width=2)
    ))
    
    fig.update_layout(
        title="Weather Metrics - Next 24 Hours",
        xaxis_title="Time",
        template="plotly_white",
        yaxis=dict(title="Humidity (%)", side="left"),
        yaxis2=dict(title="Pressure (hPa)", side="right", overlaying="y"),
        yaxis3=dict(title="Wind Speed (km/h)", side="right", overlaying="y", position=0.85)
    )
    
    return fig

def create_daily_forecast_table(forecast_data):
    """Create daily forecast summary table"""
    if not forecast_data:
        return None
    
    table_data = []
    forecast_days = forecast_data['forecast']['forecastday']
    
    for day in forecast_days:
        date = pd.to_datetime(day['date'])
        daily_data = day['day']
        
        table_data.append({
            'Date': date.strftime('%Y-%m-%d'),
            'Day': date.strftime('%A'),
            'Max Temp (°C)': round(daily_data['maxtemp_c'], 1),
            'Min Temp (°C)': round(daily_data['mintemp_c'], 1),
            'Avg Temp (°C)': round(daily_data['avgtemp_c'], 1),
            'Avg Humidity (%)': round(daily_data['avghumidity'], 1),
            'Condition': daily_data['condition']['text'],
            'Chance of Rain': f"{daily_data['daily_chance_of_rain']}%"
        })
    
    return pd.DataFrame(table_data)

def create_weather_radar(current_data):
    """Create a weather radar visualization"""
    if not current_data:
        return None
    
    current = current_data['current']
    
    metrics = ['Temperature', 'Humidity', 'Pressure', 'Wind Speed', 'Feels Like', 'UV Index']
    values = [
        current['temp_c'],
        current['humidity'],
        current['pressure_mb'],
        current['wind_kph'],
        current['feelslike_c'],
        current['uv']
    ]
    
    # Normalize values for better radar display
    max_vals = [50, 100, 1100, 100, 50, 10]  # Reasonable maximums for scaling
    normalized_values = [val/max_val * 100 for val, max_val in zip(values, max_vals)]
    
    fig = go.Figure(data=go.Scatterpolar(
        r=normalized_values,
        theta=metrics,
        fill='toself',
        line=dict(color='royalblue'),
        hoverinfo='text',
        text=[f"{metric}: {value}" for metric, value in zip(metrics, values)]
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=False,
        title="Current Weather Radar"
    )
    
    return fig

def display_hourly_forecast(forecast_data):
    """Display hourly forecast for today"""
    if not forecast_data:
        return None
    
    today_hours = forecast_data['forecast']['forecastday'][0]['hour']
    
    hourly_data = []
    for hour in today_hours[:12]:  # Next 12 hours
        time_obj = pd.to_datetime(hour['time'])
        hourly_data.append({
            'Time': time_obj.strftime('%H:%M'),
            'Temp (°C)': round(hour['temp_c'], 1),
            'Condition': hour['condition']['text'],
            'Rain (%)': hour['chance_of_rain'],
            'Humidity': hour['humidity']
        })
    
    return pd.DataFrame(hourly_data)

def main():
    st.title("🌤️ Weather Forecasting Dashboard (WeatherAPI.com)")
    st.markdown("---")
    
    # Initialize weather dashboard
    dashboard = WeatherDashboard()
    
    # Sidebar for city input
    st.sidebar.title("Settings")
    st.sidebar.info(f"API Key: ✅ Connected")
    
    city = st.sidebar.text_input("Enter City Name", "London")
    
    # Add country code option
    country = st.sidebar.text_input("Country Code (optional)", "")
    
    if country:
        search_query = f"{city},{country}"
    else:
        search_query = city
    
    # Forecast days selection
    days = st.sidebar.slider("Forecast Days", min_value=1, max_value=7, value=5)
    
    # Additional data options
    show_hourly = st.sidebar.checkbox("Show Hourly Forecast", value=True)
    show_radar = st.sidebar.checkbox("Show Weather Radar", value=True)
    
    # Auto-refresh option
    auto_refresh = st.sidebar.checkbox("Auto-refresh every 10 minutes")
    
    if auto_refresh:
        st.sidebar.write("Next refresh in 10 minutes")
        time.sleep(600)
        st.experimental_rerun()
    
    # Fetch weather data
    with st.spinner("Fetching weather data..."):
        current_data = dashboard.get_current_weather(search_query)
        forecast_data = dashboard.get_forecast(search_query, days=days)
    
    if not current_data or not forecast_data:
        st.error("Unable to fetch weather data. Please check the city name and try again.")
        return
    
    # Display location info
    location = current_data['location']
    current = current_data['current']
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader(f"📍 {location['name']}, {location['country']}")
        st.write(f"**Local Time:** {location['localtime']}")
        
        # Current weather overview
        st.markdown("### Current Weather")
        display_current_weather(current_data)
    
    with col2:
        # Weather icon and main info
        weather_icon = current['condition']['icon']
        if weather_icon.startswith('//'):
            weather_icon = f"https:{weather_icon}"
        st.image(weather_icon, width=100)
        
        temp = current['temp_c']
        st.markdown(f"# {temp}°C")
        st.write(f"**{current['condition']['text']}**")
        st.write(f"**Feels like:** {current['feelslike_c']}°C")
        st.write(f"**UV Index:** {current['uv']}")
    
    st.markdown("---")
    
    # Charts section
    col1, col2 = st.columns(2)
    
    with col1:
        temp_chart = create_temperature_chart(forecast_data)
        if temp_chart:
            st.plotly_chart(temp_chart, use_container_width=True)
    
    with col2:
        metrics_chart = create_weather_metrics_chart(forecast_data)
        if metrics_chart:
            st.plotly_chart(metrics_chart, use_container_width=True)
    
    # Additional visualizations
    if show_radar:
        col3, col4 = st.columns(2)
        
        with col3:
            radar_chart = create_weather_radar(current_data)
            if radar_chart:
                st.plotly_chart(radar_chart, use_container_width=True)
    
    # Forecast tables
    st.markdown("### 📅 Daily Forecast")
    forecast_table = create_daily_forecast_table(forecast_data)
    if forecast_table is not None:
        st.dataframe(forecast_table, use_container_width=True)
    
    # Hourly forecast
    if show_hourly:
        st.markdown("### ⏰ Hourly Forecast (Today)")
        hourly_table = display_hourly_forecast(forecast_data)
        if hourly_table is not None:
            st.dataframe(hourly_table, use_container_width=True)
    
    # Additional information
    st.markdown("---")
    st.markdown("### Additional Information")
    
    col5, col6, col7 = st.columns(3)
    
    with col5:
        st.write(f"**Location:** {location['name']}, {location['region']}, {location['country']}")
        st.write(f"**Latitude:** {location['lat']}")
        st.write(f"**Longitude:** {location['lon']}")
    
    with col6:
        st.write(f"**Wind Direction:** {current['wind_dir']}")
        st.write(f"**Wind Gust:** {current.get('gust_kph', 'N/A')} km/h")
        st.write(f"**Cloud Cover:** {current['cloud']}%")
    
    with col7:
        st.write(f"**Visibility:** {current['vis_km']} km")
        st.write(f"**Last Updated:** {current['last_updated']}")
        st.write(f"**Data Source:** WeatherAPI.com")

if __name__ == "__main__":
    main()