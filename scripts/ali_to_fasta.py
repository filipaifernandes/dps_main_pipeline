import sys

inp = sys.argv[1]
out = sys.argv[2]

seqs = {}
order = []

current = None

with open(inp) as f:
    for line in f:
        line = line.strip()

        if line.startswith(">P1;"):
            current = line.split(";")[1]
            seqs[current] = ""
            order.append(current)

        elif line.startswith("sequence"):
            continue

        elif line == "" or line == "*":
            continue

        else:
            seqs[current] += line.replace("*", "")

with open(out, "w") as o:
    for k in order:
        o.write(f">{k}\n{seqs[k]}\n")
