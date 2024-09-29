import numpy as np
import matplotlib.pyplot as plt

# Projects
projects = ['classgraph', 'commons-validator', 'guice', 'immutables', 
            'java-faker', 'modelmapper', 'tablesaw', 'tika', 'woodstox']

# Categories
categories = ['Interfaces', 'Abstract Classes', 'Enums', 'Annotations', 'Synthetic Classes', 'Regular Classes']
n_categories = len(categories)

# Data array where each row corresponds to a project, and each column corresponds to a category
# DEPTRIM MISMATCH TYPES
# data = np.array([
#     [0, 0, 0, 0, 0, 0],   # classgraph
#     [0, 0, 0, 0, 0, 0],   # commons-validator
#     [0, 3, 1, 0, 0, 8],   # guice
#     [3, 10, 4, 0, 0, 48],   # helidon
#     [0, 0, 0, 0, 0, 2],   # immutables
#     [0, 0, 0, 0, 0, 0],   # java-faker
#     [1, 22, 12, 0, 0, 236],   # jcabi-github
#     [0, 0, 0, 0, 0, 1],   # jooby
#     [2, 4, 32, 0, 0, 33],   # modelmapper
#     [0, 8, 0, 0, 0, 242],   # poi-tl
#     [0, 2, 6, 0, 0, 14],   # tablesaw
#     [0, 0, 0, 0, 0, 0],   # tika
#     [0, 2, 0, 0, 0, 5]    # woodstox
# ])

# JACT FOUND TYPES
# data = np.array([
#     [1, 20, 1, 0, 0, 136],   # classgraph
#     [0, 51, 0, 0, 0, 639],   # commons-validator
#     [8, 266, 122, 0, 0, 1498],   # guice
#     [172, 272, 151, 0, 0, 3013],   # helidon
#     [0, 18, 12, 0, 0, 182],   # immutables
#     [0, 35, 21, 0, 0, 402],   # java-faker
#     [68, 483, 194, 0, 0, 4084],   # jcabi-github
#     [60, 328, 175, 0, 0, 5240],   # jooby
#     [28, 233, 559, 0, 0, 1363],   # modelmapper
#     [1429, 653, 361, 0, 0, 8088],   # poi-tl
#     [5, 174, 69, 0, 0, 989],   # tablesaw
#     [7, 13, 5, 0, 0, 200],   # tika
#     [1, 97, 0, 0, 0, 663]    # woodstox
# ])

# JACT TOTAL TYPES
# dataTotal = np.array([
#     [62, 20, 1, 0, 2, 137],             # classgraph
#     [48, 52, 0, 25, 2, 653],            # commons-validator
#     [134, 271, 122, 377, 63, 1506],     # guice
#     [613, 272, 151, 82, 168, 3071],     # helidon
#     [57, 18, 12, 32, 3, 184],           # immutables
#     [26, 35, 22, 3, 15, 405],           # java-faker
#     [758, 489, 194, 546, 123, 4106],    # jcabi-github
#     [621, 338, 175, 151, 157, 5494],    # jooby
#     [858, 597, 197, 208, 219, 8281],    # lettuce
#     [431, 233, 559, 60, 50, 1364],      # modelmapper
#     [2751, 654, 361, 8, 256, 8103],     # poi-tl
#     [100, 175, 69, 54, 54, 991],        # tablesaw
#     [27, 13, 5, 1, 6, 200],             # tika
#     [93, 97, 0, 0, 7, 666]              # woodstox
# ])

dataFound = np.array([
    [1890, 3235, 1852, 0, 0, 34595]
])

dataTotal = np.array([
    [6597, 3264, 1868, 1547, 1125, 35161]
])

# Define colors for each project (switching to a higher-contrast colormap)
cmap = plt.get_cmap('tab10')  # 'tab10' provides better contrast for clearer distinctions
colors = cmap(np.linspace(0, 1, len(projects)))  # Generate 9 distinct colors from the colormap

# Define width of a single bar and the position offset
bar_width = 0.09  # Increased width of each bar for better readability
x = np.arange(n_categories)  # Base positions for categories

# Create the grouped bar chart
fig, ax = plt.subplots(figsize=(10, 6))

# Plot bars for each project, offsetting their position within each category
for i in range(len(projects)):
    ax.bar(x + i * bar_width, data[i], width=bar_width, color=colors[i], label=projects[i])

# Add labels and title
ax.set_ylabel('#Missing Class Files')
#ax.set_title('JACT/DepTrim Mismatch Class Types')
#ax.set_title('JACT: Included Class Types')
ax.set_title('JACT: Missing Class Types')

# Modify x-tick labels to have newlines
ax.set_xticks(x + bar_width * (len(projects) - 1) / 2)  # Center the tick labels
ax.set_xticklabels(['Interfaces', 'Abstract\nClasses', 'Enums', 'Annotations', 
                    'Synthetic\nClasses', 'Regular\nClasses'])  # Insert newline for multi-word categories

# Add a vertical dotted line between categories, shifting by a small margin to avoid overlap
for i in range(1, len(categories)):
    ax.axvline(i - 0.14, color='black', linestyle='--', linewidth=1)  # Adjusted for better spacing

# Add grid lines (apply only to the y-axis to avoid clutter)
ax.grid(True, axis='y', linestyle='-', color='gray', alpha=0.7)

# Add a legend to indicate which color corresponds to which project
ax.legend(title="Projects", bbox_to_anchor=(1.05, 1), loc='upper left')

# Display the plot
plt.tight_layout()
plt.savefig('grouped_bar_chart_with_grid_enhanced_colors.png', dpi=300)
# plt.show()  # Uncomment if you're in an interactive environment
