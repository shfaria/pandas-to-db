from operator import index
from django.core.management.base import BaseCommand
import pandas as pd
from baseapp.models import Book
from sqlalchemy import create_engine
from django.conf import settings


class Command(BaseCommand):
    help = "custom command?"

    def handle(self, *args, **options):
        
        excel_file = 'books.xlsx'
        df = pd.read_excel(excel_file)
        print(df)

        user = settings.DATABASES['default']['USER']
        password = settings.DATABASES['default']['PASSWORD']
        database_name = settings.DATABASES['default']['NAME']

        database_url = 'postgresql://{user}:{password}@localhost:5432/{database_name}'.format( user=user,password=password,database_name=database_name,)

        engine = create_engine(database_url)

        df.to_sql(Book._meta.db_table, con=engine, if_exists='append', index=False)