from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E'
    insert_sql="""
                INSERT INTO {} {}
               """
    
    @apply_defaults
    def __init__(self,
                 postgres_conn_id="",
                 sql_statement="",
                 table="",
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        self.postgres_conn_id=postgres_conn_id
        self.table = table
        self.sql_statement=sql_statement


    def execute(self, context):
        redshift = PostgresHook(self.postgres_conn_id)
        redshift.run(LoadDimensionOperator.insert_sql.format(self.table, self.sql_statement))
