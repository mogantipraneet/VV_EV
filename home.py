import streamlit as st
import folium
from streamlit_folium import st_folium
from streamlit_js_eval import get_geolocation
from folium.plugins import MarkerCluster # Import MarkerCluster

def home_page(current_user):
    # --- Glassmorphic Theme CSS ---
    st.markdown(
        """
        <style>
        /* Whole App */
        .stApp {
            background: radial-gradient(circle at top left, rgb(117, 210, 202), rgba(95, 113, 111, 0.85), rgb(76, 95, 100));
        }

        /* Main Content Area Styling */
        .main .block-container {
            background: rgba(40, 40, 40, 0.5);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(144, 238, 144, 0.4);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 0 30px rgba(144, 238, 144, 0.3);
        }

        /* Headings */
        h1, h2, h3, h4, h5, h6, .stSubheader {
            color: #bfffc8;
            text-shadow: 0px 0px 8px rgba(144, 238, 144, 0.8);
        }
        h1 { text-align: left; }

        /* Input Widgets (text, number, selectbox) */
        .stTextInput > div > div > input, .stNumberInput > div > div > input, .stSelectbox > div > div {
            border: 2px solid rgba(144, 238, 144, 0.6) !important;
            border-radius: 10px;
            background: rgba(42, 42, 42, 0.8) !important;
            color: #f1f1f1 !important;
            font-weight: 500;
        }
        label { color: #a8ffb0 !important; font-weight: bold; }

        /* Buttons */
        .stButton > button {
            background: linear-gradient(135deg, #90ee90, #5cd65c);
            color: #0a0a0a !important;
            border-radius: 10px;
            padding: 10px 20px;
            font-weight: bold;
        }

        /* Alerts */
        .stAlert {
            background: rgba(144, 238, 144, 0.1);
            border-left: 5px solid #90ee90;
            color: #bfffc8;
            border-radius: 10px;
        }
        .stAlert.st-alert-warning {
            background: rgba(255, 165, 0, 0.1);
            border-left: 5px solid #ffa500;
            color: #ffdead;
        }

        /* Folium Map Container */
        .stFoliumMap { border-radius: 15px; overflow: hidden; }
        </style>
        """,
        unsafe_allow_html=True
    )

    # --- Layout for Title and Logout Button ---
    col1, col2 = st.columns([0.85, 0.15])
    with col1:
        st.title("⚡ EV Charging Dashboard")
    with col2:
        if st.button("Logout"):
            st.session_state['logged_in'] = False
            if 'email' in st.session_state:
                del st.session_state['email']
            st.rerun()

    # --- Vehicle selection from user's data ---
    user_data = st.session_state.users.get(current_user, {})
    user_vehicles = user_data.get("vehicles", [])
    if not user_vehicles:
        st.warning("⚠️ No vehicles found for your account.")
        st.stop()
    selected_vehicle = st.selectbox("Choose your vehicle:", user_vehicles)
    st.success(f"Dashboard loaded for vehicle: **{selected_vehicle}**")

    # --- Location detection ---
    location = get_geolocation()
    if location:
        lat = location["coords"]["latitude"]
        lon = location["coords"]["longitude"]
    else:
        st.warning("Cannot get your location. Please enter manually.")
        lat = st.number_input("Latitude", value=17.44, format="%.6f")
        lon = st.number_input("Longitude", value=78.34, format="%.6f")
        if lat == 0.0 and lon == 0.0:
            st.stop()

    # --- Map with stations ---
    m = folium.Map(location=[lat, lon], zoom_start=11) # Map with default tiles
    folium.Marker(
        [lat, lon], popup="You are here 🚗",
        icon=folium.Icon(color="blue", icon="user", prefix="fa")
    ).add_to(m)

    stations = [
        {"name": "Station A", "lat":17.704486,"lon":78.0938307, "ac": 4, "dc": 2},
        {"name": "Station B", "lat":17.6593985, "lon":77.9919475,"ac": 2, "dc": 1},
        {"name": "Station C", "lat":17.6260267, "lon":77.6926427, "ac": 6, "dc": 3},
        {"name": "Station D", "lat":17.5397876, "lon":78.3720507, "ac": 7, "dc": 2},
        {"name": "Station E", "lat":17.5290662, "lon":78.3251381, "ac": 5, "dc": 2},
        {"name": "Station G", "lat":17.5616376, "lon":78.3224043, "ac": 9, "dc": 6},
        {"name": "Station H", "lat":17.5881166, "lon":78.2352711, "ac": 5, "dc": 2},
    ]

    # Create a MarkerCluster group for a cleaner map
    marker_cluster = MarkerCluster().add_to(m)

    for s in stations:
        popup_html = f"""
        <b>{s['name']}</b><br>
        AC: {s['ac']} | DC: {s['dc']}<br>
        <hr style='margin: 5px 0;'>
        <i>Click this text to book a slot</i>
        """
        # Add markers to the cluster group instead of the main map
        folium.Marker(
            location=[s["lat"], s["lon"]],
            popup=folium.Popup(popup_html, max_width=300),
            icon=folium.Icon(color="green", icon="bolt", prefix="fa")
        ).add_to(marker_cluster)

    map_data = st_folium(m, width=700, height=500)

    # --- Click-to-book logic ---
    if map_data and map_data.get("last_object_clicked_popup"):
        clicked_popup_html = map_data["last_object_clicked_popup"]
        selected_station_name = None
        for s in stations:
            if s["name"] in clicked_popup_html:
                selected_station_name = s["name"]
                break
        
        if selected_station_name:
            st.session_state["selected_vehicle"] = selected_vehicle
            st.session_state["selected_station"] = selected_station_name
            st.session_state["page"] = "book"
            st.rerun()