import os
import sys
import json
# open textfile with SRA accession numbers
f=open(sys.argv[1])
# read list of SRA to x
x=f.readlines()
f.close()
# open outfile with csv format
outfile=open("./results/phaster_job_ids.csv","w")
# for every SRA 
for i in x:
    # remove whiteline space
    i=i.strip()
    # retrieve files and split them
    os.system("/home/catherine/Software/sratoolkit.2.11.0-ubuntu64/bin/prefetch "+i)
    os.system("/home/catherine/Software/sratoolkit.2.11.0-ubuntu64/bin/fastq-dump -I --split-files /home/catherine/SRA_TRY_DOWLONAD/sra/"+i+".sra -O "+i)
    # save file1 and file2 as (SRA)_1.fastq or (SRA)_2.fastq
    file1=i+"_1.fastq"
    file2=i+"_2.fastq"
    # use bbduk to trim reads
    os.system("/home/catherine/Software/bbmap/bbduk.sh in=./"+i+"/"+file1+" in2=/home/catherine/Olivia/"+i+"/"+file2 +" out=trimmed_"+file1+" out2=trimmed_"+file2+" threads=16")
    # use SPAdes to assemble genome
    os.system("/home/catherine/SPAdes/SPAdes-3.14.1-Linux/bin/spades.py -1 trimmed_"+file1+" -2 trimmed_"+file2+" -o ./results/"+i+"_assembly --only-assembler -k 55,77,99,127")
    # use wget to upload files to Phaster
    os.system('wget --post-file="./results/'+i+'_assembly/contigs.fasta" "http://phaster.ca/phaster_api?contigs=1" -O '+i+'_phaster')
    # open returned file from Phaster
    f=open(i+'_phaster')
    # read the first line, which is in dictionary format
    y=f.readline()
    f.close()
    # use json to convert the line to a dictionary
    phaster_dict=json.loads(y)
    # write the SRA and job id to the csv outfile
    outfile.write(i+','+phaster_dict['job_id']+'\n')
# close outfile after loop is completed
outfile.close()
