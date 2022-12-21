# File To PostgreSQL
`This repository allows you to quickly and easily transfer/write your local files(only *.csv and *.xlsx) to the PostgreSQL server.`
___
## Project Folder
- **`cfg/`**: This directory includes project configuration
    - project.json
- **`data/`**: This directory database contains the files to be transferred.
    - MockPersonData.csv
    - MockPersonData.xlsx
- **`envs/`**: This directory contains the files to be transferred to the database.
- .gitignore
- main.py
- ReadMe.md
- ReadMe.pdf
- requirements.txt

## Install
```
pip install requirements.txt
```

## Run
**`Help:`** 
```
python main.py --help OR python main.py -h
```
**`Parameters:`** 
```
--host			: Database Host 
-d & --database	: Database Name
-t & --table	: Table Name
-s & --schema	: Schema
-u & --userName	: Username
-p & --userPass	: Userpass
-f & --file		: File
-b & --sep		: Seperator
```

### 1- Run

```
python main.py -t MockPersonData -f MockPersonData.csv
or
python main.py --table MockPersonData --file MockPersonData.csv
```

## ToDo
- [ ] Read Binary file formats and export to PostgreSQL
- [ ] Logging

## Contact
- Metin Uslu | uslumetin@gmail.com