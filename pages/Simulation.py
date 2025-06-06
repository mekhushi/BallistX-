import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import pickle


class TrajectoryNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(5, 64),
            nn.ReLU(),
            nn.Linear(64, 64),
            nn.ReLU(),
            nn.Linear(64, 2)
        )
    def forward(self, x):
        return self.model(x)


@st.cache_resource
def load_model_and_scalers():
    model = TrajectoryNet()
    model.load_state_dict(torch.load('model.pth', map_location='cpu'))
    model.eval()
    with open('scaler_x.pkl', 'rb') as f:
        scaler_x = pickle.load(f)
    with open('scaler_y.pkl', 'rb') as f:
        scaler_y = pickle.load(f)
    return model, scaler_x, scaler_y


st.title("🚀 Ballistics Simulator")

# Physics constants
g = 9.81
rho = 1.225
Cd = 0.47
A = 0.01
dt = 0.01

def simulate_trajectory(v0, angle_deg, mass, wind_speed=0):
    angle = np.radians(angle_deg)
    vx = v0 * np.cos(angle)
    vy = v0 * np.sin(angle)
    x, y = 0, 0
    traj = []
    while y >= 0:
        v = np.sqrt((vx - wind_speed)**2 + vy**2)
        drag_force = 0.5 * rho * Cd * A * v**2
        drag_acc_x = drag_force * (vx - wind_speed) / v / mass if v != 0 else 0
        drag_acc_y = drag_force * vy / v / mass if v != 0 else 0
        ax = -drag_acc_x
        ay = -g - drag_acc_y
        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt
        traj.append((x, y))
    return np.array(traj)


model, scaler_x, scaler_y = load_model_and_scalers()

col1, col2 = st.columns(2)

with col1:
    v0 = st.slider("Initial Velocity (m/s)", 20.0, 100.0, 50.0)
    angle = st.slider("Launch Angle (degrees)", 15, 75, 45)
    mass = st.slider("Mass (kg)", 0.1, 5.0, 1.0)
    wind = st.slider("Wind Speed (m/s)", -10.0, 10.0, 0.0)

with col2:
    st.markdown("""
    ### Parameter Explanation

    - **Initial Velocity:** Speed of the projectile at launch.
    - **Launch Angle:** Angle from the horizontal plane.
    - **Mass:** Mass of the projectile.
    - **Wind Speed:** Speed of wind affecting the projectile.
    """)

physics_traj = simulate_trajectory(v0, angle, mass, wind)

times = np.arange(0, len(physics_traj)*dt, dt)

ml_preds = []
for t in times:
    x_in = np.array([[v0, angle, mass, wind, t]])
    x_scaled = scaler_x.transform(x_in)
    x_tensor = torch.tensor(x_scaled, dtype=torch.float32)
    with torch.no_grad():
        y_pred = model(x_tensor).numpy()
    y_orig = scaler_y.inverse_transform(y_pred)[0]
    ml_preds.append(y_orig)
ml_preds = np.array(ml_preds)

fig, ax = plt.subplots(figsize=(10,6))
ax.plot(physics_traj[:,0], physics_traj[:,1], label='Physics Simulation', linewidth=2)
ax.plot(ml_preds[:,0], ml_preds[:,1], label='ML Prediction', linestyle='--')
ax.set_xlabel('X Position (m)')
ax.set_ylabel('Y Position (m)')
ax.set_title('Projectile Trajectory')
ax.legend()
ax.grid(True)
st.pyplot(fig)
