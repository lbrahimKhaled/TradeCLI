# TradeCLI
Transforms raw price data into actionable trading signals using  a composable set of operations: moving averages, rate of change,  cross-above detection, and portfolio simulation.

## Installing dependencies:

```bash
poetry shell
poetry install
```
that should install the dependencies


if the shell command is not installed by default use the following:
```bash
poetry self add poetry-plugin-shell
```

## Rest API
=> the choice of the framework will be FastAPI
=> to test if the rest api is working fine:

### run the server side first :

```bash
uvicorn interfaces.API.server:app --host 0.0.0.0 --port 8000
```

### view command:
then go to postman and put the following next to the get command: 

http://0.0.0.0:8000/view/479f8db9-1b68-4a9f-bd5c-a5c7fef194d9?items=btc&items=eth

or alternatively run the following in terminal:
```bash
curl "http://0.0.0.0:8000/view/479f8db9-1b68-4a9f-bd5c-a5c7fef194d9?items=btc&items=eth"
```

## DB:
=> sqlite was chosen as the db for the saved requests since it is easily maintainable on the user's end 

### to visualize the db do the following:
for mac:
```bash
brew install db-browser-for-sqlite
```
then go the mock-db directory (if you re on the project's directory do the follwing:)
```bash
cd tradecli-db/mock-db
```

then run:
```bash
open tradecli.db 
```
go to the brows data to find the database;
by default in the db there is 4 sample rows with script_id `14601f2a-...`, containing the variables `price`, `entry`, `exit`, and `result` with their corresponding timeseries values.