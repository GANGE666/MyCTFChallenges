#!/bin/bash

# in Ubuntu 18.04
gcc -Wno-int-conversion allinone.c -o allinone

# path to IDA
# in Mac
/Applications/IDA\ Pro\ 7.5/ida.app/Contents/MacOS/idat64 -A -c -S"ida_handle_func.py" ./allinone

# in Ubuntu 20.04
gcc -static-pie ./loader.c ./loader_main.c -o main


cp ./main ./output/
cp ./main ./admin_output/

# run in Ubuntu 18.04
# cd ./admin_output/
# ./main
