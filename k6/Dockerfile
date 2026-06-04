FROM grafana/k6:latest

WORKDIR /scripts
COPY load-test.js .
COPY stress-test.js .

ENTRYPOINT ["k6"]