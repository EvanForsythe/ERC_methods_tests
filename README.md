# ERC_methods_tests
Tools for testing the performance of ERCnet


General workflow notes:
We will develop a python script to create random sets of proteome files of various sizes (e.g. 6 proteomes, 12 proteomes etc..). The names of these files will be stored in a csv file

Next, file_mover.py will be used to move the files into new directories. We will run file_mover.py several times to create different folders containing different dataset. We will eventually run Orthofinder and ERCnet separately on each of these. 

Example commands used to run the steps:
```
python random_file_generator.py -s /Users/esforsythe/Documents/Work/Bioinformatics/ERC_networks/Analysis/ERC_methods/Cleaned_proteomes_pool/ -n 6 -j test01 -f Atha.fa -o Atri.fa
```

```
python file_mover.py -s /Users/esforsythe/Documents/Work/Bioinformatics/ERC_networks/Analysis/ERC_methods/Cleaned_proteomes_pool/ -l test01.csv -d /Users/esforsythe/Documents/Work/Bioinformatics/ERC_networks/Analysis/ERC_methods/Randomized_datasets/test01/
```