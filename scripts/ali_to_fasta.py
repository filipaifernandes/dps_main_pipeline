import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file) as f:
    lines = f.readlines()
with open(output_file, "w") as out:
    seq = ""
    header = ""
    for line in lines:
        line = line.strip()
        if line.startswith(">P1;"):
            if seq:
                out.write(f">{header}\n{seq}\n")
                seq = ""
            header = line.replace(">P1;", "")

        elif line.startswith("structure") or line == "":
            continue

        elif "*" in line:
            seq += line.replace("*", "")

        else:
            seq += line
            
    if seq:
        out.write(f">{header}\n{seq}\n")
