python3 shuffle.py $1
TrainLines=$(wc -l $1 | cut -d " " -f 1)
let TrainLines=TrainLines*8
let TrainLines=TrainLines/10 
split -$TrainLines $1 
mv -i "xaa" "spa_train"
mv -i "xab" "spa_rest"

TestLines=$(wc -l "spa_rest" | cut -d " " -f 1)
echo $TestLines
let TestLines=TestLines*5
let TestLines=TestLines/10
echo $TestLines
split -$TestLines "spa_rest"
mv -i "xaa" "spa_dev"
mv -i "xab" "spa_test"




