FROM python:3.11.4-alpine3.18

WORKDIR /app

COPY requirements.txt setup.py ./

COPY staking_deposit ./staking_deposit

RUN apk add --update gcc libc-dev linux-headers zlib-dev

RUN pip3 install cython==0.29.33
RUN pip3 install -r requirements.txt

RUN python3 setup.py install

ARG cli_command

ENTRYPOINT [ "python3", "./staking_deposit/deposit.py" ]

CMD [ $cli_command ]
