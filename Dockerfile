FROM google/python

RUN echo "deb http://security.debian.org/debian-security wheezy/updates main" >> /etc/apt/sources.list
RUN apt-get update && apt-get install -y xorg xfonts-75dpi

RUN wget http://download.gna.org/wkhtmltopdf/0.12/0.12.2.1/wkhtmltox-0.12.2.1_linux-wheezy-amd64.deb && \
    dpkg -i wkhtmltox-0.12.2.1_linux-wheezy-amd64.deb >/dev/null 2>&1 || true && apt-get install -f -y

RUN pip install pdfkit==0.5.0

EXPOSE 8000
CMD ["/bin/bash"]
