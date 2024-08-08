# Running lefse (On Linux systems)
Will use 3 environments due to the the dependancy issuses with the outdated lefse libraries and tools:
1) qimme2 environment(`qiime2-amplicon-2024.2`) for running 'dokdo prepare-lefse'.
2) lefse envoronment( `lefse`) for running lefse.
3) 3rd environment (`lefse_plots`) which uses python scripts to plot the lefse plots.

# 1. Run  this in a qiime2 environment `qiime2-amplicon-2024.2`
The inputs needed are:
1) `table-no-ecmu.qza`
2) taxonomy file - `taxonomy.qza`
3) metadata - `JvSFN_diet-Metadata.tsv`

confirm dokdo installation:
```
dokdo -h
```

```
dokdo prepare-lefse \
    -t ./table-no-ecmu.qza \
    -x ./taxonomy.qza \
    -m ./JvSFN_diet-Metadata.tsv \
    -c TreatmentGroup \
    -o ./input_table.tsv \
```
This returns a file 
Create a TSV file which can be used as input for the LEfSe tool. This command: 
1) Collapses the input feature table at the genus level.
2) Computes relative frequency of the features.
3) Performs sample filtration if requested.
4) Changes the format of feature names.
5) Adds the relevant metadata as 'Class','Subclass', and 'Subject'.
6) Writes a text file `input_table.tsv` which can be used as input for LEfSe.

# 2. Run lefse in a Lefse environment `lefse`

`create` lefse environment with compatible python version, `activate` this lefse environment and `install lefse` in this environment as follows:
```
conda create -n lefse -c conda-forge python=2.7.15
conda activate lefse
conda install -c bioconda -c conda-forge lefse
```

confirm lefse installation:
```
lefse-format_input.py -h
```

Format the input table (run below in the LEfSe terminal):
```
lefse-format_input.py \
./input_table.tsv \
./formatted_table.in \
-c 1 \
-u 2 \
-o 1000000 \
--output_table ./formatted_table.tsv
```

run  lefse:
```
run_lefse.py \
./formatted_table.in \
./output.res
```
# 3. Plot histogram with lefse's output in 3rd env `lefse_plots`
The input file here is `output.res`

Going to use a custom script ( a modified script from the lefse package which was presenting some errors when run in the lefse environment that is created above.

Create and activate 3rd python 3 environment to plot this :
```
conda create -n lefse_plots
conda activate lefse_plots
```

run script `lefse_standalone_script.py` to plot the histogram:
```
python3 ./lefse_standalone_script.py output.res out_his.png
```
