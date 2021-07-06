FROM ubuntu:18.04

RUN apt-get update && \ 
	apt-get upgrade -y && \
	apt-get install -y xinetd
RUN apt-get install -y libtinfo5 


CMD ["/usr/sbin/xinetd", "-dontfork"]

