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
- .dockerignore
- .gitignore
- Dockerfile
- main.py
- ReadMe.md
- ReadMe.pdf

## Install
```
pip install requirements.txt
```

## Run
**`Help:`** python main.py --help

### 1- Run on Local System
```
python main.py --table NameTable --file Name.csv
or
python main.py -t NameTable -f Name.csv
```

### 2- Run on with Docker System
- **Step 1:** Docker Image Build
```
docker build -t file_to_postgresql .
```

- **Step 1 Control:**
```
docker image ls
or 
docker images
```

- **Step 2:** Create and Run Container from Docker Image
```
docker run -d -p 8000:8000 file_to_postgresql
or
docker run --name file_to_postgresql_c -d -p 8000:8000 file_to_postgresql
```

- **Step 2.1 Control:** 
```
docker ps
or 
docker ps -a 
```

- **Step 2.2 Control:** 
```
docker logs <CONTAINER ID OR CONTAINER NAME>
```

- **Step 2.3 Control:** 
```
docker container ls -a
docker rm <CONTAINER ID OR CONTAINER NAME>
docker rmi face_detection_api
```

## ToDo
- [ ] Adult Detection
- [ ] Logging

## Contact
- Metin Uslu | uslumetin@gmail.com
- 