FROM python:3.10-slim

RUN apt update && apt upgrade -y
RUN apt install git -y

WORKDIR /AV_FILE_TO_LINK

COPY requirements.txt .

RUN pip3 install -U pip && pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "bot.py"]
