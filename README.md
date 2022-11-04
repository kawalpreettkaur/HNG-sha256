# HNG-sha256 
## Generates sha256 of json files

## Getting started

## Prerequisite : 
1. Python Enviornment
2. CLI

  
## Sample Code Executions

### Sample 1

![image](https://raw.githubusercontent.com/kawalpreettkaur/HNG-sha256/main/Sample%20CLI%20Executions/sample_run1.PNG)

### Sample 2

![image](https://raw.githubusercontent.com/kawalpreettkaur/HNG-sha256/main/Sample%20CLI%20Executions/sample_run2.PNG)

  - - -  
## Common Sample Errors while runnning a Script

### Sample Error 1 : Incorrect Row size in a csv file

![image](https://raw.githubusercontent.com/kawalpreettkaur/HNG-sha256/main/Sample%20Errors/IncorrectRowSize.PNG)

### Sample Error 2: No CSV file added

![image](https://raw.githubusercontent.com/kawalpreettkaur/HNG-sha256/main/Sample%20Errors/No_csvfile.PNG)

### Sample Error 3: Incorrect File Header is used in a csv file

![image](https://raw.githubusercontent.com/kawalpreettkaur/HNG-sha256/main/Sample%20Errors/incorrectFileHeader.PNG)


### Sample Error 4: Wrong Filename is given

![image](https://raw.githubusercontent.com/kawalpreettkaur/HNG-sha256/main/Sample%20Errors/wrongFilename.PNG)


# How to use this script to avoid common errors?

1. Save main.py file where your NFT Namings file(CSV file) is present
2. Open Command Prompt and change your present directory ( where TODO 1 is present)
3. Before running the script please ensure you follow these guidelines:-
- - -
           * Make sure including "csv file only" while running the script.
           * CSV file must include Headers in this order : Series Number,Filename,Description,Gender
           * Make sure your NFT file name doesn't include any spaces. If there is space, please replace it with an underscore. 
                Example: NFT Namings.csv is incorrect.
                Rename and replace the space with an underscore. Now, it becomes NFT_NAMINGS.csv
  - - -              

4. Run below command in command prompt
```sh 
python main.py NFT_Namings.csv
```
6. Viola, CSV file including sha256 has been created!


### Algorithm :

1.   Gets CSV file file from a user
2.   Generates JSON file per entry in team's sheet in CHIP-0007's default format

#### Below mentioned default CHIP-0007 format of json file has been used:
```sh
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
```

3.  Calculates sha256 hash of the each entry
4.  Appends it to the csv file underneath new header named sha256



### References:

### 1. https://github.com/Chia-Network/chips/blob/main/CHIPs/chip-0007.md
### 2. https://github.com/Chia-Network/chips/blob/main/assets/chip-0007/example.json
