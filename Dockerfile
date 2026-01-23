FROM ubuntu:latest
LABEL authors="tarasgudzovskyi"

ENTRYPOINT ["top", "-b"]