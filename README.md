# dataworld-python

Connect to Data.World with Python and plot a Dashboard

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* [data.world](https://data.world/) - Get an account to obtain the data repository
* [Python](https://www.python.org/downloads/) - An interpreter to run the program

### Installing

First localize your **TOKEN KEY**

```
Go to data.wordl account/settings/Advance and copy your Admin token
```

Install python connector **datadotworld**, type on console

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
pip install datadotworld
```

Add your token key, tpye dw configure and paste your data.world key

```
dw configure
*your key*

```
install libraries required for python program

```
pip install pandas
pip install numpy
pip install matplotlib
```


## Running the program

Now run the script ***ventas por provincia.py***


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

