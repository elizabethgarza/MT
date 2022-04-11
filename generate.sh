#!/c/Users/garza/miniconda3/envs/torch/


fairseq-generate data-bin --source-lang spa.i --target-lang spa.o --path checkpoints/checkpoint_best.pt --gen-subset test --beam 8 > $1