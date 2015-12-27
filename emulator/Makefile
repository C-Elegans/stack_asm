sim:main.o cpu.o cpu.h
	clang main.o cpu.o -o sim
	
%.o: %.c
	clang -c $< -o $@
   	
