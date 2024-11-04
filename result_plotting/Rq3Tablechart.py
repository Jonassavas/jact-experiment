import numpy as np
import matplotlib.pyplot as plt

# Categories
categories = ['Interfaces', 'Abstract Classes', 'Enums', 'Annotations', 
              'Synthetic Classes', 'Regular Classes']
n_categories = len(categories)

# Data arrays
dataFound = np.array([1890, 3235, 1852, 0, 0, 34595])  # Found data
dataTotal = np.array([6597, 3264, 1868, 1547, 1125, 35161])  # Total data

# Define width of a single bar
bar_width = 0.6  # Wider bar for better visibility
x = np.arange(n_categories)  # Base positions for categories

# Create the bar chart
fig, ax = plt.subplots(figsize=(10, 6))

# Define a new color palette with a light blue for regular classes
colors = ['#4a86e8', '#8e7cc3', '#c4a484', '#6aa84f', '#e06666', '#f6b26b']  # Softer blue, purple, orange, green, pink, light blue

# Plot the total data with hatching for each category
for i in range(n_categories):
    ax.bar(x[i], dataTotal[i], width=bar_width, color='white', edgecolor=colors[i], 
           hatch='//', alpha=0.9)

# Plot the found data (solid color) over the total for each category
for i in range(n_categories):
    ax.bar(x[i], dataFound[i], width=bar_width, color=colors[i])

# Add labels and title with increased font size
ax.set_ylabel('# of Class Files (Log Scale)', fontsize=16, labelpad=15)  # Shift y-label to the left
#ax.set_title('JACT: Included vs Total Classes by Type', fontsize=18, pad=15)  # Increased padding for title

# Apply a log scale to the y-axis
ax.set_yscale('log')

# Modify x-tick labels to have newlines and increase tick label font size
ax.set_xticks(x)
ax.set_xticklabels(['Interfaces', 'Abstract\nClasses', 'Enums', 'Annotations', 
                    'Synthetic\nClasses', 'Regular\nClasses'], fontsize=14)  # Increased size for x-tick labels

# Remove vertical grid lines and introduce more detailed horizontal grid lines
ax.grid(True, which='both', axis='y', linestyle='--', color='gray', alpha=0.5)
ax.grid(False, axis='x')  # Disable grid on x-axis

# Add more numbers on the y-axis for detailed scaling
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: '{:.0f}'.format(y)))  # Force display of integer labels
ax.yaxis.set_major_locator(plt.LogLocator(base=10.0, subs=np.arange(1.0, 10.0), numticks=10))  # More y-axis ticks

# Increase font size for y-tick labels
ax.tick_params(axis='y', labelsize=10)  # Increase size of y-tick labels

# Display the plot
plt.tight_layout()
plt.savefig('log_scaled_chart_with_lightblue_regular_classes_shifted_title.png', dpi=300)
# plt.show()  # Uncomment if you're in an interactive environment
