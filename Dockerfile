FROM python:3.14

WORKDIR /app

RUN pip install --no-cache-dir hatch

COPY pyproject.toml .

COPY . .

EXPOSE 8000

CMD ["hatch", "run", "migrate", "&&", "hatch", "run", "start"]

#LABEL authors="tarasgudzovskyi"

#ENTRYPOINT ["top", "-b"]