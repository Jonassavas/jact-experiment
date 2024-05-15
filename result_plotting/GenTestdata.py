import os
import csv
import random

# List of dependency names
dependency_names = ['woodstox', 'undertow', 'tika', 'tablesaw', 'scibejava', 'RxRelay', 'Recaf', 'poi-tl', 'pf4j', 'pdfbox', 'OpenPDF', 'mybatis-3', 'modelmapper', 'lettuce', 'jooby', 'jimfs', 'java-faker', 'jacop', 'jacabi-github', 'immutables', 'httpcomponents', 'helidon-io', 'guice', 'graphhopper', 'flink', 'CoreNLP', 'commons-validator', 'classgraph', 'Chronicle-Map', 'checkstyle']

# Create directory if it doesn't exist
if not os.path.exists('csv_files'):
    os.makedirs('csv_files')

# Function to generate random data for a single CSV file
def generate_random_data(file_name):
    with open(f'csv_files/{file_name}.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['DEPENDENCY_ID', 'DIRECT_DEPENDENCY', 'INSTRUCTION_COVERED', 'INSTRUCTION_TOTAL', 'METHOD_COVERED', 'METHOD_TOTAL', 'CLASS_COVERED', 'CLASS_TOTAL'])
        
        for i in range(30):
            writer.writerow([
                f'dep_{i}',
                random.choice(['true', 'false']),
                random.randint(100, 1000),
                random.randint(1000, 2000),
                random.randint(10, 200),
                random.randint(500, 2000),
                random.randint(5, 200),
                random.randint(600, 2000)
            ])

# Generate random data for each dependency name
for dependency in dependency_names:
    generate_random_data(dependency)