FROM node:lts-alpine
WORKDIR /
COPY . .
# npx is apparently not good in production (didnt search why) but meh its simpler
# dont need to install any modules it does it for us (i think)
# RUN npm install -g http-server && npm install

# NOTE: to change the port/host, i think we need to change the exposed port
EXPOSE 8080
# CMD ["npx", http-server"]
# NOTE: and gibe some arguments to the npx command, i think these:
CMD ["npx", "http-server", "--port=3000", "--hostname=0.0.0.0"]
