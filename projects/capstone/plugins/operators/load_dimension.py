from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E'

    @apply_defaults
    def __init__(self,
                 postgres_conn_id="",
                 aws_credentials_id="",
                 target_table="",
                 append_data="",
                 sql_load_statement="",
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        self.postgres_conn_id = postgres_conn_id
        self.aws_credentials_id = aws_credentials_id
        self.target_table = target_table
        self.append_data = append_data
        self.sql_load_statement = sql_load_statement

    def execute(self, context):
        redshift = PostgresHook(postgres_conn_id = self.postgres_conn_id)
        self.log.info(f'Loading dimension table: {self.target_table}')
        
        if self.append_data:
            self.log.info(f'Appending to {self.target_table}')
            redshift.run(self.sql_load_statement)
        else:
            self.log.info(f'Deleting and inserting into {self.target_table}')
            redshift.run(f'DELETE FROM {self.target_table}')
            redshift.run(self.sql_load_statement)

        self.log.info(f'SUCCESS: Complete loading data to {self.target_table}!')