configfile: "config.yaml"
container: "docker://filipafernandes/dps_main:002"

rule all:
    input:
        config["structural_fasta"],
        config["final_alignment"],
        config["tree"],
        "data/heatmap/sequence_identity.csv",
        "data/heatmap/sequence_identity.png"

#Profile alignment
rule profile_alignment:
    input:
        aa=config["aa_alignment"],
        struct=config["structural_fasta"]
    output:
        config["final_alignment"]
    shell:
        """
        clustalo --p1 {input.aa} --p2 {input.struct} -o {output} --force
        """

#Tree
rule build_tree:
    input:
        config["final_alignment"]
    output:
        config["tree"]
    shell:
        """
        fasttree -lg {input} > {output}
        """

rule sequence_heatmap:
    input:
        "data/alignment/final_alignment.fasta"
    output:
        "data/heatmap/sequence_identity.csv",
        "data/heatmap/sequence_identity.png"
    shell:
        """
        python scripts/sequence_heatmap.py \
        {input} \
        {output[0]} \
        {output[1]}
        """
