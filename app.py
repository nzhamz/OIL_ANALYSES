#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 13:04:46 2024

@author: macbook
"""

import panel as pn

def calculate_required_thickness(diameter, pressure):
    """
    Calculates the required thickness of a pipe based on diameter and pressure.

    Args:
        diameter (float): Pipe diameter in inches.
        pressure (float): Internal pressure in psi.

    Returns:
        float: Required thickness in inches.
    """
    # Using a common formula for required thickness
    required_thickness = (pressure * diameter) / (2 * 1000)  # Example formula, adjust as needed

    return required_thickness

def create_app():
    """
    Creates a Panel app with user input and thickness calculation output.
    """
    diameter_input = pn.widgets.FloatInput(placeholder="Diameter (inches)")
    pressure_input = pn.widgets.FloatInput(placeholder="Pressure (psi)")

    calculate_button = pn.widgets.Button(name="Calculate")

    def calculate(event):
        diameter = diameter_input.value
        pressure = pressure_input.value

        if diameter <= 0 or pressure <= 0:
            pn.alert("Error: Diameter and pressure must be positive.")
            return

        try:
            required_thickness = calculate_required_thickness(diameter, pressure)
            thickness_output.value = f"Required Thickness: {required_thickness:.2f} inches"
        except Exception as e:
            pn.alert(f"An error occurred: {e}")

    calculate_button.on_click(calculate)

    thickness_output = pn.widgets.TextInput(name="", value="")

    layout = pn.Column(
        diameter_input,
        pressure_input,
        calculate_button,
        thickness_output,
    )

    return layout

pn.extension()

app = create_app()
app.servable()  # Start the Panel app
