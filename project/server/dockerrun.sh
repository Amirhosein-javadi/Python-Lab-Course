#!/bin/sh


for c in `docker ps -a --no-trunc | grep 'hug' | awk '{print $1}'`; do
  docker kill $c
  docker rm -f $c
done


int_port=8585
ext_port=5050
if [ ! -d "$1" ]
then
	echo "This volume does not exist, buddy."
	exit 1
fi
cd $1
d=`pwd`
cd -

docker run -dit -v $d:/home/hug  -p 127.0.0.1:$ext_port:$int_port pylab
