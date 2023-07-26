FROM python:3.11.4-alpine

WORKDIR /app

COPY requirements.txt setup.py ./

COPY staking_deposit ./staking_deposit

RUN apk add --update gcc libc-dev linux-headers zlib-dev build-base openssl-dev libffi-dev
# RUN apt-get update && apt-get install -y libssl-dev libffi-dev build-essential zlib1g-dev

RUN pip3 install -U pip
RUN pip3 install -U cython==0.29.33
RUN pip3 install -U cytoolz==0.12.1
RUN pip3 install -U pycryptodome==3.14.1
RUN pip3 install -r requirements.txt

RUN python3 setup.py install

ARG cli_command

ENTRYPOINT [ "python3", "./staking_deposit/deposit.py" ]

CMD [ $cli_command ]
