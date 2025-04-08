FROM python
WORKDIR /
COPY . .
RUN pip install -r requirements.txt
# TODO: migrate the database here somehow?
# RUN alembic upgrade head && alembic revision --autogenerate

# TODO: figure out if this needs to be exposed
# because we only need to talk with backend from inside
# but fuck it, if it works im not touching it
EXPOSE 8000

CMD ["python3", "main.py"]
