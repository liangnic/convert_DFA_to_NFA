#! /usr/bin/env bash

# Uncomment exactly one of the following "language=x" lines, according to which
# language you are using.

language=Python
# language=Java
# language=C
# language=C++
# language=Haskell

# If you need to alter the way your project is executed, then you can edit the
# corresponding section below (or even replace this file entirely, if you want.)

case $language in
  Python )
    python3 main.py
    ;;
  Java )
    java Main
    ;;
  C )
    ./main
    ;;
  C++ )
    ./main
    ;;
  Haskell )
    ./main
    ;;
  * )
    echo "(run.sh) Error: language not specified. You need to edit run.sh"
    exit 1
esac
