FROM python:3.10.6-bullseye

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /peachy_peach_bot

COPY ./requirements.txt ./

# Устанавливаем зависимости 
RUN pip install --upgrade pip && pip install --no-cache-dir -r ./requirements.txt

# Копируем файлы и билд
COPY ./ ./

RUN chmod -R 755 ./ ./