import csv
import os
import sys
import hashlib
import json
from pathlib import Path

FNAME = []
C = 0
NEW = []
FLAG = 0


def main():
    try:
        fname = sys.argv[1]
    except IndexError:
        print("Wrong command input!")
        exit(1)

    try:
        with open(fname, 'r') as file:
            pass

    except:

        print(f"\nError! {fname} doesn't exist or incorrect file path added.")
        exit(1)

    defaultJson(fname)


# TODO 1 : Input CSV file
# TODO 2 : Generate a JSON file per entry in team's sheet in CHIP-0007's default format

def defaultJson(f):
    global C, FLAG

    with open(f, 'r') as file:
        try:
            os.makedirs("Json_Files", exist_ok=True)
        except OSError as error:
            print("New Directory can not be created. Already exists!")
            exit(0)

        print("\nCreating json files...")
        FNAME.append(Path(f).stem)

        csvreader = csv.reader(file)

        for row in csvreader:
            temp = row

            if FLAG == 0 and row != ['Series Number', 'Filename', 'Description', 'Gender']:
                print("Incorrect File Header!")
                print("Header Usage Guide: ['Series Number','Filename','Description','Gender']")
                print(f"Your header usage: {row}")
                exit(0)

            if len(row) > 4:
                print("Incorrect row size in your csv file.\n Total 4 columns in a row are allowed.")
                print(
                    "Column Usage Guide: Fill each column in a row corresponding to 'Series Number','Filename',"
                    "'Description','Gender'")
                exit(0)

            if row[0] == 'Series Number':
                FLAG = 1
                temp.append("sha256")
                NEW.append(temp)
                continue
            elif row[0].strip() == '':
                print(
                    f"\n= {C} json file(s) created.\nCheck them all in your Current working directory, folder named - "
                    f"Json Files")
                print("\nAdding sha256 of each json file in a new CSV file...")
                print(
                    f"\n- sha256 added to the copy of a csv file.   \nCheck the filenamed {FNAME[0]}.output.csv in "
                    f"your current working directory.")
                outputFile(NEW)
                exit(1)

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

                filepath = f"Json_Files/{new_jsonFile}"
                with open(filepath, 'w') as f:
                    json.dump(json_data, f, indent=2)
                    C += 1
                    sha256_hash = sha256_gen(filepath)
                    temp.append(sha256_hash)

                    NEW.append(temp)


# TODO 3 : Calculate sha256 of the each entry
def sha256_gen(fn):
    return hashlib.sha256(open(fn, 'rb').read()).hexdigest()


# TODO 4 : Append it to csv file including new row named sha256

def outputFile(t_list):
    output = f"{FNAME[0]}.output.csv"

    with open(output, 'a') as outputfile:
        writer = csv.writer(outputfile)
        for lis in NEW:
            writer.writerow(lis)



if __name__ == "__main__":
    main()
