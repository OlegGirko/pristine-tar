build: zgz/zgz
	pod2man -c pristine-tar pristine-tar > pristine-tar.1
	pod2man -c pristine-gz  pristine-gz  > pristine-gz.1
	pod2man -c pristine-bz2 pristine-bz2 > pristine-bz2.1
	pod2man -c zgz zgz.pod > zgz.1

ZGZ_SOURCES = zgz/zgz.c zgz/bits.c zgz/deflate.c zgz/gzip.c zgz/trees.c zgz/util.c
zgz/zgz: $(ZGZ_SOURCES) zgz/gzip.h
	gcc -Wall -O2 -lz -o $@ $(ZGZ_SOURCES)

install:
	install -d $(DESTDIR)/usr/bin
	install -d $(DESTDIR)/usr/share/man/man1
	install pristine-tar pristine-gz pristine-bz2 zgz/zgz $(DESTDIR)/usr/bin
	install -m 0644 *.1 $(DESTDIR)/usr/share/man/man1

clean:
	rm -f zgz/zgz *.1
