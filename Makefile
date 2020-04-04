# This is the default target, which will be built when you invoke make
.PHONY: all
all: hello

# This rule tells make how to build hello from hello.cpp
hello: helloWorld.cpp
	g++ helloWorld.cpp -o hello

# This rule tells make to copy hello to the binaries subdirectory, creating it 
# if necessary
.PHONY: install
install:
	mkdir -p $(DESTDIR)
	install -D -m 0755 hello $(DESTDIR)

# This rule tells make to delete hello
.PHONY: clean 
clean:
	rm -f hello
