FROM ubuntu:18.04

RUN apt-get update && \ 
	apt-get upgrade -y && \
	apt-get install -y xinetd
RUN apt-get install -y gcc python python-pip libtinfo5 libgmp3-dev libmpc-dev 

RUN pip install gmpy2

CMD ["/usr/sbin/xinetd", "-dontfork"]

