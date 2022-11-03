import csv
import os
import sys
import hashlib
import json
from pathlib import Path
FNAME = []
C = 0


def main():
    print("\nCreating json files...")
    fname = sys.argv[1]
    defaultJson(fname)


# TODO 1 : Input CSV file
# TODO 2 : Generate a JSON file per entry in team's sheet in CHIP-0007's default format

def defaultJson(f):
    global C

    with open(f, 'r') as file:
        os.mkdir("Json Files")
        FNAME.append(Path(f).stem)

        csvreader = csv.reader(file)

        for row in csvreader:

            if row[0] == 'Series Number' or row[0] == '':
                continue
            else:

                # TODO 2 : Generate a JSON file per entry in team's sheet in CHIP-0007's default format
                new_jsonFile = f"{row[1]}.json"
                json_data = {}

                json_data["format"] = "CHIP-0007"
                json_data["name"] = row[1]
                json_data["description"] = row[2]

                attribute_data = {}
                attribute_data["trait_type"] = "Gender"  # gender
                attribute_data["value"] = row[3]  # "value/male/female"

                json_data["attributes"] = [attribute_data]

                collection_data = {}
                collection_data["name"] = f"{row[1]} Collection"
                collection_data["id"] = row[0]  # "ID of the NFT collection"

                json_data["collection"] = collection_data

                filepath = f"Json Files/{new_jsonFile}"
                with open(filepath, 'w') as f:
                    json.dump(json_data, f, indent=2)
                    C += 1
                    sha256_hash = sha256_gen(filepath)
                    # HASHES.append(sha256_hash)
                    outputFile(sha256_hash)

        print(f"\n= {C} json file(s) created.\nCheck them all in your Current working directory, folder named - Json Files")
        print(f"\n- sha256 added to the copy of a csv file. Check the file in your current working directory.")


# TODO 3 : Calculate sha256 of the each entry
def sha256_gen(filename):
    return hashlib.sha256(open(filename, 'rb').read()).hexdigest()


# TODO 4 : Append it to csv file including new row named sha256

def outputFile(hash):
    output = f"{FNAME[0]}.output.csv"
    fname = sys.argv[1]
    with open(fname, 'r') as inputfile:
        # with open("file_sh256/NFT Namings.csv", 'r') as inputfile:
        with open(output, 'w') as outputfile:
            writer = csv.writer(outputfile)
            reader = csv.reader(inputfile)

            for row in reader:
                if row[0] == 'Series Number':
                    writer.writerow(row+['sha256'])
                else:
                    if row[0] == '':
                        print(f"\n= {C} json file(s) created.\nCheck them all in your Current working directory, folder named - Json Files")
                        print(f"\n- sha256 added to the copy of a csv file. Check the file in your current working directory.")

                        exit()
                    writer.writerow(row+[hash])


if __name__ == main():
    main()


'''
Resources:

1. https://github.com/Chia-Network/chips/blob/main/CHIPs/chip-0007.md
2. https://github.com/Chia-Network/chips/blob/main/assets/chip-0007/example.json


'''
