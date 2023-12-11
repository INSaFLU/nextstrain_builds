

#### Analysis
Our bioinformatic processing workflow can be found at [github.com/nextstrain/rsv](https://github.com/nextstrain/rsv) and includes:

- sequence alignment by a combination of [nextalign](https://docs.nextstrain.org/projects/nextclade/en/stable/user/nextalign-cli.html) and [MAFFT](https://mafft.cbrc.jp/alignment/software/).
- phylogenetic reconstruction using [IQTREE](http://www.iqtree.org/)
- ancestral state reconstruction and temporal inference using [TreeTime](https://github.com/neherlab/treetime)
- clade / lineage assignment defined [here](https://github.com/rsv-lineages):
    [RSV-A](https://github.com/rsv-lineages/lineage-designation-A/),
    [RSV-B](https://github.com/rsv-lineages/lineage-designation-B/)

<p>We increased clock_filter_iqd to 12.</p>

<p>References used: </p>
<p>RSV A: A/England/397/2017 (GISAID ID EPI_ISL_412866)</p>
<p>RSV B: B/Australia/VIC-RCH056/2019 (GISAID ID EPI_ISL_1653999)</p>

