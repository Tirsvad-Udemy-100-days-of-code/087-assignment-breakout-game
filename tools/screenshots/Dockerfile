# Container that runs the Turtle game on a virtual display and takes screenshots.
# The game is never run on the host desktop (framework/process/gui-testing.md).
FROM python:3.13-slim@sha256:e48f59cdba69a3cbd9ed2cf0f348d90d45a8d350d98134cf1070bc106ee9ed90

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        tk xvfb imagemagick xauth \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /work
ENV PYTHONUNBUFFERED=1 \
    DISPLAY=:99

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh \
    && useradd --create-home --shell /bin/bash shooter
USER shooter
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
