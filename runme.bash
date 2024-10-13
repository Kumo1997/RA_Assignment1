#!/bin/bash

# Create a directory for plots if it doesn't exist
mkdir -p plots
mkdir -p results

# Clear the result file
echo "" > result.txt

# Run Assignment1.py 10 times, passing the iteration number with the correct flag
for i in {1..10}
do
    # Run the Python script and pass the iteration number as a command-line argument using the --iteration flag
    python3 Assignment1.py --iteration $i >> result.txt
done