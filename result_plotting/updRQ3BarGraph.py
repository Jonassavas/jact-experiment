import numpy as np
import matplotlib.pyplot as plt

# Categories
categories = ['Interfaces', 'Abstract Classes', 'Enums', 'Annotations', 
              'Synthetic Classes', 'Regular Classes']
n_categories = len(categories)

# Data arrays
#dataFound = np.array([4313, 1368, 940, 339, 625, 18257])  # Found data
dataFound = np.array([1890, 3235, 1852, 0, 0, 34595])  # Found data
dataTotal = np.array([6417, 3264, 1867, 1547, 1117, 35165])  # Total data

# Define width of a single bar
bar_width = 0.6  # Wider bar for better visibility
x = np.arange(n_categories)  # Base positions for categories

# Create the bar chart with a slightly taller figure (increased height by ~0.5cm)
fig, ax = plt.subplots(figsize=(10, 7.0))

# Define a new color palette with a light blue for regular classes
colors = ['#4a86e8', '#8e7cc3', '#c4a484', '#6aa84f', '#e06666', '#f6b26b']

# Plot the total data with hatching for each category
for i in range(n_categories):
    ax.bar(x[i], dataTotal[i], width=bar_width, color='white', edgecolor=colors[i], 
           hatch='//', alpha=0.9)

# Plot the found data (solid color) over the total for each category
for i in range(n_categories):
    ax.bar(x[i], dataFound[i], width=bar_width, color=colors[i])

# Add labels with increased font size
ax.set_ylabel('# of Class Files (Log Scale)', fontsize=16, labelpad=15)
#ax.set_title('JACT: Included vs Total Classes by Type', fontsize=18, pad=15)

# Apply a log scale to the y-axis
ax.set_yscale('log')

# Modify x-tick labels with newlines and increased font size
ax.set_xticks(x)
ax.set_xticklabels(['Interfaces', 'Abstract\nClasses', 'Enums', 'Annotations', 
                    'Synthetic\nClasses', 'Regular\nClasses'], fontsize=14)

# Remove vertical grid lines and add horizontal grid lines
ax.grid(True, which='both', axis='y', linestyle='--', color='gray', alpha=0.5)
ax.grid(False, axis='x')

# Manually set y-axis ticks:
# Ticks below 1000: every 100 units;
# Ticks from 1000 to 10000: every 1000 units; then 20000, 30000, 40000.
ticks = list(range(100, 1000, 100)) + list(range(1000, 11000, 1000)) + [20000, 30000, 40000]
ax.set_yticks(ticks)

# Set tick labels as strings.
labels = [f'{tick:.0f}' for tick in ticks]
ax.set_yticklabels(labels)

# Adjust tick label font sizes:
# Use a smaller font for ticks below 1000 and for certain ranges if needed.
for tick_val, label in zip(ticks, ax.get_yticklabels()):
    if tick_val < 1000 or (tick_val > 5000 and tick_val < 10000):
        label.set_fontsize(10)
    else:
        label.set_fontsize(10)

# Set consistent y-axis limits based solely on dataTotal
min_total = np.min(dataTotal[dataTotal > 0]) if np.any(dataTotal > 0) else 1
y_min = min_total
y_max = np.max(dataTotal)
ax.set_ylim(y_min * 0.2, y_max * 1.2)

# Display the plot
plt.tight_layout()
plt.savefig('log_scaled_chart_with_lightblue_regular_classes_shifted_title.png', dpi=300)
# plt.show()  # Uncomment if you're in an interactive environment
