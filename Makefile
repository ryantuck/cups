# NOTE 8/2023
#	- run.py more thorough physics
#	- simulate.py clearer programming

# NOTE 11/2024
# 	- dialing initial conditions and decay rates yielded expected arc motion, nice

plots : scatter.png scatter-theta.png scatter-phi.png scatter-v.png

scatter.png : output.jsonl
	cat $< | jq -c '{x: .x, y: .y}' | python plot.py $@

scatter-phi.png : output.jsonl
	cat $< | jq -c '{x: .t, y: .phi}' | python plot.py $@

scatter-theta.png : output.jsonl
	cat $< | jq -c '{x: .t, y: .theta}' | python plot.py $@

scatter-v.png : output.jsonl
	cat $< | jq -c '{x: .t, y: .v}' | python plot.py $@

output.jsonl : run.py
	# python simulate.py | jq '.position' -c > $@
	python run.py | jq -c > $@

.PHONY : loop
loop :
	ls run.py Makefile | entr make
