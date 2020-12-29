FROM node:10
WORKDIR /usr/src/app
# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY ./frontend/weather/package*.json ./
COPY ./frontend/weather/ .

RUN npm install
# If you are building your code for production
# RUN npm ci --only=production
# Bundle app source
EXPOSE 80
EXPOSE 443
EXPOSE 3000

CMD ["npm", "start"]