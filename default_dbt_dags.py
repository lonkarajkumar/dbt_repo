from airflow import DAG
from airflow_dbt_python.operators.dbt import DbtBaseOperator, DbtRunOperator
from atlas.dbt_tasks import TARGET_CONN_ID
from atlas.dbt_utils.dbt_dag_factory import create_dags
 
def _add_dags_to_global (dags: list [DAG]) :
    for dag in dags:
        globals () [dag.dag_id] = dag
 
def deploy_dags (
        target_conn _id: str, dbt_folder_name: str | None = None,
        dbt_operator : DbtBaseOperator = DbtRunOperator) :
 
dags = create_dags (target_conn_id, dbt_folder_name, dbt_operator)
_add_dags_to_global (dags)
 
deploy_dags(snowflake_test)