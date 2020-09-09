for file in data/*-tsp.txt

do 
    echo $file
    base=${file%-tsp.txt}
    python3 solution.py < $file
done