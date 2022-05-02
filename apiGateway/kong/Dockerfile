FROM kong:alpine

USER root

COPY kong.yml /kong.yml
COPY kong.conf /kong.conf
COPY helper.py /helper.py
COPY start.sh /start.sh

RUN chmod a+w /kong.yml \
 && chmod +x /helper.py \
 && chmod +x /start.sh \
 && apk add --no-cache \
      tini \
      python3 \
      py3-pip \
 && pip install \
      requests \
      pyyaml \
 && rm -rf \
      /var/cache/* \
      /root/.cache/* \
      /docker-entrypoint.sh

ENV KONG_NGINX_DAEMON=off
ENV FUNCTION_NAMESPACE=myService

ENTRYPOINT ["/start.sh"]
