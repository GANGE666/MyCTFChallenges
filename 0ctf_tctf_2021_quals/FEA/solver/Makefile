unpacker: unpacker.o fastlz.o
	gcc -o unpacker unpacker.o fastlz.o

unpacker.o : unpacker.c fastlz.h
	gcc -c unpacker.c

fastlz.o : fastlz.c fastlz.h
	gcc -c fastlz.c

clean:
	rm -rf unpacker *.o sc.decompressed sc.compressed tmpfile sc __pycache__
