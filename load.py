import logging.config
import sys
import psycopg2
from resources.credentials.connection_data import connection_dict
import configparser

class Load:

    logging.config.fileConfig('resources/configs/logging.conf')
    logger = logging.getLogger('load')

    def __init__(self, spark):
        self.spark = spark
        self.output_table = self.parse_output_configuration()

    def parse_output_configuration(self):
        config = configparser.ConfigParser()
        config.read('resources/configs/pipeline.ini')
        return config.get('DB_CONFIGS', 'OUTPUT_TABLE')

    def run(self, df):
        self.logger.info('loading')
        try:
            df.write.option('header', 'True').csv('retailstore_transformed.csv')
        except Exception as e:
            self.logger.error('Loading error: ' + str(e))
            sys.exit(1)
    def writeHiveTable(self, df):
        df.write.mode('overwrite').saveAsTable(self.output_table)

    def insert_into_postgresql(self, insert_query, insert_tuple):
        self.connection = psycopg2.connect(
            user=connection_dict['user'],
            password=connection_dict['password'],
            host=connection_dict['host'],
            database=connection_dict['database'])
        cursor = self.connection.cursor()
        insert_query = insert_query,
        insert_tuple = insert_tuple,
        cursor.execute(insert_query, insert_tuple)
        cursor.close()
        self.connection.commit()

    def insert_into_postgresql_jdbc(self, df):
        df.write \
            .mode('append') \
            .format('jdbc') \
            .option('url', 'jdbc:postgresql://localhost:5432/postgres') \
            .option('dbtable', 'db.tbl2') \
            .option('user', connection_dict['user']) \
            .option('password', connection_dict['password']) \
            .save()
