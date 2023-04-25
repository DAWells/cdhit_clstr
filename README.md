# CDhit .clstr
After clustering CDhit produces a .clstr file detailing
which sequences went into which clusters. However, it
is not in a machine friendly format. This script converts
it to csv while preserving sequence length, and clustering identity.

Can be called as a command line tool. Takes 2 arguments, the 
cd-hit `.clstr` file and the output path.
`code/analysis/clstr_to_csv.py data/raw/eg.clstr data/processed/eg.csv`