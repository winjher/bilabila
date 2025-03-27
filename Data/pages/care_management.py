import streamlit as st
import datetime

st.title('🦋 Bilabila Machine Learning App')

# Simulated data (replace with your actual data source)
notifications = [
    {"message": "Daily reminder: Clean cages and refill food plates.", "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
    {"message": "Warning: Potential disease outbreak detected. Monitor butterflies closely.", "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
    {"message": "Notification: Butterfly emergence expected in 2 days.", "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
]

dashboardData = {
    "plantInventory": {
        "floweringPlants": 10,
        "hostPlants": 5,
        "plant alert": "leaves = {0: 'with leaves', 1: 'out leaves'}"

    },
    "butterflyPopulation": {
        "totalButterflies": 25,
        "eggs": 15,
        "pupae": 8,
    },
    "careRecommendations": [
        "Refill food plates today.",
        "Check for signs of disease in butterflies.",
        "Monitor ovipositing stems for eggs."
    ],
    "analytics": {
        "butterflyEmergenceRate": "90%",
        "eggHatchingRate": "85%",
        "averageLifespan": "3 weeks",
    },
}


def display_notifications(notifications):
    st.subheader("Inbox")
    for notification in notifications:
        st.info(f"{notification['message']} ({notification['timestamp']})")


def display_dashboard(dashboardData):
    st.subheader("Dashboard")
    cols = st.columns(2)  # Arrange items in two columns

    with cols[0]:
        st.subheader("Plant Inventory")
        st.write(f"Flowering Plants: {dashboardData['plantInventory']['floweringPlants']}")
        st.write(f"Host Plants: {dashboardData['plantInventory']['hostPlants']}")

    with cols[1]:
        st.subheader("Butterfly Population")
        st.write(f"Total Butterflies: {dashboardData['butterflyPopulation']['totalButterflies']}")
        st.write(f"Eggs: {dashboardData['butterflyPopulation']['eggs']}")
        st.write(f"Pupae: {dashboardData['butterflyPopulation']['pupae']}")


    st.subheader("Care Recommendations")
    for recommendation in dashboardData['careRecommendations']:
        st.write(f"- {recommendation}")


    st.subheader("Analytics")
    st.write(f"Butterfly Emergence Rate: {dashboardData['analytics']['butterflyEmergenceRate']}")
    st.write(f"Egg Hatching Rate: {dashboardData['analytics']['eggHatchingRate']}")
    st.write(f"Average Lifespan: {dashboardData['analytics']['averageLifespan']}")


# Streamlit app
st.title("Butterfly Care Management System")

if st.button("Configure Notifications"):
    st.warning("Notifications configuration is not yet implemented.")

display_notifications(notifications)
display_dashboard(dashboardData)
