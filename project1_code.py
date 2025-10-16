# -------------------------------------------------------------
# Name: Amrita Gujarati 
# Student ID: 26505868
# Email: amritasg@umich.edu
# Collaborators: Amrita Gujarati, Anna DeWitt, Willow Tonelli
# AI Tools Used: ChatGPT (for debugging guidance and code review)
# Functions created by Anna: 1 and 2
# Functions created by Amrita: 5 and 6 
# Functions created by Willow: 3 and 4
# we all collaborated on the functions, it wasn't just individual work. 
# Dataset: Palmer Penguins (Kaggle)
# -------------------------------------------------------------


import csv

def load_penguin(csv_file):
    penguins = []
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            penguins.append(row)
    return penguins


def safe_float(value):
    try:
        if value is None or value == "" or str(value).upper() == "NA":
            return None
        return float(value)
    except ValueError:
        return None


def avg_bill_length_by_sex(penguins):
  
    species_list = ['Adelie', 'Chinstrap', 'Gentoo']
    sexes = ['male', 'female']
    averages = {}
    for species in species_list:
        for sex in sexes:
            values = []
            for p in penguins:
                if p['species'] == species and p['sex'].lower() == sex:
                    val = safe_float(p['bill_length_mm'])
                    if val is not None:
                        values.append(val)
            if values:
                averages[f'{species}_{sex}'] = round(sum(values) / len(values), 2)
    return averages


def avg_flipper_length_by_island(penguins):
  
    species_list = ['Adelie', 'Chinstrap', 'Gentoo']
    islands = set(p['island'] for p in penguins if p.get('island'))
    averages = {}
    for species in species_list:
        for island in islands:
            values = []
            for p in penguins:
                if p['species'] == species and p['island'] == island:
                    val = safe_float(p['flipper_length_mm'])
                    if val is not None:
                        values.append(val)
            if values:
                averages[f'{species}_{island}'] = round(sum(values) / len(values), 2)
    return averages


def avg_body_mass_by_island_and_sex(penguins):
  
    islands = set(p['island'] for p in penguins if p.get('island'))
    sexes = ['male', 'female']
    averages = {}
    for island in islands:
        for sex in sexes:
            masses = []
            for p in penguins:
                if p.get('island') == island and p.get('sex') == sex:
                    val = safe_float(p['body_mass_g'])
                    if val is not None:
                        masses.append(val)
            if masses:
                averages[f'{island}_{sex}'] = round(sum(masses) / len(masses), 2)
    return averages


def percent_heavy_penguins_by_species(penguins, threshold=5000):
   
    species_list = set(p['species'] for p in penguins)
    percentages = {}
    for species in species_list:
        weights = []
        for p in penguins:
            if p['species'] == species:
                val = safe_float(p['body_mass_g'])
                if val is not None:
                    weights.append(val)
        if weights:
            heavy = [w for w in weights if w > threshold]
            percentages[species] = round(len(heavy) / len(weights) * 100, 1)
    return percentages


def avg_bill_depth_by_island_and_species(penguins):
    
    species_list = set(p['species'] for p in penguins)
    islands = set(p['island'] for p in penguins if p.get('island'))
    averages = {}
    for species in species_list:
        for island in islands:
            depths = []
            for p in penguins:
                if p['species'] == species and p['island'] == island:
                    val = safe_float(p['bill_depth_mm'])
                    if val is not None:
                        depths.append(val)
            if depths:
                averages[f'{species}_{island}'] = round(sum(depths) / len(depths), 2)
    return averages


def sex_ratio_by_species(penguins):
   
    species_list = set(p['species'] for p in penguins)
    ratios = {}
    for species in species_list:
        males = len([p for p in penguins if p['species'] == species and p['sex'].lower() == 'male'])
        females = len([p for p in penguins if p['species'] == species and p['sex'].lower() == 'female'])
        if females > 0:
            ratios[species] = round(males / females, 2)
    return ratios


def max_average(averages):
    
    if not averages:
        return ("None", 0)
    max_key = max(averages, key=averages.get)
    return (max_key, averages[max_key])


def generate_report(results):
  
    with open("penguin_report.txt", "w") as f:
        f.write("🐧 Penguin Data Analysis Report\n")
        f.write("==================================\n\n")

        for title, data in results.items():
            f.write(f"{title}:\n")
            for k, v in data.items():
                f.write(f"  {k}: {v}\n")
            f.write("\n")

        if "Average Bill Length by Sex" in results:
            bill_max = max_average(results["Average Bill Length by Sex"])
            f.write(f"Highest Average Bill Length: {bill_max[0]} ({bill_max[1]} mm)\n")

        if "Average Flipper Length by Island" in results:
            flip_max = max_average(results["Average Flipper Length by Island"])
            f.write(f"Highest Average Flipper Length: {flip_max[0]} ({flip_max[1]} mm)\n")

    print('Report generated: "penguin_report.txt"!')


def main():
    penguins = load_penguin('/Users/amritagujarati/Desktop/SI 201/fall25-project1-amritasg-spec/penguins.csv')

    bill_avg = avg_bill_length_by_sex(penguins)
    flipper_avg = avg_flipper_length_by_island(penguins)
    body_mass_avg = avg_body_mass_by_island_and_sex(penguins)
    heavy_pct = percent_heavy_penguins_by_species(penguins)
    bill_depth_avg = avg_bill_depth_by_island_and_species(penguins)
    sex_ratio = sex_ratio_by_species(penguins)

    results = {
        "Average Bill Length by Sex": bill_avg,
        "Average Flipper Length by Island": flipper_avg,
        "Average Body Mass by Island and Sex": body_mass_avg,
        "Percent Heavy Penguins by Species": heavy_pct,
        "Average Bill Depth by Island and Species": bill_depth_avg,
        "Sex Ratio by Species": sex_ratio
    }

    generate_report(results)


import unittest

class TestFunctions(unittest.TestCase):

    def setUp(self):
        self.data = [
            {"species": "Adelie", "bill_length_mm": "40.1", "bill_depth_mm": "18.7",
             "flipper_length_mm": "181", "body_mass_g": "3750", "sex": "male", "island": "Torgersen"},
            {"species": "Adelie", "bill_length_mm": "37.8", "bill_depth_mm": "18.4",
             "flipper_length_mm": "180", "body_mass_g": "3700", "sex": "female", "island": "Torgersen"},
            {"species": "Gentoo", "bill_length_mm": "47.3", "bill_depth_mm": "15.3",
             "flipper_length_mm": "217", "body_mass_g": "5050", "sex": "male", "island": "Biscoe"},
            {"species": "Adelie", "bill_length_mm": "NA", "bill_depth_mm": "NA",
             "flipper_length_mm": "NA", "body_mass_g": "NA", "sex": "male", "island": "Torgersen"}
        ]

    def test_avg_bill_length_by_sex(self):
        result = avg_bill_length_by_sex(self.data)
        self.assertAlmostEqual(result['Adelie_male'], 40.1)
        self.assertAlmostEqual(result['Adelie_female'], 37.8)

    def test_percent_heavy_penguins_by_species(self):
        result = percent_heavy_penguins_by_species(self.data, threshold=4000)
        self.assertIn('Gentoo', result)
        self.assertTrue(result['Gentoo'] > 0)

    def test_sex_ratio_by_species(self):
        result = sex_ratio_by_species(self.data)
        self.assertIn('Adelie', result)
        self.assertAlmostEqual(result['Adelie'], 2.0)

    def test_avg_body_mass_by_island_and_sex(self):
        result = avg_body_mass_by_island_and_sex(self.data)
        self.assertIn('Torgersen_male', result)
        self.assertAlmostEqual(result['Torgersen_male'], 3750)


if __name__ == "__main__":
    main()
    unittest.main(exit=False) 
