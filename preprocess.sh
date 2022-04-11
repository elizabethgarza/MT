#!/c/Users/garza/miniconda3/envs/torch/python

bash split.sh $1
python3 PrePreprocess.py spa_train train.spa.i train.spa.o
python3 PrePreprocess.py spa_dev dev.spa.i dev.spa.o 
python3 PrePreprocess.py spa_test test.spa.i test.spa.o
fairseq-preprocess --source-lang spa.i --target-lang spa.o --trainpref train --validpref dev --testpref test --tokenizer space --thresholdsrc 2 --thresholdtgt 2 