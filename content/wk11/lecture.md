# Peak Calling

Conceptually, peak calling consists of the following steps:
 - Align reads to the genome.
 - Count the coverage at each position in the genome.
 - Normalize the coverage across the genome.
 - Compare heights between pull-down and mock treated samples.
 - Filter for regions of high differential.

The Model Based Analysis of ChIP-Seq (MACS) is the reigning champion with more than 16,000 citations. 
In November 2023 Zhang et al released MACS3, which includes new background models and major usability improvements.

As test data we'll use [PRJNA622558](PRJNA622558-yeast-tf-compendium.md), a study by Rossi et al in 2021.
They performed an extensive set fo ChIP-Seq pull-downs in Yeast. 
I've downloaded and pre-aligned some of them.

```bash
/home/jupyter-will/share/OMICS/wk11/
├── aligns
│   ├── chip_CCL1.sorted.bam
│   └── chip_notag_rep1.sorted.bam
└── reads
    ├── chip_CCL1_1.fq.gz
    ├── chip_CCL1_2.fq.gz
    ├── chip_ELF1_1.fq.gz
    ├── chip_ELF1_2.fq.gz
    ├── chip_notag_rep1_1.fq.gz
    ├── chip_notag_rep1_2.fq.gz
    ├── chip_notag_rep2_1.fq.gz
    └── chip_notag_rep2_2.fq.gz
```


## But first, environments

Environments are directories on your computer which contain fully independent copies of programs like `python`, `bwa`, `minimap2`, or Python packages like numpy, matplotlib, etc.
We can then manipulate our `$PATH` variable such that these programs are chosen instead of those installed in the base system.

This is how we can do two important things:
 - Maintain our own software environments to install our own needed packages.
 - Maintain software that has conflicting requirements.

It is the last one that is important here.
My `base` environment is `python3.9` and MACS3 requires `python>=3.11`. 
So, we'll all create our own virtual environment with has a newer python and install MACS3 within that.

## Snake-based pun #7

There are many virtual environment systems.
If you're doing bioinformatics, the only rational answer is `conda`/`mamba`. 
This is completely because of `bioconda` ([I'm slightly biased](https://github.com/orgs/bioconda/people?query=judowill))
Bioconda is a HUGE repository of pre-built bioinformatics related software.
Everything we've used in this class was installed through bioconda.
If you're using conda, you can install _anything_ in bioconda in minutes.
If its not in _bioconda_ ... good luck.


These instructions are loosely based off of this [tutorial](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

`mamba` is the tool we will use to create and manage our environments.
Terminology Note: 
 - `conda` a package managing tool.
 - `miniconda` and `anaconda` are particular environment "build-outs". The former is designed to be tiny, the later is designed to be everything you'd likely need.
 - `mamba` is a drop-in replacement command for `conda` that has faster dependency resolution, multi-threaded download, and is generally better than `conda`.
    If you're creating environments you should use `mamba`.
 
First, which python are we using?

```bash
which python
which macs3
```

That's the `base` one.

Let's create a place to put our environments.

```bash
cd ~/
mkdir envs
```

It is easiest to keep track of your environment if you manage it using a `yaml` definition file.
This lets you specify exactly which tools, which version, and where to get them.
You can easily setup your computational environment on different computer or map across blades.

Create a file in this directory called `macs.yaml`.
Put in:

```yaml
name: macs-tools
channels:
 - bioconda
 - conda-forge
 
dependencies:
 - macs3
```

If you had more tools you needed installed, you could add them here.


```bash
mamba env create -p envs/macs --file envs/macs.yaml 
```

This command searched all of the required sofware and installed it to the `envs/macs` directory.

You can now `activate` that environment with `conda activate envs/macs`.

Try `which python` and `which macs3`.
You should now see them as available.
They'll be available **only in this terminal**.

## Back to peak calling

Now that we have MACS properly installed.
Explore the documentation at https://macs3-project.github.io/MACS/index.html.

Task (45 minutes):
 - Use `macs3` to get the following things for the CLL1 & ELF1 pulldown experiment.
   - When running `macs3`, ensure you are using "paired end" mode and include the notag sample as a control.
   - A `bedGraph` file showing the coverage across the genome.
   - A `bed` file of peaks where TFs bind binds more than expected.
   - Download these for IGV.
 - Are any genes modulated by both CCL1 and ELF1.
   - Use `bedtools` and `saccharomyces_cerevisiae.gff` to find all hits within the 1000 bp upstream of a gene.
   - Intersect the list of genes between the two sets.
   - Export a `bed` file for IGV.
