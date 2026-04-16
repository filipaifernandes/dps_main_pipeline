FROM snakemake/snakemake:latest

RUN conda install -y -c bioconda -c conda-forge \
    snakemake \
    clustalo \
    fasttree \
    biopython \
    pandas \
    numpy \
    matplotlib \
    seaborn \
    python=3.13 && \
    conda clean -afy

WORKDIR /workflow
