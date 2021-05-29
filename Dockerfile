FROM python:3-alpine
RUN apk update && apk upgrade && apk add --no-cache bash git
RUN git clone https://github.com/kerszl/sylladic
RUN cd sylladic && pip3 install -r requirements.txt && chmod +x sylladic.py
RUN ln -s /usr/local/bin/python3 /usr/bin/python3
WORKDIR /sylladic
ENTRYPOINT ["/bin/bash", "-c"]
