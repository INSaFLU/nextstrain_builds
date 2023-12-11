

#### Analysis
Our bioinformatic processing workflow can be found at [github.com/nextstrain/rsv](https://github.com/nextstrain/rsv) and includes:

- sequence alignment by a combination of [nextalign](https://docs.nextstrain.org/projects/nextclade/en/stable/user/nextalign-cli.html) and [MAFFT](https://mafft.cbrc.jp/alignment/software/).
- phylogenetic reconstruction using [IQTREE](http://www.iqtree.org/)
- ancestral state reconstruction and temporal inference using [TreeTime](https://github.com/neherlab/treetime)
- clade assignment via clade definitions defined here for
    [RSV-A/genome](https://github.com/nextstrain/rsv/blob/master/config/clades_genome_a.tsv),
    [RSV-B/genome](https://github.com/nextstrain/rsv/blob/master/config/clades_genome_b.tsv),
    [RSV-A/G gene](https://github.com/nextstrain/rsv/blob/master/config/clades_G_a.tsv), and
    [RSV-B/G gene](https://github.com/nextstrain/rsv/blob/master/config/clades_G_b.tsv) to label RSV clades based on the entire genome and for just the G gene.
    These clade definitions are based on the proposed nomenclatures by [Goya et al](https://onlinelibrary.wiley.com/doi/abs/10.1111/irv.12715) and [Ramaekers et al](https://doi.org/10.1093/ve/veaa052).

<p>We increased clock_filter_iqd to 12.</p>

<p>References used: </p>
<p>RSV A: GISAID ID EPI_ISL_412866</p>
<p>RSV B: GISAID ID EPI_ISL_1653999</p>

