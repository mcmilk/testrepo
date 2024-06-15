#!/usr/bin/env bash

rm out* *.txt
exit

for i in *.zip; do
  name=`basename $i .zip`
  test -d $name && rm -rf $name
  mkdir -p $name
  cd $name
  unzip ../$i
  cd ..
done
