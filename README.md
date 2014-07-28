Data Sheet Generator
===

Tools to generate information of recording data.

Written in Shell script.

## Fetch and run

    git clone https://github.com/alfmunny/data-sheet-statistics.git

Direct to the folder und generate the data sheet.
Give the master brach path of data

    ./wacom_data.sh path/to/name.data/
    ./tablet_data.sh path/to/name.data/

Two data sheets will be created in current folder: `wacom_data.txt`, `tablet_data`.

Then run `statistics.sh` to generate the statisitics for each writer

./statistics.sh

## Description of data sheet

The script will only collect the segmentations which are fullfill these conditions

1. has a *labels* data, which must be not empty
2. has a *pen* data
3. has a *letters* data

Data sheet example:
```
Wacom 1404723795942 writer_1 kerze
Wacom 1404723873109 writer_1 kerze
Wacom 1404724171516 writer_2 rollschuhe
Wacom 1404724272672 writer_3 rollschuhe
```

There are four columns in each data sheet, which are

1. equipment: Wacom or Tablet
2. timestamp in the name of the recording file
3. writer
4. content

**NOTE**: The tablet data sheet is only from the delay corrected recordings.

## Description of statistics

The statistics file is to be generated in Markdown format.

Quantity of all available data in data sheet will after writers' names recorded.

And amount of each type of file per writer.

**NOTE**: the numbers are not presented as the words' amount, but for the files
which contain the corresponding words.

Statistics example:

```
# Writer_name_1:	7

  |--Eima	2
  |--Eimer	1
  |--Kersa	1
  |--nehmen	1
  |--spinne	1
  |--stefel	1

---
# Writer_name_2:	88

  |--Eima	4
  |--Eimer	5
  |--Rollschuhe	1
  |--Spine	4
  |--Spinne	4
  |--Stefel	4
  ...
  ...
```

## TODO

1. The labels of the tablet recordings are not corresponding words
to the recording content(see tablet_data.txt, labels are some other sentences),
it's now not possible to generate the statistics of the tablet recordings

2. A script to generate statistics according to each word.
