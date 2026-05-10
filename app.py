import streamlit as st

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Mechanical Unit Converter & Material Density Checker",
    page_icon="⚙️",
    layout="centered"
)

# -------------------------------
# Header
# -------------------------------
st.title("⚙️ Mechanical Unit Converter & Material Density Checker")

st.markdown("""
### Developed By:
- **Muhammad Junaid**
- **Roll Number: 25-ME-95**
""")

st.divider()

# -------------------------------
# Sidebar Menu
# -------------------------------
option = st.sidebar.selectbox(
    "Select Tool",
    ["Unit Converter", "Material Density Checker"]
)

# =====================================================
# UNIT CONVERTER
# =====================================================
if option == "Unit Converter":

    st.header("🔄 Mechanical Unit Converter")

    conversion_type = st.selectbox(
        "Choose Conversion Type",
        ["Length", "Force", "Pressure", "Temperature"]
    )

    # ---------------- LENGTH ----------------
    if conversion_type == "Length":

        value = st.number_input("Enter Value", value=0.0)

        from_unit = st.selectbox(
            "From",
            ["Meter", "Centimeter", "Millimeter"]
        )

        to_unit = st.selectbox(
            "To",
            ["Meter", "Centimeter", "Millimeter"]
        )

        # Convert to meters first
        meter_value = value

        if from_unit == "Centimeter":
            meter_value = value / 100

        elif from_unit == "Millimeter":
            meter_value = value / 1000

        # Convert meters to target
        result = meter_value

        if to_unit == "Centimeter":
            result = meter_value * 100

        elif to_unit == "Millimeter":
            result = meter_value * 1000

        st.success(f"Converted Value = {result:.4f} {to_unit}")

    # ---------------- FORCE ----------------
    elif conversion_type == "Force":

        value = st.number_input("Enter Force Value", value=0.0)

        from_unit = st.selectbox(
            "From Force Unit",
            ["Newton", "Kilonewton"]
        )

        to_unit = st.selectbox(
            "To Force Unit",
            ["Newton", "Kilonewton"]
        )

        # Convert to Newton
        newton = value

        if from_unit == "Kilonewton":
            newton = value * 1000

        # Convert to target
        result = newton

        if to_unit == "Kilonewton":
            result = newton / 1000

        st.success(f"Converted Force = {result:.4f} {to_unit}")

    # ---------------- PRESSURE ----------------
    elif conversion_type == "Pressure":

        value = st.number_input("Enter Pressure Value", value=0.0)

        from_unit = st.selectbox(
            "From Pressure Unit",
            ["Pascal", "Kilopascal", "Bar"]
        )

        to_unit = st.selectbox(
            "To Pressure Unit",
            ["Pascal", "Kilopascal", "Bar"]
        )

        # Convert to Pascal
        pascal = value

        if from_unit == "Kilopascal":
            pascal = value * 1000

        elif from_unit == "Bar":
            pascal = value * 100000

        # Convert to target
        result = pascal

        if to_unit == "Kilopascal":
            result = pascal / 1000

        elif to_unit == "Bar":
            result = pascal / 100000

        st.success(f"Converted Pressure = {result:.4f} {to_unit}")

    # ---------------- TEMPERATURE ----------------
    elif conversion_type == "Temperature":

        value = st.number_input("Enter Temperature", value=0.0)

        from_unit = st.selectbox(
            "From Temperature Unit",
            ["Celsius", "Fahrenheit"]
        )

        to_unit = st.selectbox(
            "To Temperature Unit",
            ["Celsius", "Fahrenheit"]
        )

        result = value

        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = (value * 9/5) + 32

        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (value - 32) * 5/9

        st.success(f"Converted Temperature = {result:.2f} {to_unit}")


# =====================================================
# MATERIAL DENSITY CHECKER
# =====================================================
elif option == "Material Density Checker":

    st.header("🧱 Material Density Checker")

    materials = {
        "Steel": 7850,
        "Aluminum": 2700,
        "Copper": 8960,
        "Brass": 8500,
        "Cast Iron": 7200
    }

    material = st.selectbox(
        "Select Material",
        list(materials.keys())
    )

    density = materials[material]

    st.info(f"Density of {material} = {density} kg/m³")

    volume = st.number_input(
        "Enter Volume (m³)",
        min_value=0.0,
        value=1.0
    )

    mass = density * volume

    st.success(f"Estimated Mass = {mass:.2f} kg")

# -------------------------------
# Footer
# -------------------------------
st.divider()

st.caption("Mechanical Engineering Mini Project using Streamlit Cloud")
