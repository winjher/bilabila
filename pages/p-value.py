import pandas as pd
from scipy.stats import ttest_ind

# Data
data = pd.DataFrame({
    'Species': ['Batwing', 'Atlas Moth', 'Red Lacewing', 'Common Mime', 'Plain Tiger', 'Tailed Jay', 
                'Common Jay', 'Great Eggfly', 'Paper Kite', 'Pink Rose', 'Common Lime', 
                'Emerald Swallowtail', 'Great Yellow Mormon', 'Common Mormon', 'Scarlet Mormon', 
                'Giant Silk Moth', 'Clipper', 'Golden Birdwing'],
    'Total_Inspected': [150, 200, 120, 170, 130, 160, 180, 140, 190, 155, 165, 175, 185, 195, 
                        135, 145, 125, 210],
    'Defects_Detected': [5, 10, 4, 7, 3, 6, 9, 5, 8, 7, 6, 4, 5, 8, 3, 6, 2, 9]
})

# Add Correct Classification column
data['Correct_Classification'] = data['Total_Inspected'] - data['Defects_Detected']

# Perform t-test
correct_classifications = data['Correct_Classification']
incorrect_classifications = data['Defects_Detected']
t_stat, p_value = ttest_ind(correct_classifications, incorrect_classifications)

print("t-statistic:", t_stat)
print("p-value:", p_value)

# Interpretation of p-value
if p_value < 0.05:
    print("There is a significant difference in classification between species.")
else:
    print("No significant difference found in classification between species.")
