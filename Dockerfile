FROM python:3.11.3-alpine

WORKDIR /app

COPY requirements.txt setup.py ./

COPY staking_deposit ./staking_deposit

RUN apk add --update gcc libc-dev linux-headers zlib-dev build-base openssl-dev libffi-dev

RUN pip3 install -U pip
RUN pip3 install --user -U cython==0.29.33
RUN pip3 install --user -U cytoolz==0.12.2
RUN pip3 install --user -U pycryptodome==3.14.1
RUN pip3 install --user -r requirements.txt

RUN python3 setup.py install

ARG cli_command

ENTRYPOINT [ "python3", "./staking_deposit/deposit.py" ]

CMD [ $cli_command ]
