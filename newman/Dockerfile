FROM node:20-alpine

RUN apk add --no-cache curl bash

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci

COPY collections/ ./collections/

CMD ["tail", "-f", "/dev/null"]