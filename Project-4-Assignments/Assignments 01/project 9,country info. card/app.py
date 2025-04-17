import streamlit as st
import requests

def fetch_country_data(country_name):
    url = f"https://restcountries.com/v3/name/{country_name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        country_data = data[0]  

        name = country_data["name"]["common"]
        capital = country_data["capital"][0] if "capital" in country_data else "N/A"
        population = country_data.get("population", "N/A")
        area = country_data.get("area", "N/A")
        currency = ", ".join(country_data.get("currencies", {}).keys()) if "currencies" in country_data else "N/A"
        region = country_data.get("region", "N/A")

        return name, capital, population, area, currency, region
    else:
        return None


def main():
    st.title("🌍 Country Information App")

   
    country_name = st.text_input("Enter country name:", "")

    if st.button("Get Country Info"):
        result = fetch_country_data(country_name)

        if result:
            name, capital, population, area, currency, region = result

            st.subheader("Country Information")
            st.write(f"**Name:** {name}")
            st.write(f"**Capital:** {capital}")
            st.write(f"**Population:** {population}")
            st.write(f"**Area:** {area} square kilometers")
            st.write(f"**Currency:** {currency}")
            st.write(f"**Region:** {region}")
        else:
            st.error("❌ Error: Country data not found! Please enter a valid country name.")

if __name__ == "__main__":
    main()
