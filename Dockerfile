FROM python
WORKDIR /app
COPY . /app
CMD ["python3", "File_Organizer.py"]