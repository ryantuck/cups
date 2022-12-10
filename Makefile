scatter.png : output.jsonl
	cat $< | python plot.py

output.jsonl : run.py
	python run.py | jq -c > $@

.PHONY : loop
loop :
	ls run.py Makefile | entr make
