# data_engineeri_itv-ghactivity
Read data from files

Let us develop the code to read the data from files into Spark Dataframes.

Create directory for data and copy some files into it.
Create a Python program by name read.py. We will create a function by name from_files. It reads the data from files into Dataframe and returns it.
Call the program from app.py. For now review schema and data.
Process data using Spark APIs

We will eventually partition the data by year, month and day of month while writing to target directory. However, to partition the data we need to add new columns.

Create a Python program by name process.py. We will create a function by name df_transform. It partitions the Dataframe using specified field.
Call the program from app.py. For now review schema and data.
Productionize Code

Let us make necessary changes to the code so that we can run on a multinode cluster.
Update util.py to use multi node cluster.
Here are the commands to download the files.
