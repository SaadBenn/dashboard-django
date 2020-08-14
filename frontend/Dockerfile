FROM node
EXPOSE 3000
RUN npm i -g serve
RUN mkdir frontend

COPY . frontend
WORKDIR frontend
RUN npm ci
RUN npm run build