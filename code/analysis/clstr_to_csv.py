#!/usr/bin/env python3

import sys
import re
import pandas as pd

file = sys.argv[1]
output = sys.argv[2]

with open(file, "r") as f:
    lines = f.readlines()

clstr_tab = []
for l in lines:
    if l.startswith(">Cluster"):
        cluster = re.sub("[> \n]", "", l)
    else:
        row = re.split("\s", l)
        row = [x for x in row if not x in ["at",""]]
        row = [cluster] + row
        clstr_tab.append(row)

clstr_tab = pd.DataFrame(clstr_tab,
    columns=['cluster','pos_in_cluster','len','name','identity'])
clstr_tab.len = clstr_tab.len.replace("[a-zA-Z]*,", "", regex=True)
clstr_tab.name = clstr_tab.name.str.replace(">", "")
clstr_tab.identity = clstr_tab.identity.replace("*", "100")
clstr_tab.identity = clstr_tab.identity.str.replace("%", "")

clstr_tab.to_csv(output, index=False)
