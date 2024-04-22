FROM python

WORKDIR /app

COPY stop_words.py /app/
COPY paragraphs.txt /app/

RUN pip install nltk
RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader stopwords

CMD ["python", "stop_words.py"]



