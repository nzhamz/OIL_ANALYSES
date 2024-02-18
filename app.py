import streamlit as st

def calculate_required_thickness(diameter, pressure):
    """
    Calculates the required thickness of a pipe based on diameter and pressure.

    Args:
        diameter (float): Pipe diameter in inches.
        pressure (float): Internal pressure in psi.

    Returns:
        float: Required thickness in millimeters.
    """
    # Using a common formula for required thickness
    required_thickness_inches = (pressure * diameter) / (2 * 1000)  # Example formula, adjust as needed

    # Convert inches to millimeters
    required_thickness_mm = required_thickness_inches * 25.4

    return required_thickness_mm

def main():
    st.title("Pipe Thickness Calculator")

    diameter = st.number_input("Enter Pipe Diameter (inches):", min_value=0.1, step=0.1)
    pressure = st.number_input("Enter Internal Pressure (psi):", min_value=0.1, step=0.1)

    if st.button("Calculate"):
        if diameter <= 0 or pressure <= 0:
            st.error("Error: Diameter and pressure must be positive.")
        else:
            try:
                required_thickness = calculate_required_thickness(diameter, pressure)
                st.success(f"Required Thickness: {required_thickness:.2f} mm")
            except Exception as e:
                st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
