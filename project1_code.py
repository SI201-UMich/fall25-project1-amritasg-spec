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