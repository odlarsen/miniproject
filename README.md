# miniproject

This script is designed to pull SRA data from NCBI, trim reads and assemble genomes, submit the assemblies to PHASTER, and record job ids from PHASTER.

In order to run this code, a text file with a list of SRA accession numbers each on their own line must be created.  The textfile and this script should be in the same location.

SPAdes, bbmap, sratoolkit, and wget must be installed on a machine for it to be able to run this code.

Input python3 sra_script.py textfile into the command line.   (Ex: python3 sra_script.py sra_numbers.txt)
