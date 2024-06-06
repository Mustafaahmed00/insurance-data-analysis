import pandas as pd
from statistics import median

# Load the CSV file into a DataFrame
file_path = 'insurance.csv'
insurance_data = pd.read_csv(file_path)

# Load the data from the DataFrame into lists
ages = insurance_data['age'].tolist()
sexes = insurance_data['sex'].tolist()
bmis = insurance_data['bmi'].tolist()
num_children = insurance_data['children'].tolist()
smoker_statuses = insurance_data['smoker'].tolist()
regions = insurance_data['region'].tolist()
insurance_charges = insurance_data['charges'].tolist()

class PatientsInfo:
    def __init__(self, patients_ages, patients_sexes, patients_bmis, patients_num_children, 
                 patients_smoker_statuses, patients_regions, patients_charges):
        self.patients_ages = patients_ages
        self.patients_sexes = patients_sexes
        self.patients_bmis = patients_bmis
        self.patients_num_children = patients_num_children
        self.patients_smoker_statuses = patients_smoker_statuses
        self.patients_regions = patients_regions
        self.patients_charges = patients_charges

    def analyze_ages(self):
        total_age = sum(self.patients_ages)
        return ("Average Patient Age: " + str(round(total_age / len(self.patients_ages), 2)) + " years")

    def analyze_sexes(self):
        females = self.patients_sexes.count('female')
        males = self.patients_sexes.count('male')
        return f"Number of females: {females}\nNumber of males: {males}"

    def unique_regions(self):
        return list(set(self.patients_regions))

    def average_charges(self):
        total_charges = sum(self.patients_charges)
        return ("Average Yearly Medical Insurance Charges: " +  
                str(round(total_charges / len(self.patients_charges), 2)) + " dollars.")
    
    def create_dictionary(self):
        self.patients_dictionary = {
            "age": self.patients_ages,
            "sex": self.patients_sexes,
            "bmi": self.patients_bmis,
            "children": self.patients_num_children,
            "smoker": self.patients_smoker_statuses,
            "regions": self.patients_regions,
            "charges": self.patients_charges
        }
        return self.patients_dictionary

    def analyze_bmi(self):
        total_bmi = sum(self.patients_bmis)
        return ("Average BMI: " + str(round(total_bmi / len(self.patients_bmis), 2)))
    
    def bmi_categories(self):
        underweight = 0
        normal_weight = 0
        overweight = 0
        obese = 0
        
        for bmi in self.patients_bmis:
            if bmi < 18.5:
                underweight += 1
            elif 18.5 <= bmi < 24.9:
                normal_weight += 1
            elif 25 <= bmi < 29.9:
                overweight += 1
            else:
                obese += 1
        
        return {
            "Underweight": underweight,
            "Normal weight": normal_weight,
            "Overweight": overweight,
            "Obese": obese
        }

    def analyze_children(self):
        total_children = sum(self.patients_num_children)
        return ("Average Number of Children: " + str(round(total_children / len(self.patients_num_children), 2)))
    
    def smoker_statuses_analysis(self):
        smokers = self.patients_smoker_statuses.count('yes')
        non_smokers = self.patients_smoker_statuses.count('no')
        return f"Number of smokers: {smokers}\nNumber of non-smokers: {non_smokers}"

    def compare_smoker_charges(self):
        smoker_charges = [charge for i, charge in enumerate(self.patients_charges) if self.patients_smoker_statuses[i] == 'yes']
        non_smoker_charges = [charge for i, charge in enumerate(self.patients_charges) if self.patients_smoker_statuses[i] == 'no']
        avg_smoker_charges = round(sum(smoker_charges) / len(smoker_charges), 2) if smoker_charges else 0
        avg_non_smoker_charges = round(sum(non_smoker_charges) / len(non_smoker_charges), 2) if non_smoker_charges else 0
        return f"Average Charges for Smokers: {avg_smoker_charges} dollars\nAverage Charges for Non-Smokers: {avg_non_smoker_charges} dollars"

    def max_min_charges(self):
        return f"Maximum Charges: {max(self.patients_charges)} dollars\nMinimum Charges: {min(self.patients_charges)} dollars"

    def median_charges(self):
        med = median(self.patients_charges)
        return f"Median Charges: {med} dollars"

    def region_charges(self):
        region_charge_dict = {}
        for region in set(self.patients_regions):
            region_charges = [charge for i, charge in enumerate(self.patients_charges) if self.patients_regions[i] == region]
            region_charge_dict[region] = round(sum(region_charges) / len(region_charges), 2)
        return region_charge_dict

    def region_distribution(self):
        region_dist = {region: self.patients_regions.count(region) for region in set(self.patients_regions)}
        return region_dist
    
# Instantiate the class and call its methods
patient_info = PatientsInfo(ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges)
print(patient_info.analyze_ages())
print(patient_info.analyze_sexes())
print("Unique regions:", patient_info.unique_regions())
print(patient_info.average_charges())
print("Patient dictionary:", patient_info.create_dictionary())
print(patient_info.analyze_bmi())
print("BMI categories:", patient_info.bmi_categories())
print(patient_info.analyze_children())
print(patient_info.smoker_statuses_analysis())
print(patient_info.compare_smoker_charges())
print(patient_info.max_min_charges())
print(patient_info.median_charges())
print("Average charges per region:", patient_info.region_charges())
print("Region distribution:", patient_info.region_distribution())
