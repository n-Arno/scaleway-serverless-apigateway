FROM kong:alpine

COPY kong.yml /kong.yml
COPY kong.conf /kong.conf

ENV KONG_NGINX_DAEMON=off

ENTRYPOINT ["/usr/local/bin/kong", "start", "-v", "-c", "/kong.conf"]
