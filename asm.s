jump start
test:
push 1
out
jump end

start: push 2
push 12
gt
cjump test
push 0
out
end: nop
