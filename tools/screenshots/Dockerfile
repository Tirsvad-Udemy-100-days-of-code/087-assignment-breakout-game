# Container that runs the Turtle game on a virtual display and takes screenshots.
# The game is never run on the host desktop (framework/process/gui-testing.md).
FROM python:3.13-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        tk xvfb imagemagick xauth \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /work
ENV PYTHONUNBUFFERED=1 \
    DISPLAY=:99

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh \
    && useradd --create-home --shell /bin/bash shooter
USER shooter
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
