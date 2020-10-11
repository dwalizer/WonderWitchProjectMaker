# WonderWitchProjectMaker
This is just a quick script I made in both Bash and Python to create new WonderWitch projects for me, as I got tired of making the same files over and over again.  Use is simple:

```bash
build_project.sh {project_name}

python build_project.py {project_name}
```

**project_name** is just whatever you want to call the project - this will be the name of the folder, the initial .c file, the .cf file that's generated and
what's used in the makefile.  It defaults to where I have my WonderWitch libraries installed, so you might have to modify the script to suit your purposes.
