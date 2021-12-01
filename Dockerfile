FROM node:14-alpine
WORKDIR /usr/src/app/twitter_good
COPY twitter_good/package.json ./
RUN npm install
RUN npm install -g create-react-app
RUN npm i vite @vitejs/plugin-react-refresh
