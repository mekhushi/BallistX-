import streamlit as st

st.set_page_config(page_title="About | Smart Ballistics Simulator", page_icon="ℹ️")

st.title("🚀 About")



st.header(" Core Idea")
st.markdown(""" 
            
            This project blends classical physics with machine learning to simulate and predict the trajectory of a projectile (like a bullet, missile, or object under gravity + drag + wind effects). It visualizes both the physics-based simulation and ML predictions side by side""")

st.image(
        "pages/1663000963.jpg",
        caption=" Precision & Performance",
        width=700
)

st.markdown("""
### 🧠 What Problem Does This Solve?

Traditional projectile simulators rely solely on physics equations, which can become inefficient or less flexible in real-time applications, especially when dealing with varying environmental factors like wind, mass, and angle.  
**Smart Ballistics Simulator** addresses this by blending classical **physics** with **machine learning (ML)**, allowing for:

- ⚡ Real-time prediction of projectile motion  
- ⚡ Continuous learning from new data  
- ⚡ Adaptability to environmental changes (like wind speed)  
- ⚡ Improved targeting precision in ballistics simulations

---

###  Tech Stack

Built with modern tools to ensure accuracy, speed, and interactivity:

-  **Python 3.9+**
-  **Streamlit** – Sleek & fast web UI  
-  **PyTorch** – For deep learning trajectory models  
-  **NumPy** &  **SciPy** – Scientific calculations  
-  **Matplotlib** – Plotting the trajectories  
-  **Scikit-learn** – Preprocessing and feature scaling

---

###  Author

**Khushi Singh**  
Passionate about AI for real-world problems 

🔗 [GitHub](https://github.com/mekhushi)  
🔗 [LinkedIn](https://www.linkedin.com/in/khushi-singh-557317284/)

---

### 📬 Contact

💬 Got ideas, feedback, or want to collaborate?  
Feel free to reach out at: `khushisingh8317@gmail.com` ✉️

---

🎓 *This project was built as part of a deep learning & simulation initiative to bridge the gap between pure science and intelligent computing.*
""")

