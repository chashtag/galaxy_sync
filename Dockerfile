FROM python:3.11.0b3

RUN pip3 install requests PyYAML

COPY get_listing.py /

ENTRYPOINT [ "/usr/bin/env", "python3","/get_listing.py" ]