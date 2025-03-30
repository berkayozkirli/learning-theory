import streamlit as st
import matplotlib.pyplot as plt
from linear_algebra import ComplexNumber

st.set_page_config(layout="wide")
# Create a 2-column layout
col1, col2 = st.columns([1, 1])  # You can adjust the width ratio here

# Left column: title + controls
with col1:
    st.title("🌀 Complex Number Explorer")

    mode = st.radio("Input Mode", ["Rectangular (a + bi)", "Polar (r ∠ θ)"])

    if mode == "Rectangular (a + bi)":
        real = st.slider("Real Part (a)", -10.0, 10.0, 1.0)
        imag = st.slider("Imaginary Part (b)", -10.0, 10.0, 1.0)
        z = ComplexNumber(real, imag)
    else:
        magnitude = st.slider("Magnitude (r)", 0.0, 10.0, 1.0)
        angle = st.slider("Angle θ (radians)", -3.14, 3.14, 0.0)
        z = ComplexNumber.from_polar(magnitude, angle)

    st.latex(f"z = {z.re:.2f} + {z.im:.2f}i")
    st.latex(f"z = {abs(z):.5f} \\cdot e^{{i \\cdot {z.angle:.5f}}}")


# Right column: plot
with col2:
    fig, ax = plt.subplots()
    ax.quiver(0, 0, z.re, z.im, angles='xy', scale_units='xy', scale=1, color='blue')
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_aspect('equal')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    st.pyplot(fig)
