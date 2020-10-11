#!/bin/bash

echo "Creating new project $1"

if [[ $# -ne 1 ]]; then
	echo "Use: build_project [project_name]"
	exit 2
fi

if [[ ! -d ./$1/ ]]; then
	mkdir -p ./$1/;
fi

printf "name: $1\ninfo: $1\nmode: 7\nsource: $1.bin\noutput: $1.fx" > ./$1/$1.cf
printf "#include <stdio.h>\n#include <stdlib.h>\n#include <sys/bios.h>\n\nvoid main(int argc, char *argv[]) {\n\n\n    return;\n\n}" > ./$1/$1.c
cat >./$1/makefile <<EOL
WWITCH=C:\Development\WWitch

WWITCH_INCLUDES = \$(WWITCH)\include
WWITCH_LIB = \$(WWITCH)\lib
LSIC_LIB = \$(WWITCH)\lsic86ww\lib\s

default:
	lcc86 -I\$(WWITCH_INCLUDES) -L\$(WWITCH_LIB) -L\$(LSIC_LIB) -o ${1}.bin ${1}.c
	mkfent ${1}.cf
EOL