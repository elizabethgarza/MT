#!/c/Users/garza/miniconda3/envs/torch/python

import argparse
import csv


parser = argparse.ArgumentParser()
parser.add_argument('infile', help='infile')
parser.add_argument('outfileI', help='outfileI')
parser.add_argument('outfileO', help='outfileO')
args = parser.parse_args()

def split(infile, outfileI, outfileO): 
    with open(infile, 'r', encoding='utf-8') as source, open(outfileI, 'w', encoding='utf-8') as sinkI, open(outfileO, 'w', encoding='utf-8') as sinkO: 
        for line in source:      
            toks = line.split('\t')
            I = toks[0]
            O = toks[1].rstrip()
            print(" ".join(I), file=sinkI)
            print(" ".join(O), file=sinkO)
    
if __name__ == '__main__':
    split(args.infile, args.outfileI, args.outfileO)
   

    
