Processing and visualising the family food dataset

5-a-day-thing

This code takes the family food dataset 
(https://www.gov.uk/government/statistical-data-sets/family-food-datasets)
extracts how much of their 5-a-day different demographics in the UK get
(Spoiler - no one except 70 year olds do) and plots that as a bar chart.
It also makes a series of excel spreadsheets of that, but they are a little
clunky.

It needs the datafiles from the above link converted to excel and saved in
a folder.  This is also all from an Eclipse workspace, so won't work as 
standard Python straight out of the box.

Issues -

This assumes the weekly fruit and veg consumption is spread evenly out over
each day.  The 5-a-day will be effected if people binge on fruit juice on a
single day, say, as only 1 of your 5 a day can come from fruit juice.  

Also, no demographic, on average, consumes more that 1 portion of fruit juice
a day.  I therefore haven't included this as an exception, but if fruit juice
consumption jumps, that if statement will need to go in there somewhere.

for_salt_2

This takes the same dataset and extracts how much of various unhealthy 
foodstuff people eat (processed food, salt, sugar, that sort of thing)
by income.

The primary output for this is an excel workbook for each of income quintile
and decile, with a sheet for each food stuff and a final sheet for total 
expenditure.

This was constructed in colaboration with cookit (cookit.co) in support of a
funding bit.  It was extended in support of a white paper they're writing.

Copyright (C) 2015  Christopher Joseph Davie

MIT License
