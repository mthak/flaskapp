FROM myflask

ADD app.py /root/webapp/app.py
ADD requirements.txt .
RUN pip install -r requirements.txt
CMD ["/usr/bin/supervisord"]
