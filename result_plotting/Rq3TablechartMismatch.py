import numpy as np
import matplotlib.pyplot as plt

# Categories
categories = ['Interfaces', 'Abstract Classes', 'Enums', 'Annotations', 
              'Synthetic Classes', 'Regular Classes']
n_categories = len(categories)

# Data arrays
#dataMismatch = np.array([9, 58, 60, 0, 0, 717])  # Mismatch data
dataMismatch = np.array([4313, 1368, 940, 339, 625, 18257])  # Mismatch data

# Define width of a single bar
bar_width = 0.6  # Wider bar for better visibility
x = np.arange(n_categories)  # Base positions for categories

# Create the bar chart
fig, ax = plt.subplots(figsize=(10, 6))

# Define a color palette
colors = ['#4a86e8', '#8e7cc3', '#c4a484', '#6aa84f', '#e06666', '#f6b26b']  # Softer colors

# Plot the mismatch data (solid color) for each category
for i in range(n_categories):
    ax.bar(x[i], dataMismatch[i], width=bar_width, color=colors[i])
    
    # Add the total number above each bar
    ax.text(x[i], dataMismatch[i] + 5, str(dataMismatch[i]), 
            ha='center', va='bottom', fontsize=12, color='black')

# Add labels and title with increased font size
ax.set_ylabel('# of Class Files', fontsize=16, labelpad=15)  # Shift y-label to the left
#ax.set_title('JACT vs DepTrim: Mismatched Classes by Type', fontsize=18, pad=20)  # Increased padding for title

# Modify x-tick labels to have newlines and increase tick label font size
ax.set_xticks(x)
ax.set_xticklabels(['Interfaces', 'Abstract\nClasses', 'Enums', 'Annotations', 
                    'Synthetic\nClasses', 'Regular\nClasses'], fontsize=14)  # Increased size for x-tick labels

# Introduce detailed horizontal grid lines
ax.grid(True, which='both', axis='y', linestyle='--', color='gray', alpha=0.5)
ax.grid(False, axis='x')  # Disable grid on x-axis

# Increase font size for y-tick labels
ax.tick_params(axis='y', labelsize=12)  # Increase size of y-tick labels

# Display the plot
plt.tight_layout()
plt.savefig('mismatched_classes_with_totals.png', dpi=300)
# plt.show()  # Uncomment if you're in an interactive environment
