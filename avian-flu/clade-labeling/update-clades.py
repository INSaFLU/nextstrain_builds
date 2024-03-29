"""This script will pull in the existing clades file and new downloaded fasta, compare the 
strain names, and pull out the sequences which do not yet have a clade label. Those 
sequences are written to a fasta file, which is shuttled into LABEL, and run. Finally, 
those new strains with their corresponding clade annotation are added onto the master 
clades file."""


import pandas as pd
import numpy as np
import csv
from Bio import SeqIO
from subprocess import call 
import os

import argparse
parser = argparse.ArgumentParser()

parser.add_argument('--clades_file', type=str, help='a tab-delimited text file containing H5 HA clade assignments by LABEL')
parser.add_argument('--metadata_file', type=str, help='metadata file output from augur parse')
parser.add_argument('--sequences', type=str, help='path to fasta file from rule download')
parser.add_argument('--subtype', type=str, help='avian flu subtype, either h5nx or h5n1')
parser.add_argument('--label', type=str, help='location of the LABEL binary')

args = parser.parse_args()
metadata_file = args.metadata_file
clades_file = args.clades_file
sequences = args.sequences
subtype = args.subtype
label = args.label

def find_new_strains(clades_file, new_strains):
    old_strains = pd.read_csv(clades_file, sep="\t")['name']
    new_strains = pd.read_csv(new_strains, sep="\t")['strain']
        
    # union of the series -> combination of values present in either set 1 or set 2; so, sum of all elements
    union = pd.Series(np.union1d(new_strains, old_strains))
    
    # intersection of the series -> elements that are shared between the 2
    intersect = pd.Series(np.intersect1d(new_strains, old_strains))
  
    # uncommon elements in both the series; union - all elements of union that are in intersect
    notcommonseries = union[~union.isin(intersect)]
  
    new_strains = notcommonseries.tolist()
    
    return(new_strains)



def separate_new_strains(new_strains_list, input_fasta, output_fasta):
    with open(output_fasta, "w") as outfile: 
        outfile.write("")
    
    for seq in SeqIO.parse(input_fasta, "fasta"):
        #strain = seq.description.split("|")[0]
        strain = seq.description
        full_sequence_header = seq.description
        
        if strain in new_strains_list:             
            with open(output_fasta, "a") as outfile:
                outfile.write(">" + full_sequence_header + "\n" + str(seq.seq) + "\n")



def append_new_clades(new_clades, old_clades):
    with open(new_clades, "r") as infile: 
        for line in infile: 
            if "name\t" not in line:
                strain = line.split("\t")[0]
                clade = line.split("\t")[1]
                
                with open(old_clades, "a") as outfile:
                    outfile.write(strain + "\t" + clade)


"""generate names for new intermediary files"""
new_strains_fasta = "clade-labeling/"+subtype+"-new.fasta"
new_clades_file = "clade-labeling/"+subtype+"-clades-new.tsv"
label_output = subtype+"-new"


"""find new strains and write those new sequences to a fasta file"""
new_strains = find_new_strains(clades_file, metadata_file)
separate_new_strains(new_strains, sequences, new_strains_fasta)


"""run label and reformat the output"""
os.system('{label} -D {new_strains_fasta} {label_output} H5v2015'.format(label=label, new_strains_fasta=new_strains_fasta, label_output=label_output))
#os.system('python clade-labeling/check-LABEL-annotations.py --label_output {label_output}_final.txt --output {new_clades_file}'.format(new_clades_file=new_clades_file, label_output=label_output))
os.system('cat {label_output}_final.txt | grep -v "VIRUS STRAIN" | sed -r \'s/^\s+//\'  | sed -r \'s/\s+/\t/\' > {new_clades_file}'.format(label_output=label_output, new_clades_file=new_clades_file))

"""append the new strains and clades to the master clades file"""
append_new_clades(new_clades_file, clades_file)

"""remove intermediate files"""
os.system('rm {label_output}_final.txt {label_output}.zip {new_strains_fasta} {new_clades_file}'.format(new_strains_fasta=new_strains_fasta, label_output=label_output, new_clades_file=new_clades_file))
