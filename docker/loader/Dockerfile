FROM neo4j:latest

ADD ./scripts/loader-entrypoint.sh /
RUN ["chmod", "+x", "/loader-entrypoint.sh"]

ENTRYPOINT [ "/loader-entrypoint.sh" ]