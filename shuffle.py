#!/c/Users/garza/miniconda3/envs/torch/python


import argparse
import random


parser = argparse.ArgumentParser()
parser.add_argument('infile', help='infile')
args = parser.parse_args()

def ShuffleLines(infile): 
    
    lines=[]
    with open(infile, 'r', encoding='utf-8') as source:
        
        for line in source: 
            lines.append(line.rstrip())
        random.shuffle(lines)
    
    with open(infile, 'w', encoding='utf-8') as sink: 
        
        for line in lines: 
            print(line, file=sink)

        
if __name__ == '__main__':
    ShuffleLines(args.infile)