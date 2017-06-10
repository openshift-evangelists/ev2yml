FROM fedora
WORKDIR /tmp
ADD main.py /tmp
WORKDIR /tmp/data
VOLUME ['/tmp/data']
ENTRYPOINT ["/usr/bin/python3", "/tmp/main.py"]
CMD ['-h']
