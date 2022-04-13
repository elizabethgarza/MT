# MT
Workflow: 

1.  Manually remove data-bin and checkpoints. 
2.  Preprocess by running the following: 

        $ bash preprocess.sh spa.txt
        
3.  Manually assure that all files don't have empty lines.

4.  Train by running: 

        $ bash train.sh -a <EncoderEmbedDim> -b <DecoderEmbedDim> -c <DecoderOutEmbedDim> -d <EncoderHiddenSize> -e <DecoderHiddenSize>
        
5.  Generate predictions by running: 

        $ bash generate.sh <predictions_DATE.txt>
        
6.  Run an error analysis by running: 

        $ python error_analysis.py <predictions_DATE.txt> <errors_DATE.txt>
