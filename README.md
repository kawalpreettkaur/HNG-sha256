# HNG-sha256
Generates sha256 of json files

# Prerequisite : 
1. Python Enviornment
2. CLI

-> TODO 1 : Save this file where your NFT Namings file(CSV file) is present
-> TODO 2 : Open Command Prompt and change your present directory ( where TODO 1 is present)
-> TODO 3 : Before running the script please ensure you follow these guidelines:-
# Make sure to include "csv file only" while running the script.
# CSV file must include Headers in this order : Series Number,Filename,Description,Gender
# Make sure your NFT file name doesn't include any spaces.
# If there is space please replace it with an underscore.
# TODO 4 : Run this -> python main.py NFT_Namings.
# TODO 5 : Viola, CSV file including sha256 has been created!

Algorithm to implement sha256 generator:

TODO 1 : Input CSV file
TODO 2 : Generate a JSON file per entry in team's sheet in CHIP-0007's default format
TODO 3 : Calculate sha256 of the each entry
TODO 4 : Append it to csv file including new row named sha256

Resources:

1. https://github.com/Chia-Network/chips/blob/main/CHIPs/chip-0007.md
2. https://github.com/Chia-Network/chips/blob/main/assets/chip-0007/example.json

It has used below default format of json file:

'''
DEFAULT DATA FORMAT

json_data =
{
    "format": "CHIP-0007",
    "name" : "NFT name",
    "description": "Description of the NFT",
    "attributes": 
    [
        {
            "trait_type": "Gender",
            "value": "Value of the NFT attribute"
        }
    ],
    "collection": 
    {
        "name": "Name of the NFT collection - NFT NAme + Collection",
        "id": "ID of the NFT collection - e43fcfe6-1d5c-4d6e-82da-5de3aa8b3b57"
    }
}


'''
