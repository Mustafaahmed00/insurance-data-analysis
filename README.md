# Insurance Data Analysis

This project involves analyzing a dataset of insurance data to derive various insights. The dataset includes information about patients such as age, sex, BMI, number of children, smoking status, region, and insurance charges. The analysis is performed using Python, and the results provide a comprehensive overview of the data, including average values, distributions, and comparisons between different groups.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Methods and Analysis](#methods-and-analysis)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Installation

To run this project, you need to have Python installed on your system. You can install the necessary libraries using pip:

pip install pandas

## Usage

Clone the repository:

git clone https://github.com/Mustafaahmed00/insurance-data-analysis.git
cd insurance-data-analysis
Ensure you have the insurance.csv file in the project directory.

Run the analysis script:

python analysis.py
Methods and Analysis

## The PatientsInfo class contains several methods to analyze the insurance data:

- analyze_ages: Calculates and returns the average age of patients.
- analyze_sexes: Returns the number of male and female patients.
- unique_regions: Returns a list of unique regions.
- average_charges: Calculates and returns the average insurance charges.
- create_dictionary: Creates and returns a dictionary with all patients' data.
- analyze_bmi: Calculates and returns the average BMI.
- bmi_categories: Categorizes patients into BMI categories and returns the counts for each category.
- analyze_children: Calculates and returns the average number of children.
- smoker_statuses_analysis: Returns the number of smokers and non-smokers.
- compare_smoker_charges: Compares and returns the average charges for smokers and non-smokers.
- max_min_charges: Returns the maximum and minimum insurance charges.
- median_charges: Calculates and returns the median insurance charges.
- region_charges: Calculates and returns the average charges for each region.
- region_distribution: Returns the distribution of patients across different regions.

## Results
After running the analysis script, you will get a comprehensive output of the analyzed data. The results include:

- Average patient age
- Number of male and female patients
- List of unique regions
- Average yearly medical insurance charges
- Dictionary with all patients' data
- Average BMI and BMI categories
- Average number of children
- Number of smokers and non-smokers
- Comparison of average charges between smokers and non-smokers
- Maximum and minimum insurance charges
- Median insurance charges
- Average charges per region
- Distribution of patients across different regions

## Contributing
Contributions are welcome! Please open an issue to discuss what you would like to change or submit a pull request.
