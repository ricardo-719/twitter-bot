FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN rm -rf _pycache_ .gitignore
CMD [ "python", "twitter_bot.py" ]