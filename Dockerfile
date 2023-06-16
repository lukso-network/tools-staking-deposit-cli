FROM python:3.9.17-alpine3.18

WORKDIR /app

COPY requirements.txt setup.py ./

COPY staking_deposit ./staking_deposit

RUN apk add --update --no-cache gcc libc-dev linux-headers zlib-dev \
    && pip3 install -r requirements.txt \
    && python3 setup.py install

ARG cli_command

ENTRYPOINT [ "python3", "./staking_deposit/deposit.py" ]

CMD [ $cli_command ]
