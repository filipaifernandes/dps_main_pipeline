configfile: "config.yaml"
container: "docker://filipafernandes/dps_main:001"

rule all:
    input:
        config["tree"]

# STEP 1 — convert .ali → FASTA
rule ali_to_fasta:
    input:
        config["structural_ali"]
    output:
        config["structural_fasta"]
    shell:
        """
        python scripts/ali_to_fasta.py {input} {output}
        """

# STEP 2 — profile alignment
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

# STEP 3 — tree
rule build_tree:
    input:
        config["final_alignment"]
    output:
        config["tree"]
    shell:
        """
        fasttree -lg {input} > {output}
        """
