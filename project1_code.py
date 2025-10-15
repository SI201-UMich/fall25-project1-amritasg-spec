# -------------------------------------------------------------
# Name: Amrita Gujarati 
# Student ID: 26505868
# Email: amritasg@umich.edu
# Collaborators: Amrita Gujarati, Anna DeWitt, Willow Tonelli
# AI Tools Used: ChatGPT (for debugging guidance and code review)
# Functions created by Anna:
# Functions created by Amrita:
# Functions created by Willow:
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

def get_length(penguins, species):
  return [penguin['bill_length_mm'] for penguin in penguins if penguin['species'] == species.lower()]

def avg_bill_length_by_sex(penguins):
    species_list = ['Adelie', 'Chinstrap', 'Gentoo']
    averages = {}
    for species in species_list:
        for sex in ['male', 'female']:
            lengths = [float(p['bill_length_mm']) for p in penguins
                       if p['species'] == species and p['sex'] == sex]
            if lengths:
                averages[f"{species}_{sex}"] = sum(lengths) / len(lengths)
    return averages

def avg_flipper_length(penguins):
  species_list = ['adelie', 'chinstrap', 'gentoo']
  averages = {}
  for species in species_list:
    lengths = get_length(penguins, species)
    averages[species] = sum(map(float, lengths)) / len(lengths)
  return averages