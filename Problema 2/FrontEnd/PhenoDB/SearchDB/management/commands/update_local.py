from django.core.management.base import BaseCommand, CommandError
from SearchDB.models import PhenoDB
import psycopg2

class Command(BaseCommand):
    help = 'Update the current Django model database'

    def update(self,cur):
        cur.execute("""select * FROM pheno_db""")
        rows = cur.fetchall()
        for row in rows:
            exists = PhenoDB.objects.filter(
                phenoilln__iexact=row[2],
                phenogene__iexact=row[1])
            if not exists:
                p = PhenoDB(
                    phenogene = row[1],
                        phenoilln = row[2])
                p.save()
    
    def connectToPhenosDB(self):
        try:
            conn = psycopg2.connect(
                database="Pheno",
                host="ec2-107-22-175-206.compute-1.amazonaws.com",
                port="5432",
                dbname="dfu5v18hea0jro",
                user="puxsikmrnjnnml",
                password="fpqWwIT73lFClOn23I1MMYpjP3")
            cur = conn.cursor()
            return conn,cur
        except:
            raise CommandError('Could not connect to PhenosDB')
            return None, None

    def handle(self, *args, **options):
        state,cur = self.connectToPhenosDB()
        if state == None:
            return
        self.update(cur) 
        self.stdout.write(self.style.SUCCESS('Successfully updated django db '))


