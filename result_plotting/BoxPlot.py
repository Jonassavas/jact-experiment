import pandas as pd
import matplotlib.pyplot as plt
import os

# Function to process a CSV file and calculate coverage percentage
def process_csv(file_path):
    try:
        # Read data from CSV file
        data = pd.read_csv(file_path)

        # Check if 'DIRECT_DEPENDENCY' column contains string values
        if data['DIRECT_DEPENDENCY'].dtype == 'object':
            # Convert 'DIRECT_DEPENDENCY' values to lowercase
            data['DIRECT_DEPENDENCY'] = data['DIRECT_DEPENDENCY'].str.lower()

        # Filter data where DIRECT_DEPENDENCY is true
        filtered_data = data[data['DIRECT_DEPENDENCY']].copy()

        # Convert INSTRUCTION_COVERED and INSTRUCTION_TOTAL to numeric
        filtered_data['INSTRUCTION_COVERED'] = pd.to_numeric(filtered_data['INSTRUCTION_COVERED'], errors='coerce')
        filtered_data['INSTRUCTION_TOTAL'] = pd.to_numeric(filtered_data['INSTRUCTION_TOTAL'], errors='coerce')

        # Calculate the coverage percentage only if both INSTRUCTION_COVERED and INSTRUCTION_TOTAL are numeric
        filtered_data['Coverage_Percentage'] = filtered_data.apply(lambda row: row['INSTRUCTION_COVERED'] / row['INSTRUCTION_TOTAL'] * 100
                                                                if pd.notnull(row['INSTRUCTION_COVERED']) and pd.notnull(row['INSTRUCTION_TOTAL'])
                                                                else pd.NA, axis=1)

        # Drop rows where Coverage_Percentage is NA
        filtered_data = filtered_data.dropna(subset=['Coverage_Percentage'])

        # Get the name of the CSV file without extension
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        return filtered_data, file_name

    except pd.errors.EmptyDataError:
        print(f"The CSV file '{file_path}' is empty or doesn't contain any data.")
        return None, None
    except FileNotFoundError:
        print(f"The CSV file '{file_path}' was not found.")
        return None, None

# List CSV files in the ./csv_files directory
csv_files = [f'csv_files/{file}' for file in os.listdir('csv_files') if file.endswith('.csv')]

# Process each CSV file and collect data
data_list = []
file_names = []
for file_path in csv_files:
    data, file_name = process_csv(file_path)
    if data is not None:
        data_list.append(data)
        file_names.append(file_name)

# Sort file names alphabetically in reverse order, ignoring case
file_names.sort(key=str.lower, reverse=True)

# Create boxplot
fig, ax = plt.subplots(figsize=(10, 7))

# Plot the data for each CSV file with different colors
colors = plt.cm.tab10.colors
num_colors = len(colors)
for i, data in enumerate(data_list):
    color = colors[i % num_colors]  # Cycling through colors if there are more CSV files than available colors
    ax.boxplot(data['Coverage_Percentage'], vert=False, positions=[i], widths=0.6, boxprops=dict(color=color))

# Set y-axis labels to file names
ax.set_yticks(range(len(data_list)))
ax.set_yticklabels(file_names)

# Set x-axis label and limits
ax.set_xlabel('Instruction Coverage (%)')
ax.set_xlim(0, 100)

# Set title
ax.set_title('Direct Dependency Coverage')

# Save plot as an image file
plt.savefig('boxplot.png', bbox_inches='tight')

# Optionally, you can specify the DPI (dots per inch) for better resolution
# plt.savefig('boxplot.png', dpi=300)

# Optionally, you can specify the file format (e.g., PDF, SVG) by changing the file extension
# plt.savefig('boxplot.pdf')

# Optionally, you can specify additional parameters such as bbox_inches and pad_inches to adjust the bounding box and padding

# Optionally, you can close the plot to release memory
plt.close()
