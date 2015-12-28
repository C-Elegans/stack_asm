test.hex:test
	objcopy -I binary -O ihex test test.hex
	cp test.hex ../main.hex
test:asm.s
	stack_as asm.s test
clean:
	rm test.hex
	rm test
	
