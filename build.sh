#! /usr/bin/env bash

# Uncomment exactly one of the following "language=x" lines, according to which
# language you are using.

language=Python
# language=Java
# language=C
# language=C++
# language=Haskell

# If you need to alter the way your project is compiled (e.g. to add a compiler
# flag, or use a different filename), then you can edit the corresponding
# section below (or even replace this file entirely, if you want.)

case $language in
  Python )
    #for Python, there's nothing to compile, leave this blank
    ;;
  Java )
    javac *.java
    ;;
  C )
    clang main.c -o main
    ;;
  C++ )
    clang++ main.cpp -o main
    ;;
  Haskell )
    ghc main.hs
    ;;
  * )
    echo "(build.sh) Error: language not specified. You need to edit build.sh"
    exit 1
esac
