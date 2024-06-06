# import streamlit as st
# import requests

# st.title("Télécommande pour Minicar")

# # Section pour afficher l'état du minicar
# st.subheader("État du Minicar")
# if "status" not in st.session_state:
#     st.session_state.status = "En attente des données..."
# status = st.text(f"Statut : {st.session_state.status}")

# # CSS pour positionner les boutons en cercle
# circle_css = """
# <style>
# .circle-container {
#     position: relative;
#     width: 300px;
#     height: 300px;
#     border-radius: 50%;
#     margin: 50px auto;
#     border: 1px solid #ddd;
# }
# .circle-container button {
#     position: absolute;
#     width: 80px;
#     height: 80px;
#     border-radius: 50%;
#     border: none;
#     cursor: pointer;
# }
# .btn-forward { top: 10%; left: 50%; transform: translate(-50%, -50%); }
# .btn-left { top: 50%; left: 10%; transform: translate(-50%, -50%); }
# .btn-right { top: 50%; left: 90%; transform: translate(-50%, -50%); }
# .btn-backward { top: 90%; left: 50%; transform: translate(-50%, -50%); }
# .btn-stop { top: 50%; left: 50%; transform: translate(-50%, -50%); background-color: red; }
# </style>
# """

# st.markdown(circle_css, unsafe_allow_html=True)


# # Functions to send POST requests and update status
# def send_request(endpoint):
#     try:
#         response = requests.post(f"http://adresse_ip_du_minicar/{endpoint}")
#         st.session_state.status = response.text
#     except Exception as e:
#         st.session_state.status = f"Erreur : {str(e)}"


# # HTML for buttons in circle
# circle_html = """
# <div class="circle-container">
#     <button class="btn-forward" onclick="fetch('/forward', {method: 'POST'})">Avant</button>
#     <button class="btn-left" onclick="fetch('/left', {method: 'POST'})">Gauche</button>
#     <button class="btn-right" onclick="fetch('/right', {method: 'POST'})">Droite</button>
#     <button class="btn-backward" onclick="fetch('/backward', {method: 'POST'})">Arrière</button>
#     <button class="btn-stop" onclick="fetch('/stop', {method: 'POST'})">Stop</button>
# </div>
# """

# st.markdown(circle_html, unsafe_allow_html=True)
import streamlit as st
import requests

st.title("Télécommande pour Minicar")

# Section pour afficher l'état du minicar
st.subheader("État du Minicar")
if "status" not in st.session_state:
    st.session_state.status = "En attente des données..."
status = st.text(f"Statut : {st.session_state.status}")

# Ajouter une section pour la caméra
st.subheader("Caméra du Minicar")
# URL de l'image de la caméra (à remplacer par l'URL réelle)
camera_url = "http://adresse_ip_de_la_camera/image"
st.image(camera_url, caption="Vue de la caméra", use_column_width=True)

# CSS pour positionner les boutons en cercle
circle_css = """
<style>
.circle-container {
    position: relative;
    width: 300px;
    height: 300px;
    border-radius: 50%;
    margin: 50px auto;
    border: 1px solid #ddd;
}
.circle-container button {
    position: absolute;
    width: 80px;
    height: 80px;
    border-radius: 50%;
    border: none;
    cursor: pointer;
}
.btn-forward { top: 10%; left: 50%; transform: translate(-50%, -50%); }
.btn-left { top: 50%; left: 10%; transform: translate(-50%, -50%); }
.btn-right { top: 50%; left: 90%; transform: translate(-50%, -50%); }
.btn-backward { top: 90%; left: 50%; transform: translate(-50%, -50%); }
.btn-stop { top: 50%; left: 50%; transform: translate(-50%, -50%); background-color: red; }
</style>
"""

st.markdown(circle_css, unsafe_allow_html=True)


# Functions to send POST requests and update status
def send_request(endpoint):
    try:
        response = requests.post(f"http://adresse_ip_du_minicar/{endpoint}")
        st.session_state.status = response.text
    except Exception as e:
        st.session_state.status = f"Erreur : {str(e)}"


# HTML for buttons in circle
circle_html = """
<div class="circle-container">
    <button class="btn-forward" onclick="fetch('/forward', {method: 'POST'})">Avant</button>
    <button class="btn-left" onclick="fetch('/left', {method: 'POST'})">Gauche</button>
    <button class="btn-right" onclick="fetch('/right', {method: 'POST'})">Droite</button>
    <button class="btn-backward" onclick="fetch('/backward', {method: 'POST'})">Arrière</button>
    <button class="btn-stop" onclick="fetch('/stop', {method: 'POST'})">Stop</button>
</div>
"""

st.markdown(circle_html, unsafe_allow_html=True)
