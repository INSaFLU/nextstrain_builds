# nextstrain.org/flu/avian

This is a customized [Nextstrain](https://nextstrain.org) build for avian influenza viruses.
The original build is available online at [nextstrain.org/flu/avian](https://nextstrain.org/flu/avian).

We've changed it to allow more divergence, to a maximum clock_filter_iqd of 12.

The influenza virus output files have the wildcard set

`{lineage}_{segment}`

that currently use the following values:

* lineage: [`h5n1`]
* segment: [`ha`, `na`, `pb2`,`pb1`,`pa`,`np`,`mp`,`sh`]

To run this customized build, copy sequences_{lineage}_{segment}.fasta and metadata_{lineage}_{segment}.tsv into the data folder and run:

```
snakemake  auspice/flu_avian_{lineage}_{segment}.json --configfile config/configfile.yaml --cores [nbr of threads]
```

In order to have clade information available (only for NA), before running the build, you need to estimate clades (you need to have HA gene sequences):

```
snakemake -s Snakefile_h5n1.clades --cores [nbr of threads] --config label=[location of LABEL binary]
```


[Nextstrain]: https://nextstrain.org
[augur]: https://github.com/nextstrain/augur
[auspice]: https://github.com/nextstrain/auspice
[snakemake cli]: https://snakemake.readthedocs.io/en/stable/executable.html#all-options
[nextstrain-cli]: https://github.com/nextstrain/cli
[nextstrain-cli README]: https://github.com/nextstrain/cli/blob/master/README.md
