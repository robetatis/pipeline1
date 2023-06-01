import logging.config

class CreateDummyHiveTable:

    logging.config.fileConfig('resources/configs/logging.conf')
    logger = logging.getLogger('root')

    def execute_sql_query(self, spark, query_string):
        sql_array = query_string.split(';')
        for statement in sql_array:
            if len(statement.strip()) > 0:
                spark.sql(statement)
    
    def run(self, spark, query_string):

        self.logger.info('Creating dummy Hive table...')

        self.execute_sql_query(spark, query_string)
