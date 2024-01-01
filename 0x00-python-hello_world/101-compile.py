#!/usr/bin/python3
import py_compile
import os
import compileall

filename = os.environ["PYFILEc"]
compileall.compile_file(filename, force=True, legacy=True)
