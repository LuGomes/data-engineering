from airflow import DAG
from airflow.operators import PythonOperator
from datetime import datetime
from datetime import timedelta
from operators import (StageToRedshiftOperator, LoadFactOperator,
                                LoadDimensionOperator, DataQualityOperator)
from helpers.sql_queries import SqlQueries


default_args = {
    'owner': 'lugomes',
    'depends_on_past': False,
    'email_on_retry': False,
    'retries': 2,
    'catchup': False,
    'retry_delay': timedelta(minutes=2)
}


dag = DAG('capstone_dag',
          default_args=default_args,
          start_date = datetime.now() - timedelta(days=1),
          description='ETL with AWS Redshift',
          schedule_interval=None
        )

stage_visits_to_redshift = StageToRedshiftOperator(
    task_id='Stage_visits',
    dag=dag,
    postgres_conn_id='redshift',
    aws_credentials_id='aws_credentials',
    table_name='staging_visits',
    s3_bucket='data-eng-capstone-lugomes',
    s3_key='staging_visits',
)

stage_cities_to_redshift = StageToRedshiftOperator(
    task_id='Stage_cities',
    dag=dag,
    postgres_conn_id='redshift',
    aws_credentials_id='aws_credentials',
    table_name='staging_cities',
    s3_bucket='data-eng-capstone-lugomes',
    s3_key='staging_cities',
)

stage_airports_to_redshift = StageToRedshiftOperator(
    task_id='Stage_airports',
    dag=dag,
    postgres_conn_id='redshift',
    aws_credentials_id='aws_credentials',
    table_name='staging_airports',
    s3_bucket='data-eng-capstone-lugomes',
    s3_key='staging_airports',
)

load_visits_dim_table = LoadFactOperator(
    task_id='Load_visits_fact_table',
    dag=dag,
    postgres_conn_id='redshift',
    aws_credentials_id="aws_credentials",
    target_table='visits',
    append_data = True,
    sql_load_statement=SqlQueries.visits_table_insert
)

load_visitors_dim_table = LoadDimensionOperator(
    task_id='Load_visitors_dim_table',
    dag=dag,
    postgres_conn_id='redshift',
    aws_credentials_id="aws_credentials",
    target_table='visitors',
    append_data = False,
    sql_load_statement=SqlQueries.visitors_table_insert
)

load_airports_dim_table = LoadDimensionOperator(
    task_id='Load_airports_dim_table',
    dag=dag,
    postgres_conn_id='redshift',
    aws_credentials_id="aws_credentials",
    target_table='airports',
    append_data = False,
    sql_load_statement=SqlQueries.airports_table_insert
)

load_cities_dim_table = LoadDimensionOperator(
    task_id='Load_cities_dim_table',
    dag=dag,
    postgres_conn_id='redshift',
    aws_credentials_id="aws_credentials",
    target_table='cities',
    append_data = False,
    sql_load_statement=SqlQueries.cities_table_insert
)

run_data_quality_checks = DataQualityOperator(
    task_id='Run_data_quality_checks',
    dag=dag,
    postgres_conn_id="redshift",
    quality_checks=[
        {'quality_check_sql_stmt': "SELECT COUNT(*) FROM visits WHERE visit_id is NULL", 'expected': 0},
        {'quality_check_sql_stmt': "SELECT COUNT(*) FROM cities WHERE city is NULL", 'expected': 0},
        {'quality_check_sql_stmt': "SELECT COUNT(*) FROM visitors WHERE visitor_id is NULL", 'expected': 0}
    ]
)


stage_visits_to_redshift >> load_visits_dim_table
stage_visits_to_redshift >> load_visitors_dim_table
stage_airports_to_redshift >> load_airports_dim_table
stage_cities_to_redshift >> load_cities_dim_table
load_visits_dim_table >> run_data_quality_checks
load_visitors_dim_table >> run_data_quality_checks
load_airports_dim_table >> run_data_quality_checks
load_cities_dim_table >> run_data_quality_checks
