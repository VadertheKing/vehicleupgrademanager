import glob

# Get a list of all files ending in .txt in the current directory
files = glob.glob("./*.txt")

# Open a new file for writing
with open('concatenated_output.txt', 'w') as outfile:
    # Iterate over all files and copy their contents to the output file
    for f in files:
        with open(f, 'r') as infile:
            outfile.write(infile.read())