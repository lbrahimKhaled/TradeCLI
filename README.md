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