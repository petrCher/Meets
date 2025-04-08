# Meets
Meeting app. Create your form and start looking for people with similar interests

## Building the project

to build the project, clone the repository:

```git
git clone https://github.com/petrCher/Meets.git
```

Then create in folder models file ".env". In file write "DB_DSN=postgresql://USER:PASSWORD@HOST:PORT"

cd into the root folder, and run these commands in your terminal:

```docker
docker compose build
docker compose up
```

then go to http://127.0.0.1:8080 to view the website :)