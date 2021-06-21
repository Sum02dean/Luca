import sys  # nopep8
import os  # nopep8
sys.path.append(os.path.abspath('../'))  # nopep8
from classes.luca import Luca  # nopep8
import pandas as pd
import argparse


# Get CML args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', default='Luca',
                    help="target string",
                    type=str)

parser.add_argument('-if', '--input_file', default='../../data/20210103_hundenamen.csv',
                    help="csv file containing dog_names under the field 'HUNDENAME'.",
                    type=str)

parser.add_argument('-of', '--output_file', default='../../data/filtered_hundenamen.csv',
                    help="csv file containing dog names under the field 'HUNDENAME'.",
                    type=str)


args = parser.parse_args()

# Run Code
x = pd.read_csv(args.input_file)
dog_names = x.HUNDENAME.values

# Call method
L = Luca(target=args.target)
filtered_names = L.compute_distance(dog_names)

# Save output as DataFrame
df = pd.DataFrame({'HUNDENAME': [x for x in filtered_names]})
df.to_csv(args.output_file, index=None)

# Print names to terminal
print(filtered_names)
