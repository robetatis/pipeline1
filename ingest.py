import logging.config
import psycopg2
import pandas.io.sql as pdsql
from resources.credentials.connection_data import connection_dict
import configparser

class Ingestion:

    logging.config.fileConfig('resources/configs/logging.conf')
    logger = logging.getLogger('ingest')

    def __init__(self, spark):
        self.spark = spark
        self.input_table = self.parse_input_configuration()

    def parse_input_configuration(self):
        config = configparser.ConfigParser()
        config.read('resources/configs/pipeline.ini')
        return config.get('DB_CONFIGS', 'INPUT_TABLE')

    def run(self):
        self.logger.info('ingesting')
        df = self.spark.sql(f'SELECT * FROM {self.input_table}')
        # df = self.spark.read.csv('retailstore.csv', header=True, inferSchema=True)
        return df

    def read_from_postgresql(self):
        connection = psycopg2.connect(
            user=connection_dict['user'],
            password=connection_dict['password'],
            host=connection_dict['host'],
            database=connection_dict['database']
        )
        sql_query = f'SELECT * FROM {self.input_table}'
        df_pandas = pdsql.read_sql_query(sql_query, connection) # read as pandas dataframe...
        df = self.spark.createDataFrame(df_pandas) # ...and then transform to spark dataframe

        return df

    def read_from_postgresql_jdbc(self):
        return self.spark.read.format('jdbc') \
            .option('url', 'jdbc:postgresql://localhost:5432/postgres') \
            .option('dbtable', self.input_table) \
            .option('user', f"{connection_dict['user']}") \
            .option('password', f"{connection_dict['password']}") \
            .load()
