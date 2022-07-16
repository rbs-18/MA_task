# MA_task

## Description

Parser for "Detskii mir" shop. Parsing data from category "Lego" from Moscow and St. Petersburg.
Data creating in src/result/ folder to product.csv file. Data demonstrates in 'id', 'title', 'price, RUB',
'city', promo_price, RUB, 'link'.

## Technologies

- Python 3.7

## Running a project in dev mode

- Clone project
```sh
git clone git@github.com:rbs-18/MA_task.git
````

- Install and activate the virtual environment
```sh
python -m venv venv
source venv/bin/activate
````

- Install dependencies from file requirements.txt

```sh
pip install -r requirements.txt
```

- Run parser:

```sh
cd src/script/
python parser.py
```

## Authors

_Aleksei Kozhevnikov_
