chmod +x mapper.py reducer.py
cat input.txt | ./mapper.py | sort | ./reducer.py
