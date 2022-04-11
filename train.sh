#!/c/Users/garza/miniconda3/envs/torch/


while getopts a:b:c:d:e: flag
do 
    case "${flag}" in 
        a) EncoderEmbedDim=${OPTARG};; 
        b) DecoderEmbedDim=${OPTARG};; 
        c) DecoderOutEmbedDim=${OPTARG};; 
        d) EncoderHiddenSize=${OPTARG};;
        e) DecoderHiddenSize=${OPTARG};;
    esac 
done

fairseq-train data-bin --save-dir checkpoints --source-lang spa.i --target-lang spa.o --seed 5228554 --arch lstm --encoder-bidirectional --dropout .2 --encoder-embed-dim $EncoderEmbedDim --decoder-embed-dim $DecoderEmbedDim --decoder-out-embed-dim $DecoderOutEmbedDim  --encoder-hidden-size $EncoderHiddenSize --decoder-hidden-size $DecoderHiddenSize --share-decoder-input-output-embed --criterion label_smoothed_cross_entropy --label-smoothing .1 --optimizer adam --lr .001 --clip-norm 1 --batch-size 128 --max-update 4000 --no-epoch-checkpoints