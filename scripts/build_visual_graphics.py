import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

target_dir = "work/week-03-visual-identity/selected_images"
os.makedirs(target_dir, exist_ok=True)

# Set style for minimal dark technical graphics
plt.style.use('dark_background')
fig_bg = '#11111b'
card_bg = '#181825'
text_color = '#cdd6f4'
primary_blue = '#89b4fa'
accent_green = '#a6e3a1'
accent_red = '#f38ba8'

# --- 1. hero_architecture.png ---
fig, ax = plt.subplots(figsize=(10, 5.625), dpi=150) # 16:9 aspect ratio
fig.patch.set_facecolor(fig_bg)
ax.set_facecolor(fig_bg)

ax.axis('off')

# Title
ax.text(0.5, 0.92, 'SYSTEM ARCHITECTURE: RESEARCH & INFERENCE PIPELINE', 
        ha='center', va='center', color=primary_blue, fontsize=13, fontweight='bold', family='monospace')
ax.text(0.5, 0.86, 'Streaming Data -> Feature Extraction -> ML Model Engine -> Priority Review Queue', 
        ha='center', va='center', color='#a6adc8', fontsize=9, family='monospace')

boxes = [
    ("1. DATA SOURCES", "Streaming Logs\n30k Page Records\nSearch Console", 0.12, 0.5),
    ("2. FEATURE FRAME", "Interaction Signals\nPosition Tiers\nCTR Gap & Freshness", 0.37, 0.5),
    ("3. MODEL ENGINE", "PyTorch Autoencoder\nRandom Forest\nGroupShuffleSplit", 0.62, 0.5),
    ("4. OUTPUT QUEUE", "Precision@50 Queue\nRanked Decline Risks\nEditorial Action", 0.87, 0.5)
]

for title, sub, x, y in boxes:
    rect = patches.FancyBboxPatch((x-0.11, y-0.2), 0.22, 0.4, 
                                 boxstyle="round,pad=0.01,rounding_size=0.02",
                                 facecolor=card_bg, edgecolor=primary_blue, linewidth=1.5)
    ax.add_patch(rect)
    ax.text(x, y+0.1, title, ha='center', va='center', color=accent_green, fontsize=9.5, fontweight='bold', family='sans-serif')
    ax.text(x, y-0.05, sub, ha='center', va='center', color=text_color, fontsize=8, family='monospace', multialignment='center')

arrow_props = dict(arrowstyle='->', color=primary_blue, lw=2)
ax.annotate('', xy=(0.25, 0.5), xytext=(0.23, 0.5), arrowprops=arrow_props)
ax.annotate('', xy=(0.50, 0.5), xytext=(0.48, 0.5), arrowprops=arrow_props)
ax.annotate('', xy=(0.75, 0.5), xytext=(0.73, 0.5), arrowprops=arrow_props)

plt.tight_layout()
hero_path = os.path.join(target_dir, "hero_architecture.png")
plt.savefig(hero_path, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
plt.close()
print(f"Generated {hero_path}")

# --- 2. project_aegis_diagram.png ---
fig, ax = plt.subplots(figsize=(10, 5.625), dpi=150) # 16:9 aspect ratio
fig.patch.set_facecolor(fig_bg)
ax.set_facecolor(card_bg)

np.random.seed(42)
benign_mse = np.random.exponential(scale=0.08, size=300)
anomaly_mse = np.random.normal(loc=0.65, scale=0.12, size=50)

ax.hist(benign_mse, bins=30, alpha=0.75, color=primary_blue, label='Benign Events (Normal Traffic)', density=True)
ax.hist(anomaly_mse, bins=20, alpha=0.75, color=accent_red, label='Security Anomalies (Injection Threats)', density=True)

tau = 0.35
ax.axvline(tau, color=accent_green, linestyle='--', linewidth=2, label=f'Anomaly Threshold (tau = {tau})')

ax.set_title('PROJECT AEGIS: AUTOENCODER RECONSTRUCTION LOSS DISTRIBUTION (MSE)', 
             color=primary_blue, fontsize=11, fontweight='bold', pad=12, family='monospace')
ax.set_xlabel('Reconstruction Error (Mean Squared Error)', color=text_color, fontsize=9.5, family='sans-serif')
ax.set_ylabel('Probability Density', color=text_color, fontsize=9.5, family='sans-serif')
ax.tick_params(colors=text_color)
ax.grid(True, linestyle=':', alpha=0.3, color='#45475a')
ax.legend(facecolor=card_bg, edgecolor='#313244', labelcolor=text_color, loc='upper right')

ax.annotate('Flagged Anomalies\n(MSE > tau)', xy=(0.55, 1.2), xytext=(0.65, 2.5),
            arrowprops=dict(facecolor=accent_red, shrink=0.05, width=1, headwidth=6),
            color=accent_red, fontweight='bold', fontsize=8.5)

plt.tight_layout()
aegis_path = os.path.join(target_dir, "project_aegis_diagram.png")
plt.savefig(aegis_path, facecolor=fig.get_facecolor(), edgecolor='none', bbox_inches='tight')
plt.close()
print(f"Generated {aegis_path}")
