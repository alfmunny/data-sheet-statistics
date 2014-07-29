Data Sheet Generator Python
===

Tools to generate a statistic data sheet from recordings.

Written in Python 3.x

## Run

Direct to the `data_sheet_py` folder. Run the `data_sheet_py` with the data path argument

Now it's only for Wacom data

    python data_sheet_py path/to/wacom_data/

A `writer_statistics.md` is to be created.

## Class

### Statistic(string)

A statistic class to include some basic informations for generating corrosponding data sheet, like writers and letters

    s = Statistic('path/to/your/wanting/data')

#### Attributes:

* root

Return a string for the root path of data storing folder

#### Method

* get_writers()

Return a array for all the writers' names

### Writer(string, string)

    w = Writer('writer', 'root')

#### Attributes

* name

Return a string for the name of the given writer

* root

Return a string for the root path of data storing folder

#### Method

* get_letters_files()

Return a array for all the letters json file of the writer 

* get_letters()

Return a dictionary, which contains letters written by the writer 
and the reapt times of each letters

### Printer(object)

    p = Printer(s)

A printer class to help printing out the data sheet to some defined destinations

#### Attributes

* statistic

Return a object of statistic, which defined by Class Statistic.

#### Method

* print_to('filepath')

    p.print_to('statistic.md')

Return a boolean value, which indicate if the file was created

And print the statistics data sheet to the filepath in Markdown format

## TODOs

1. Add the function to create data sheet according to each letter.
2. Add the function to create data sheet according to writer with writer's timestamp
2. Dealing with the Tablet data.


