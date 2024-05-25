import streamlit as st
import pandas as pd

# Load the dataset
@st.cache
def load_data():
    # Replace 'housing_data.csv' with the path to your dataset file
    return pd.read_csv('housing_data.csv')

data = load_data()

# Streamlit App
st.title("Indian Housing Dataset Explorer")

# About Dataset
st.header("About Dataset")
st.markdown("""
**Context**

The spectrum of housing options in India is incredibly diverse, spanning from the opulent palaces once inhabited by maharajas of yore, to the contemporary high-rise apartment complexes in bustling metropolitan areas, and even to the humble abodes in remote villages, consisting of modest huts. This wide-ranging tapestry of residential choices reflects the significant expansion witnessed in India's housing sector, which has paralleled the upward trajectory of income levels in the country. According to the findings of the Human Rights Measurement Initiative, India currently achieves 60.9% of what is theoretically attainable, considering its current income levels, in ensuring the fundamental right to housing for its citizens.

In the realm of housing arrangements, renting, known interchangeably as hiring or letting, constitutes an agreement wherein compensation is provided for the temporary utilization of a resource, service, or property owned by another party. Within this arrangement, a gross lease is one where the tenant is obligated to pay a fixed rental amount, and the landlord assumes responsibility for covering all ongoing property-related expenses. The concept of renting also aligns with the principles of the sharing economy, as it fosters the utilization of assets and resources among individuals or entities, promoting efficiency and access to housing solutions for a broad spectrum of individuals.

**Content**

Within this dataset, you will find a comprehensive collection of data pertaining to nearly 4700+ available residential properties, encompassing houses, apartments, and flats offered for rent. This dataset is rich with various attributes, including the number of bedrooms (BHK), rental rates, property size, number of floors, area type, locality, city, furnishing status, tenant preferences, bathroom count, and contact information for the respective point of contact.
""")

# Dataset Glossary
st.header("Dataset Glossary (Column-Wise)")
st.markdown("""
- **BHK**: Number of Bedrooms, Hall, Kitchen.
- **Rent**: Rent of the Houses/Apartments/Flats.
- **Size**: Size of the Houses/Apartments/Flats in Square Feet.
- **Floor**: Houses/Apartments/Flats situated in which Floor and Total Number of Floors (Example: Ground out of 2, 3 out of 5, etc.)
- **Area Type**: Size of the Houses/Apartments/Flats calculated on either Super Area or Carpet Area or Build Area.
- **Area Locality**: Locality of the Houses/Apartments/Flats.
- **City**: City where the Houses/Apartments/Flats are Located.
- **Furnishing Status**: Furnishing Status of the Houses/Apartments/Flats, either it is Furnished or Semi-Furnished or Unfurnished.
- **Tenant Preferred**: Type of Tenant Preferred by the Owner or Agent.
- **Bathroom**: Number of Bathrooms.
- **Point of Contact**: Whom should you contact for more information regarding the Houses/Apartments/Flats.
""")

# Data Explorer
st.header("Data Explorer")

# Display the dataset
st.write(data)

# Filters
st.sidebar.header("Filters")
city_filter = st.sidebar.multiselect("Select City", data['City'].unique())
furnishing_filter = st.sidebar.multiselect("Select Furnishing Status", data['Furnishing Status'].unique())

# Apply filters
filtered_data = data
if city_filter:
    filtered_data = filtered_data[filtered_data['City'].isin(city_filter)]
if furnishing_filter:
    filtered_data = filtered_data[filtered_data['Furnishing Status'].isin(furnishing_filter)]

st.write(filtered_data)

if st.sidebar.checkbox("Show Summary"):
    st.header("Summary Statistics")
    st.write(filtered_data.describe())

if st.sidebar.checkbox("Show Visualizations"):
    st.header("Visualizations")
    st.bar_chart(filtered_data['City'].value_counts())
    st.bar_chart(filtered_data['Furnishing Status'].value_counts())



# Streamlit App
st.title("Housing Dataset Descriptive Statistics")

# Display the dataset
st.header("Dataset")
st.write(data)

# Descriptive Statistics
st.header("Descriptive Statistics")

# Show descriptive statistics for numerical columns
st.subheader("Numerical Columns")
st.write(data.describe())

# Show descriptive statistics for categorical columns
st.subheader("Categorical Columns")
categorical_columns = data.select_dtypes(include=['object']).columns
st.write(data[categorical_columns].describe())

# Filtered Descriptive Statistics
st.sidebar.header("Filters")
selected_city = st.sidebar.selectbox("Select City", options=data['City'].unique())
filtered_data = data[data['City'] == selected_city]

st.header(f"Descriptive Statistics for {selected_city}")
st.subheader("Numerical Columns")
st.write(filtered_data.describe())

st.subheader("Categorical Columns")
st.write(filtered_data[categorical_columns].describe())