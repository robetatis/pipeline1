from pyspark.sql import SparkSession
from create_dummy_hive_table import CreateDummyHiveTable
import queries
from ingest import Ingestion
from transform import Transformation
from load import Load
import logging.config

class Pipeline:

    logging.config.fileConfig('resources/configs/logging.conf')
    logger = logging.getLogger('pipeline')

    def __init__(self, jdbc=False):
        if jdbc:
            self.create_spark_session_jdbc()
        else:
            self.create_spark_session()

    def create_spark_session(self):
        self.spark = SparkSession \
            .builder \
            .appName('app') \
            .enableHiveSupport() \
            .getOrCreate()

        self.logger.info("spark session created as 'spark'")

    def create_spark_session_jdbc(self):
        self.spark = SparkSession \
            .builder \
            .appName('app_jdbc') \
            .config('spark.driver.extraClassPath', 'resources/postgresql-42.2.18.jar') \
            .enableHiveSupport() \
            .getOrCreate()

        self.logger.info("spark session created as 'spark'")

    def run(self):
        self.logger.info('starting pipeline')

        # create dummy hive table
        dummy_table_creator = CreateDummyHiveTable()
        dummy_table_creator.run(self.spark, queries.query1)

        # instantiate pipeline stages
        ingestion_stage = Ingestion(self.spark)
        transformation_stage_fillna = Transformation()
        loading_stage = Load(self.spark)

        # read from Hive, write to Hive
        df = ingestion_stage.run()
        df.show()
        df_nafilled = transformation_stage_fillna.run(df)
        loading_stage.writeHiveTable(df_nafilled)

        # read from Hive, write to postresql with psycopg2
        # df = ingestion_stage.run()
        # df_transformed = transformation_stage.run(df)
        # loading_stage.insert_into_postgresql(insert_query=queries.query3, insert_tuple=queries.insert_tuple1)

        # read from postgresql with psycopg2, write to postgresql with psycopg2
        # df = ingestion_stage.read_from_postgresql()
        # df_transformed = transformation_stage.run(df)

        # read from postgresql with jdbc, write to postgresql with jdbc
        # df = ingestion_stage.read_from_postgresql_jdbc()
        # loading_stage.insert_into_postgresql_jdbc(df)

        # read from Hive, write to posgresql with jdbc
        # df = ingestion_stage.run()
        # loading_stage.insert_into_postgresql_jdbc(df)

        self.logger.info('pipeline finished')


if __name__ == '__main__':
    pipeline = Pipeline(jdbc=False)
    pipeline.run()

