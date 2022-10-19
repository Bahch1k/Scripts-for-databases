# Scripts for databases

These scripts are for loading data to MySQL database using `faker` library and transfer this data to MongoDB.

## Dependencies

* Python 3.10.6
* All you need for installing another dependencies, is's use some terminal commmands:
    * Create `env` file with a command depending on your OS.
    * Use `pip install -r requirements.txt` command in terminal.

You have installed the dependencies!

#### Now you can run scripts

### `download.py`

* Open `config` file and change variables with your values to connect to the database.
* Replace the number in the `counter` variable with the number of records you need to load into the database.
* Run `download.py` from terminal.

### `transfer.py`

You can run this script after `download.py` or connect to another database and transfer data from there.

* Open `config` file and change variables with your values to connect to the databases.
* If you want, you can set limit of transfered records by changing `select_data` variable by adding `LIMIT`. 
* Run `transfer.py` from terminal.