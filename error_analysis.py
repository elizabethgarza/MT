#!/c/Users/garza/miniconda3/envs/torch/python


import pandas as pd


def error_analysis(infile, outfile):

    with open(infile, 'r', encoding='utf-16 LE') as source, open(outfile, 'w', encoding='utf-8') as sink: 

        S = []
        T = []
        H = []
        Error_types = []
        
        for line in source:
            line = line.split('\t')
            if 'INFO' in line[0]:
                continue
            else: 
                if 'S' in line[0]: 
                    S.append(line[1].rstrip())
                if 'T' in line[0]: 
                    T.append(line[1].rstrip())
                if 'H' in line[0]: 
                    H.append(line[2].rstrip())
                else: 
                    continue

        data = {'Source':S, 'Target':T, 'Hypothesis':H}
        df = pd.DataFrame(data)
        
        ALL_ERRORS = 0
        TOTAL = 0
    
        IRREGULAR_ERRORS = 0
        TOTAL_IRREGULARS = 0
        OVER_REG = 0
        OVER_IRREG = 0
        DIACRITICS = 0
        irregular_errors = []
        
        for _, row in df.iterrows(): 
            
            TOTAL += 1
            target = row[1]
            hypothesis = row[2] 
            
            source_stem = row[0][0:-4]
            target_stem = row[1][0:-2]
            hypothesis_stem = row[2][0:-2]
            
            if target != hypothesis: 
                ALL_ERRORS += 1
                if source_stem != target_stem:
                    if len(target_stem)!=len(hypothesis_stem):
                        IRREGULAR_ERRORS += 1
                        OVER_REG +=1
                        Error_types.append('OVER-REGULARIZING')
                    else: 
                        DIACRITICS += 1
                        Error_types.append('DIACRITIC/SPELLING')
                else:
                    if len(target_stem)!=len(hypothesis_stem):
                        IRREGULAR_ERRORS += 1
                        OVER_IRREG += 1
                        Error_types.append('OVER-IRREGULARIZING')
                    else: 
                        Error_types.append('DIACRITIC/SPELLING')
                        DIACRITICS += 1
                    continue
                
            if source_stem != target_stem:
                TOTAL_IRREGULARS += 1
                if target_stem == hypothesis_stem: 
                    Error_types.append('')
            else: 
                Error_types.append('')
                
        df['Error types'] = Error_types
            
          
                    
   
        print(f'''
    TOTAL NO. OF ENTRIES: {TOTAL}
    TOTAL ERRORS: {ALL_ERRORS}
    WORD ERROR RATE: {ALL_ERRORS/TOTAL}
    
    TOTAL NO. OF ERRORS DUE TO IRREGULAR MORPHOLOGY: {IRREGULAR_ERRORS}
    PERCENTAGE OF ERRORS DUE TO IRREGULAR MORPHOLOGY: {IRREGULAR_ERRORS/ALL_ERRORS}
    
    TOTAL NO. OF VERBS WITH IRREGULAR MORPHOLOGY: {TOTAL_IRREGULARS}
    PERCENTAGE OF ERRORS WITHIN THE IRREGULAR MORPHOLOGY SET:  {IRREGULAR_ERRORS/TOTAL_IRREGULARS}
       
    OVER-REGULARIZATION ERROR RATE: {OVER_REG/ALL_ERRORS}
    OVER-IRREGULARIZATION ERROR RATE:  {OVER_IRREG/ALL_ERRORS}
    DIACRITIC/SPELLING ERROR RATE: {DIACRITICS/ALL_ERRORS}
    
        ''')

        
        df.to_csv(sink, sep='\t')