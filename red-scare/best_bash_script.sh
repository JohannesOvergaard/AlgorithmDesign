for file in data/*.txt

do 
    base=${file%.txt}
    echo "../"$base"" >> output.txt 
    python3 run.py < $file >> output.txt 
    echo "" >> output.txt 
    
done
