FROM fedora
WORKDIR /tmp
ADD main.py /tmp
WORKDIR /tmp/data
VOLUME ['/tmp/data']
ENTRYPOINT ['/tmp/main.py']


