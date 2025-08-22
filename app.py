import streamlit as st

st.set_page_config(
    page_title="Smart Ballistics Simulator",
    page_icon="🚀",
    layout="wide",
)

# Header with emojis and colors
st.markdown(
    """
    <h1 style='text-align: center; color: #1F77B4; font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;'>
        🚀 Welcome to the <span style='color:#FF6F61;'>Smart Ballistics Simulator</span> 
    </h1>
    """,
    unsafe_allow_html=True,
)

# Subtitle with emojis
st.markdown(
    """
    <p style='text-align: center; font-size:18px; font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif; color: #ffffff'>
    Experience the perfect fusion of <b> physics</b> and <b> machine learning</b> to simulate projectile trajectories.
    Use the menu on the left  to explore interactive simulations, AI predictions, and detailed insights .
    </p>
    """,
    unsafe_allow_html=True,
)

st.write("---")

col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.write("")

with col2:
    st.image("img.jpg",width=700)
    st.markdown(
        """
        <h3 style='text-align: center; color: #ffffff; font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;'>
            Why Choose Our Simulator? 
        </h3>
        <ul style='font-size:16px; line-height:1.6; color: #ffffff;'>
            <li>🔹 Realistic physics-based simulation </li>
            <li>🔹 AI-driven trajectory prediction </li>
            <li>🔹 Interactive and intuitive interface </li>
            <li>🔹 Visualize and compare results side-by-side </li>
        </ul>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.write("")

st.write("---")

st.markdown(
    """
    <p style='text-align: center; font-size: 16px; color: #ffffff;'>
        Developed with ❤️ by <b>Khushi singh</b> | Powered by Streamlit , PyTorch  & Matplotlib 
    </p>
    """,
    unsafe_allow_html=True,
)

