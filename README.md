# ERC_methods_tests
Tools for testing the performance of ERCnet


General workflow notes:
We will develop a python script create random sets of proteome files of various sizes (e.g. 6 proteomes, 12 proteomes etc..). The names of these files will be stored in a csv file

Next, file_mover.py will be used to move the files into new directories. We will run file_mover.py several times to create different folders containing different dataset. We will eventually run Orthofinder and ERCnet separately on each of these. 

