# python project example
## Nadav Ivzan 
### This repository cotains a dash app and custom python scripts 


## what is in this repository

we developed a dash app to present the iris data set based on different parameters

## how do you run the code locally

the commands below assume you are using a terminal (command line for linux, anaconda prompt for windows see link below) 

### executing it for the first time

using [conda](https://docs.conda.io/en/latest/miniconda.html) create a virtual environment 

```
conda create -n vnv python==3.7 
```

clone this repository in your local computer and change directories into py project

```
git clone https://github.com/kingos82/py-project.git
cd py-project/
```

activate environment 

```
conda activate vnv
```

install dependencies 

```
pip install -r requirements.txt
```

to execute the dash application simply run 

```
python app.py
```

open web browser and enter following address: http://127.0.0.1:8050/

to deactivate an environment simply type 

```
conda deactivate
```

### ongoing execution 

to execute moving forward

```
conda activate vnv 
python app.py
```

open web browser and enter following address: http://127.0.0.1:8050/

## how do you run in hiroku

## personal notes

```
conda activate vnv
pip install sklearn
```
ctrl+shift+P select interpreter choose vnv
pip freeze save all teh environment
to make folders visible outside folder you import in __init__.py: 1.root level __init__ to choose which folders are visible 2. __init__ in each folder which scripts I want to access
