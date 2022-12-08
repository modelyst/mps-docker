FROM neo4j:4.4.15

ADD ./scripts/loader-entrypoint.sh /
RUN ["chmod", "+x", "/loader-entrypoint.sh"]

ENTRYPOINT [ "/loader-entrypoint.sh" ]