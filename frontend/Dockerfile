FROM node:latest

WORKDIR /code

COPY package*.json ./

RUN npm install

COPY . /code/frontend

EXPOSE 8080
CMD ["gulp", "start"]