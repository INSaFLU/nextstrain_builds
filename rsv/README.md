

## nextstrain.org/rsv

This is a customized Nextstrain build for respiratory syncytial virus (RSV). This is based on the public build, visible at nextstrain.org/rsv.

We've modified it to allow more divergence, increasing clock_filter_iqd to 12.


## Input data

Input sequences (sequences.fasta) and metadata (metadata.tsv) need to be added to the data/a (RSV-A) or data/b (RSV-B) folder.

## Run Analysis Pipeline

The workflow produces whole genome trees for RSV-A and RSV-B.

To run the workflow, use ``snakemake -j4 -p auspice/rsv_{a|b}_genome.json --configfile config/configfile.yaml ` 

