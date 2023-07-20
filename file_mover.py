#!/usr/bin/env python3

#Storebought modules
import os
import re
import sys
import glob
import time
import math
import shutil
import argparse
import itertools
import subprocess
import numpy as np
import pandas as pd

#At runtime set working directory to the place where the script lives
working_dir = sys.path[0]+'/' 

working_dir="/Users/esforsythe/Documents/Work/Bioinformatics/ERC_networks/Analysis/ERC_methods/ERC_methods_tests"

os.chdir(working_dir)


print(working_dir)


#Set up an argument parser
parser = argparse.ArgumentParser(description='Script for moving files based on a list input')

parser.add_argument('-s', '--source_dir', type=str, metavar='', required=True, help='This should be the full path to the directory where the full pool of proteome files lives. Should end in "/"')
parser.add_argument('-l','--list_file', type=str, metavar='', required=True, help='This should be the name of a csv file containing the name of each file to copy, with each file on a new line. Store file in the same folder where this script lives.')
parser.add_argument('-d','--dest_dir', type=str, metavar='', required=True, help='This should be a full path to the directory where you would like these to land; the scipt will create this folder if needed. Should end in "/"')


#Define the parser
args = parser.parse_args()


#Store arguments
source_dir=args.source_dir
list_file=args.list_file
dest_dir=args.dest_dir


#source_dir="/Users/esforsythe/Documents/Work/Bioinformatics/ERC_networks/Analysis/ERC_methods/ERC_methods_tests/Source/"
#list_file="files2move.csv"
#dest_dir="/Users/esforsythe/Documents/Work/Bioinformatics/ERC_networks/Analysis/ERC_methods/ERC_methods_tests/Destination/"


# Open the file in read mode and read the lines
with open(list_file, "r") as file:
    lines = file.readlines()

# Step 3: Remove any leading or trailing whitespaces and newline characters
lines = [line.strip() for line in lines]


#For loop start
for f in lines:
    if not os.path.isdir(dest_dir):
        os.makedirs(dest_dir)
    else:
        print("Copying file:"+str(f))
        shutil.copy2(source_dir+str(f), dest_dir)
        
        
    
        
shutil.copy2(source_dir+str(f), dest_dir)
