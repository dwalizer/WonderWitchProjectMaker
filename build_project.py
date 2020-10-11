import sys
import os

if len(sys.argv) != 2:
	print 'Use: build_project.py project_name'
else:
	try:
		os.mkdir(sys.argv[1])
	except OSError:
		print "Failed to create the target directory"
	else:
		cf_file_info = [
			"name: " + sys.argv[1] + "\n", "info: " + sys.argv[1] + "\n", "mode: 7\n"
			"source: " + sys.argv[1] + ".bin\n", "output: " + sys.argv[1] + ".fx"
		]
		cf_filename = sys.argv[1] + "/" + sys.argv[1] + ".cf"
		cf_file = open(cf_filename, "w")
		cf_file.writelines(cf_file_info)
		cf_file.close()

		c_file_info = [
			"#include <stdio.h>\n" "#include <stdlib.h>\n", "#include <sys/bios.h>\n\n",
			"void main(int argc, char *argv[]) {\n\n\n", "    return;\n\n", "}"
		]
		c_filename = sys.argv[1] + "/" + sys.argv[1] + ".c"
		c_file = open(c_filename, "w")
		c_file.writelines(c_file_info)
		c_file.close()

		makefile_contents = [
			"WWITCH=C:\\Development\\WWitch\n\n",
			"WWITCH_INCLUDES = $(WWITCH)\\include\n",
			"WWITCH_LIB = $(WWITCH)\\lib\n",
			"LSIC_LIB = $(WWITCH)\\lsic86ww\\lib\\s\n\n",
			"default:\n",
			"	lcc86 -I$(WWITCH_INCLUDES) -L$(WWITCH_LIB) -L$(LSIC_LIB) -o " + sys.argv[1] + ".bin " + sys.argv[1] + ".c\n",
			"	mkfent " + sys.argv[1] + ".cf"
		]

		makefile = open(sys.argv[1] + "/makefile", "w")
		makefile.writelines(makefile_contents)
		makefile.close()