from typing import List

import click
import click_config_file

import montecarlodata.settings as settings
from montecarlodata.common import create_mc_client
from montecarlodata.integrations.onboarding.bi.reports import ReportsOnboardingService
from montecarlodata.common.commands import DISAMBIGUATE_DC_OPTIONS
from montecarlodata.common.resources import CloudResourceService
from montecarlodata.integrations.info.status import OnboardingStatusService
from montecarlodata.integrations.onboarding.data_lake.databricks import DatabricksOnboardingService, \
    DEFAULT_SECRET_NAME, DEFAULT_SECRET_SCOPE
from montecarlodata.integrations.onboarding.data_lake.events import EventsOnboardingService
from montecarlodata.integrations.onboarding.data_lake.glue_athena import GlueAthenaOnboardingService
from montecarlodata.integrations.onboarding.data_lake.hive import HiveOnboardingService
from montecarlodata.integrations.onboarding.data_lake.presto import PrestoOnboardingService
from montecarlodata.integrations.onboarding.data_lake.spark import SparkOnboardingService, \
    SPARK_HTTP_MODE_CONFIG_TYPE, SPARK_DATABRICKS_CONFIG_TYPE, SPARK_BINARY_MODE_CONFIG_TYPE
from montecarlodata.integrations.onboarding.etl.dbt_cloud import DbtCloudOnboardingService
from montecarlodata.integrations.onboarding.fields import (
    AIRFLOW_LOGS_CONNECTION_TYPE,
    AIRFLOW_LOGS_EVENT_TYPE,
    CONNECTION_TO_WAREHOUSE_TYPE_MAP,
    GLUE_CONNECTION_TYPE,
    GQL_TO_FRIENDLY_CONNECTION_MAP,
    HIVE_MYSQL_CONNECTION_TYPE,
    HIVE_S3_CONNECTION_TYPE,
    PRESTO_S3_CONNECTION_TYPE,
    DATABRICKS_METASTORE_CONNECTION_TYPE,
    DATABRICKS_DELTA_CONNECTION_TYPE,
    S3_METADATA_EVENT_TYPE,
    S3_QL_EVENT_TYPE,
    SECRETS_MANAGER_CREDENTIAL_MECHANISM,
    SELF_HOSTING_MECHANISMS,
)
from montecarlodata.integrations.onboarding.operations.connection_ops import ConnectionOperationsService
from montecarlodata.integrations.onboarding.self_hosted_credentials import SelfHostedCredentialOnboardingService
from montecarlodata.integrations.onboarding.warehouse.warehouses import WarehouseOnboardingService
from montecarlodata.integrations.keys import IntegrationKeyScope, IntegrationKeyService
from montecarlodata.tools import add_common_options, validate_json_callback, AdvancedOptions, \
    convert_uuid_callback, convert_empty_str_callback

# Shared command verbiage
METADATA_VERBIAGE = 'For metadata'
QL_VERBIAGE = 'For query logs'
SQL_VERBIAGE = 'For health queries'
EVENT_VERBIAGE = 'For tracking data freshness and volume at scale. Requires s3 notifications to be configured first'
REGION_VERBIAGE = 'If not specified the region the collector is deployed in is used'
WAREHOUSE_VERBIAGE = 'For metadata, query logs and metrics'
BI_VERBIAGE = 'For reports'
PASSWORD_VERBIAGE = f'If you prefer a prompt (with hidden input) enter {settings.SHOW_PROMPT_VALUE}'
RESOURCE_VERBIAGE = 'This can be helpful if the resources are in different accounts'
CONNECTION_ID_VERBIAGE = 'ID for the connection.'


# Options shared across commands
def role_options(required: bool = True) -> List:
    return [
        click.option('--role', help='Assumable role ARN to use for accessing AWS resources.', required=required),
        click.option('--external-id', help='An external id, per assumable role conditions.', required=False),
    ]


# Name is used for the creation of a warehouse that will contain the connection.
def warehouse_create_option(required: bool = False, default: str = None) -> List:
    return _warehouse_option(
        help='Friendly name for the created warehouse. Name must be unique.',
        required=required,
        default=default
    )


# Name is used to identify an existing warehouse that will contain the connection.
def warehouse_select_option(required: bool = False, default: str = None) -> List:
    return _warehouse_option(
        help='Friendly name of the warehouse which the connection will belong to.',
        required=required,
        default=default
    )


def _warehouse_option(help: str, required: bool = False, default: str = None) -> List:
    return [click.option(
        '--name',
        help=help,
        required=required,
        default=default
    )]


WAREHOUSE_OPTIONAL_CREATE_OPTIONS = [
    click.option('--create-warehouse', help='Create a new warehouse with this connection', type=click.BOOL, default=True, required=False)
]
S3_OPTIONS = [
    click.option('--bucket', help='S3 Bucket where query logs are contained.', required=True),
    click.option('--prefix', help='Path to query logs.', required=True),
    *role_options(required=False)
]
DATABASE_OPTIONS = [
    click.option('--host', help='Hostname.', required=True),
    click.option('--user', help='Username with access to the database.', required=True),
    click.option('--database', help='Name of database.', required=True),
    click.option('--password', help=f'User\'s password. {PASSWORD_VERBIAGE}.', required=True, cls=AdvancedOptions, prompt_if_requested=True)
]

CONNECTION_OPTIONS = [
    click.option('--connection-id', help=CONNECTION_ID_VERBIAGE, required=True, type=click.UUID, callback=convert_uuid_callback)
]

ONBOARDING_CONFIGURATION_OPTIONS = [
    *DISAMBIGUATE_DC_OPTIONS,
    click.option('--skip-validation', is_flag=True, help='Skip all connection tests.',
                 cls=AdvancedOptions, mutually_exclusive_options=['validate_only']),
    click.option('--validate-only', is_flag=True, help='Run connection tests without adding.',
                 cls=AdvancedOptions, mutually_exclusive_options=['skip_validation']),
    click.option('--auto-yes', is_flag=True, help='Skip any interactive approval.', default=False, show_default=True)
]

NETWORK_OPTIONS = [
    click.option('--test-network-only', 'skip_permission_tests', is_flag=True, default=False, show_default=True,
                 cls=AdvancedOptions, mutually_exclusive_options=['skip_validation'],
                 help='Skip any permission tests. Only validates network connection between the collector and resource can be established.')
]

BI_OPTIONS = [
    click.option('--verify-ssl/--no-verify-ssl', 'verify_ssl', required=False, default=True, show_default=True,
                 help='Whether to verify the SSL connection (uncheck for self-signed certs).')
]

DATABRICKS_OPTIONS = [
    click.option('--databricks-workspace-url', help='Databricks workspace URL.', required=True),
    click.option('--databricks-workspace-id', help='Databricks workspace ID.', required=True),
    click.option('--databricks-cluster-id', help='Databricks cluster ID.', required=True),
    click.option('--databricks-token', help=f'Databricks access token. {PASSWORD_VERBIAGE}.', required=True,
                 cls=AdvancedOptions, prompt_if_requested=True)
]

DATABRICKS_DATA_COLLECTOR_OPTIONS = [
    click.option('--skip-secret-creation', help='Skip secret creation.', default=False, show_default=True, is_flag=True),
    click.option('--databricks-secret-key', help='Databricks secret key.', default=DEFAULT_SECRET_NAME, show_default=True),
    click.option('--databricks-secret-scope', help='Databricks secret scope.', default=DEFAULT_SECRET_SCOPE,
                 show_default=True),
    click.option('--skip-notebook-creation', help='Skip notebook creation.', default=False, show_default=True,
                 is_flag=True, cls=AdvancedOptions,
                 required_with_options=['databricks_job_id', 'databricks_job_name', 'databricks_notebook_path']),
    click.option('--databricks-job-id', help='Databricks job id, required if notebook creation is skipped.',
                 required=False, cls=AdvancedOptions,
                 required_with_options=['skip_notebook_creation']),
    click.option('--databricks-job-name', help='Databricks job name, required if notebook creation is skipped.',
                 required=False, cls=AdvancedOptions,
                 required_with_options=['skip_notebook_creation']),
    click.option('--databricks-notebook-path', help='Databricks notebook path, required if notebook creation is skipped.',
                 required=False, cls=AdvancedOptions,
                 required_with_options=['skip_notebook_creation']),
    click.option('--databricks-notebook-source',
                 help='Databricks notebook source, required if notebook creation is skipped. (e.g. "resources/databricks/notebook/v1/collection.py")',
                 required=False, cls=AdvancedOptions,
                 required_with_options=['skip_notebook_creation']),
]

S3_BUCKET_OPTIONS = [
    click.option('--bucket', 'bucket_name', required=False, help='Name of bucket to enable events for.'),
    click.option('--prefix', default=None, callback=convert_empty_str_callback, required=False,
                  help='Limit the notifications to objects starting with a prefix (e.g. \'data/\').'),
    click.option('--suffix', default=None, callback=convert_empty_str_callback, required=False,
                  help='Limit notifications to objects ending with a suffix (e.g. \'.csv\').'),
    click.option('--topic-arn', default=None, callback=convert_empty_str_callback, required=False,
                  help='Use an existing SNS topic (same region as the bucket). Creates a topic if one is not specified or '
                       'if an MCD topic does not already exist in the region.'),
    click.option('--buckets-filename', required=False, help='Filename that contains bucket config to enable events for',
                 cls=AdvancedOptions, mutually_exclusive_options=['bucket_name'])
]

EVENT_TYPE_OPTIONS = [
    click.option('--event-type', required=True, default=CloudResourceService.MCD_EVENT_TYPE_MD, show_default=True,
                  help='Type of event to setup.',
                  type=click.Choice(CloudResourceService.MCD_EVENT_TYPE_FRIENDLY_TO_COLLECTOR_OUTPUT_MAP.keys(), case_sensitive=True)),
]

RESOURCE_PROFILE_OPTIONS = [
    click.option('--resource-aws-profile', 'bucket_aws_profile', required=False,
                  help=f'Override the AWS profile use by the CLI for operations on S3/SNS. {RESOURCE_VERBIAGE}.')
]

COLLECTOR_PROFILE_OPTIONS = [
    click.option('--collector-aws-profile', required=False,
                  help=f'Override the AWS profile use by the CLI for operations on SQS/Collector. {RESOURCE_VERBIAGE}.')
]

AUTO_YES_OPTIONS = [
    click.option('--auto-yes', is_flag=True, help='Skip any interactive approval.', default=False, show_default=True)
]


@click.group(help='Manage or integrate an asset with Monte Carlo.')
def integrations():
    """
    Group for any integration related subcommands
    """
    pass


@integrations.command(help=f'Setup a Hive metastore integration (MySQL). {METADATA_VERBIAGE}.')
@click.pass_obj
@click.option('--port', help='HTTP port.', default=3306, type=click.INT, show_default=True)
@click.option('--use-ssl', help='Use SSL to connect (using AWS RDS certificates).', required=False, is_flag=True,
              default=False, show_default=True)
@click.option('--catalog', help='Presto catalog name. For using multiple hive clusters with Presto. '
                                'Uses \'hive\' if not specified.', required=False)
@add_common_options(warehouse_create_option())
@add_common_options(WAREHOUSE_OPTIONAL_CREATE_OPTIONS)
@add_common_options(DATABASE_OPTIONS)
@add_common_options(ONBOARDING_CONFIGURATION_OPTIONS)
@click_config_file.configuration_option(settings.OPTION_FILE_FLAG)
def add_hive_metastore(ctx, database, name, **kwargs):
    """
    Onboard a hive metastore connection (MySQL)
    """
    HiveOnboardingService(config=ctx['config']).onboard_hive_mysql(
        dbName=database, warehouseName=name, **kwargs
    )


@integrations.command(help=f'Setup a Presto SQL integration. {SQL_VERBIAGE}.')
@click.pass_obj
@click.option('--host', help='Hostname.', required=True)
@click.option('--port', help='HTTP port.', default=8889, type=click.INT, show_default=True)
@click.option('--user', help='Username with access to catalog/schema.', required=False)
@click.option('--password', help=f'User\'s password. {PASSWORD_VERBIAGE}', required=False, cls=AdvancedOptions, prompt_if_requested=True)
@click.option('--catalog', help='Mount point to access data source.', required=False)
@click.option('--schema', help='Schema to access.', required=False)
@click.option('--http-scheme', help='Scheme for authentication.',
              type=click.Choice(['http', 'https'], case_sensitive=True), required=True)
@click.option('--cert-file', help='Local SSL certificate file to upload to collector.', required=False,
              type=click.Path(dir_okay=False, exists=True), cls=AdvancedOptions, mutually_exclusive_options=['cert_s3'])
@click.option('--cert-s3', help='Object path (key) to a certificate already uploaded to the collector.',
              required=False, cls=AdvancedOptions, mutually_exclusive_options=['cert_file'])
@click.option('--skip-cert-verification', help='Skip SSL certificate verification.', required=False, is_flag=True)
@add_common_options(warehouse_select_option())
@add_common_options(ONBOARDING_CONFIGURATION_OPTIONS)
@click_config_file.configuration_option(settings.OPTION_FILE_FLAG)
def add_presto(ctx, password, name, **kwargs):
    """
    Onboard a presto sql connection
    """
    if not password:
        password = None  # make explicitly null if not set. Prompts can't be None
    PrestoOnboardingService(config=ctx['config']).onboard_presto_sql(
        password=password, warehouseName=name, **kwargs
    )


@integrations.command(help=f'Setup a Hive SQL integration. {SQL_VERBIAGE}.')
@click.pass_obj
@click.option('--host', help='Hostname.', required=True)
@click.option('--database', help='Name of database.', required=False)
@click.option('--port', help='HTTP port.', default=10000, type=click.INT, show_default=True)
@click.option('--user', help='Username with access to hive.', required=True)
@click.option('--auth-mode', help='Hive authentication mode.', required=False, default='SASL',
              type=click.Choice(['SASL', 'NOSASL']), show_default=True)
@add_common_options(warehouse_select_option())
@add_common_options(ONBOARDING_CONFIGURATION_OPTIONS)
@click_config_file.configuration_option(settings.OPTION_FILE_FLAG)
def add_hive(ctx, user, name, **kwargs):
    HiveOnboardingService(config=ctx['config']).onboard_hive_sql(
        username=user, warehouseName=name, **kwargs
    )


@integrations.command(help=f'Setup a Presto logs integration (S3). {QL_VERBIAGE}.')
@click.pass_obj
@add_common_options(S3_OPTIONS)
@add_common_options(ONBOARDING_CONFIGURATION_OPTIONS)
@click_config_file.configuration_option(settings.OPTION_FILE_FLAG)
def add_presto_logs(ctx, role, **kwargs):  # DEPRECATED
    """
    Onboard a presto logs (s3) connection
    """
    PrestoOnboardingService(config=ctx['config']).onboard_presto_s3(assumable_role=role, **kwargs)


@integrations.command(help=f'Setup a Hive EMR logs integration (S3). {QL_VERBIAGE}.')
@click.pass_obj
@add_common_options(S3_OPTIONS)
@add_common_options(ONBOARDING_CONFIGURATION_OPTIONS)
@click_config_file.configuration_option(settings.OPTION_FILE_FLAG)
def add_hive_logs(ctx, role, **kwargs):  # DEPRECATED
    """
    Onboard a hive emr (s3) connection
    """
    HiveOnboardingService(config=ctx['config']).onboard_hive_s3(assumable_role=role, **kwargs)


@integrations.command(help=f'Setup a Glue integration. {METADATA_VERBIAGE}.')
@click.pass_obj
@click.option('--region', help=f'Glue catalog region. {REGION_VERBIAGE}.', required=False)
@add_common_options(role_options())
@add_common_options(warehouse_create_option())
@add_common_options(ONBOARDING_CONFIGURATION_OPTIONS)
@click_config_file.configuration_option(settings.OPTION_FILE_FLAG)
def add_glue(ctx, role, region, name, **kwargs):
    """
    Onboard a glue connection
    """
    GlueAthenaOnboardingService(config=ctx['config']).onboard_glue(
        assumable_role=role, aws_region=region, warehouseName=name, **kwargs
    )


@integrations.command(help='Setup an Athena integration. For query logs and health queries.')
@click.pass_obj
@click.option('--catalog', help='Glue data catalog. If not specified the AwsDataCatalog is used.', required=False)
@click.option('--workgroup',
              help='Workbook for running queries and retrieving logs. If not specified the primary is used.',
              required=False)
@click.option('--region', help=f'Athena cluster region. {REGION_VERBIAGE}.', required=False)
@add_common_options(warehouse_select_option())
@add_common_options(role_options())
@add_common_options(ONBOARDING_CONFIGURATION_OPTIONS)
@click_config_file.configuration_option(settings.OPTION_FILE_FLAG)
def add_athena(ctx, role, region, name, **kwargs):
    """
    Onboard an athena connection
    """
    GlueAthenaOnboardingService(config=ctx['config']).onboard_athena(
        assumable_role=role, aws_region=region, warehouseName=name, **kwargs
    )


@integrations.command(help=f'Setup a thrift binary Spark integration. {SQL_VERBIAGE}.')
@click.pass_obj
@click.option('--host', help='Hostname.', required=True)
@click.option('--database', help='Name of database.', required=True)
@click.option('--port', help='Port.', default=10000, type=click.INT, show_default=True)
@click.option('--user', help='Username with access to spark.', required=True)
@click.option('--password', help=f'User\'s password. {PASSWORD_VERBIAGE}.', required=True,
              cls=AdvancedOptions, prompt_if_requested=True)
@add_common_options(warehouse_select_option())
@add_common_options(ONBOARDING_CONFIGURATION_OPTIONS)
@click_config_file.configuration_option(settings.OPTION_FILE_FLAG)
def add_spark_binary_mode(ctx, user, name, **kwargs):
    """
    Onboard a spark connection, thrift binary mode
    """
    SparkOnboardingService(config=ctx['config']).onboard_spark(
        SPARK_BINARY_MODE_CONFIG_TYPE, username=user, warehouseName=name, **kwargs
    )


@integrations.command(help=f'Setup a thrift HTTP Spark integration. {SQL_VERBIAGE}.')
@click.pass_obj
@click.option('--url', help='HTTP URL.', required=True)
@click.option('--user', help='Username with access to spark.', required=True)
@click.option('--password', help=f'User\'s password. {PASSWORD_VERBIAGE}.', required=True,
              cls=AdvancedOptions, prompt_if_requested=True)
@add_common_options(warehouse_select_option())
@add_common_options(ONBOARDING_CONFIGURATION_OPTIONS)
@click_config_file.configuration_option(settings.OPTION_FILE_FLAG)
def add_spark_http_mode(ctx, user, name, **kwargs):
    """
    Onboard a spark connection, thrift http mode
    """
    SparkOnboardingService(config=ctx['config']).onboard_spark(
        SPARK_HTTP_MODE_CONFIG_TYPE, username=user, warehouseName=name, **kwargs
    )


@integrations.command(help=f'Setup a Spark integration for Databricks. {SQL_VERBIAGE}.')
@click.pass_obj
@add_common_options(DATABRICKS_OPTIONS)
@add_common_options(warehouse_select_option())
@add_common_options(ONBOARDING_CONFIGURATION_OPTIONS)
@click_config_file.configuration_option(settings.OPTION_FILE_FLAG)
def add_spark_databricks(ctx, name, **kwargs):
    """
    Onboard a spark connection, databricks
    """
    SparkOnboardingService(config=ctx['config']).onboard_spark(
        SPARK_DATABRICKS_CONFIG_TYPE, warehouseName=name, **kwargs
    )


@integrations.command(help='Setup a Databricks metastore integration. For metadata and health queries.')
@click.pass_obj
@add_common_options(warehouse_create_option())
@add_common_options(DATABRICKS_OPTIONS)
@add_common_options(DATABRICKS_DATA_COLLECTOR_OPTIONS)
@add_common_options(ONBOARDING_CONFIGURATION_OPTIONS)
@click_config_file.configuration_option(settings.OPTION_FILE_FLAG)
def add_databricks_metastore(ctx, name, **kwargs):
    """
    Onboard a databricks metastore
    """
    DatabricksOnboardingService(
        config=ctx['config'], mc_client=create_mc_client(ctx)
    ).onboard_databricks_metastore(
        connection_type=DATABRICKS_METASTORE_CONNECTION_TYPE, warehouseName=name, **kwargs
    )


@integrations.command(help='Setup a Databricks Delta integration. For metadata queries on delta tables when using an external metastore in databricks.')
@click.pass_obj
@add_common_options(DATABRICKS_OPTIONS)
@add_common_options(warehouse_select_option())
@add_common_options(DATABRICKS_DATA_COLLECTOR_OPTIONS)
@add_common_options(ONBOARDING_CONFIGURATION_OPTIONS)
@click_config_file.configuration_option(settings.OPTION_FILE_FLAG)
def add_databricks_delta(ctx, name, **kwargs):
    """
    Onboard a databricks delta service
    """
    DatabricksOnboardingService(
        config=ctx['config'], mc_client=create_mc_client(ctx)
    ).onboard_databricks_metastore(
        connection_type=DATABRICKS_DELTA_CONNECTION_TYPE, warehouseName=name, **kwargs
    )


@integrations.command(help=f'Setup a Redshift integration. {WAREHOUSE_VERBIAGE}.')
@click.pass_obj
@click.option('--port', help='HTTP port.', default=5439, type=click.INT, show_default=True)
@add_common_options(warehouse_create_option())
@add_common_options(DATABASE_OPTIONS)
@add_common_options(ONBOARDING_CONFIGURATION_OPTIONS)
@add_common_options(NETWORK_OPTIONS)
@click_config_file.configuration_option(settings.OPTION_FILE_FLAG)
def add_redshift(ctx, database, name, **kwargs):
    """
    Onboard a redshift connection
    """
    WarehouseOnboardingService(config=ctx['config']).onboard_redshift(dbName=database, warehouseName=name, **kwargs)


@integrations.command(help=f'Setup a Snowflake integration. {WAREHOUSE_VERBIAGE}.')
@click.pass_obj
@click.option('--user', help='User with access to snowflake.', required=True, cls=AdvancedOptions,
              at_least_one_set=['password', 'private_key'])
@click.option('--account', help='Snowflake account name.', required=True)
@click.option('--warehouse', help='Name of the warehouse for the user.', required=True)
@click.option('--password', help=f'User\'s password if using user/password basic auth. {PASSWORD_VERBIAGE}.',
              required=False, cls=AdvancedOptions, prompt_if_requested=True,
              mutually_exclusive_options=['private_key'])
@click.option('--private-key', help='User\'s private key file path if using key pair auth.',
              type=click.Path(exists=True), required=False, cls=AdvancedOptions,
              mutually_exclusive_options=['password'])
@click.option('--private-key-passphrase', help=f'User\'s private key passphrase if using key pair auth. This argument is only needed when the private key is encrypted. {PASSWORD_VERBIAGE}.',
              required=False, cls=AdvancedOptions, prompt_if_requested=True,
              mutually_exclusive_options=['password'], required_with_options=['private_key'])
@add_common_options(warehouse_create_option())
@add_common_options(ONBOARDING_CONFIGURATION_OPTIONS)
@click_config_file.configuration_option(settings.OPTION_FILE_FLAG)
def add_snowflake(ctx, name, **kwargs):
    """
    Onboard a snowflake connection
    """
    WarehouseOnboardingService(config=ctx['config']).onboard_snowflake(warehouseName=name, **kwargs)


@integrations.command(help=f'Setup a BigQuery integration. {WAREHOUSE_VERBIAGE}.')
@click.pass_obj
@click.option('--key-file', help='JSON Key file.', type=click.Path(exists=True), required=True)
@add_common_options(warehouse_create_option())
@add_common_options(ONBOARDING_CONFIGURATION_OPTIONS)
@click_config_file.configuration_option(settings.OPTION_FILE_FLAG)
def add_bigquery(ctx, key_file, name, **kwargs):
    """
    Onboard a BigQuery connection
    """
    WarehouseOnboardingService(config=ctx['config']).onboard_bq(ServiceFile=key_file, warehouseName=name, **kwargs)


@integrations.command(help='Setup an integration that uses self-hosted credentials.')
@click.pass_obj
@click.option(
    '--connection-type',
    help='Type of connection.',
    required=True,
    type=click.Choice(GQL_TO_FRIENDLY_CONNECTION_MAP.keys(), case_sensitive=False),
    cls=AdvancedOptions,
    values_with_required_options=CONNECTION_TO_WAREHOUSE_TYPE_MAP.keys(),
    required_options_for_values=['name'],
)
@click.option(
    '--mechanism',
    help='Credential self-hosting mechanism.',
    required=True,
    type=click.Choice(SELF_HOSTING_MECHANISMS, case_sensitive=False),
    default=SECRETS_MANAGER_CREDENTIAL_MECHANISM,
)
@click.option('--key', help='Identifier for credentials within self-hosting mechanism.', required=True)
@click.option('--name', help='Friendly name for the warehouse.', required=False)
@add_common_options(role_options(required=False))
@add_common_options(ONBOARDING_CONFIGURATION_OPTIONS)
@click_config_file.configuration_option(settings.OPTION_FILE_FLAG)
def add_self_hosted_credentials(ctx, mechanism, key, role, name, **kwargs):
    """
    Onboard a connection with self-hosted credentials
    """
    SelfHostedCredentialOnboardingService(config=ctx['config']).onboard_connection(
        self_hosting_mechanism=mechanism,
        self_hosting_key=key,
        assumable_role=role,
        warehouseName=name,
        **kwargs
    )


@integrations.command(help='Configure S3 events for Airflow task logs.')
@click.pass_obj
@add_common_options(warehouse_create_option(default='airflow-logs-s3'))
@add_common_options(DISAMBIGUATE_DC_OPTIONS)
@add_common_options(role_options())
@click_config_file.configuration_option(settings.OPTION_FILE_FLAG)
def configure_airflow_log_events(ctx, **kwargs):
    """
    Configure s3 events for Airflow task logs
    """
    EventsOnboardingService(config=ctx['config']).configure_airflow_events(**kwargs)


@integrations.command(help=f'Configure S3 metadata events. {EVENT_VERBIAGE}.')
@click.pass_obj
@click.option('--connection-type',
              help='Type of the integration.', cls=AdvancedOptions,
              mutually_exclusive_options=['connection_id'],
              type=click.Choice([
                  DATABRICKS_METASTORE_CONNECTION_TYPE,
                  GLUE_CONNECTION_TYPE,
                  HIVE_MYSQL_CONNECTION_TYPE
              ], case_sensitive=False),
              required=True)
@add_common_options(warehouse_create_option(default='s3-metadata-events'))
@add_common_options(DISAMBIGUATE_DC_OPTIONS)
@click_config_file.configuration_option(settings.OPTION_FILE_FLAG)
def configure_metadata_events(ctx, **kwargs):
    """
    Configure S3 metadata events for a lake
    """
    EventsOnboardingService(config=ctx['config']).configure_metadata_events(**kwargs)


@integrations.command(help=f'Configure S3 query log events. {EVENT_VERBIAGE}.')
@click.pass_obj
@click.option('--connection-type',
              help='Type of the integration.',
              type=click.Choice([
                  HIVE_S3_CONNECTION_TYPE,
                  PRESTO_S3_CONNECTION_TYPE
              ], case_sensitive=True),
              required=True)
@add_common_options(warehouse_select_option())
@add_common_options(role_options())
@click.option('--format-type', help='Query log format.',
              type=click.Choice(['hive-emr', 'hive-native', 'custom'], case_sensitive=True),
              required=True)
@click.option('--source-format', help='Query log file format. Only required when "custom" is used.',
              type=click.Choice(['json', 'jsonl'], case_sensitive=True),
              required=False)
@click.option('--mapping-file',
              help='Mapping of expected to existing query log fields. Only required if "custom" is used.',
              type=click.Path(exists=True),
              required=False)
@click_config_file.configuration_option(settings.OPTION_FILE_FLAG)
def configure_query_log_events(ctx, **kwargs):
    """
    Configure S3 query log events for a lake
    """
    EventsOnboardingService(config=ctx['config']).configure_query_log_events(**kwargs)


@integrations.command(help=f'Disable S3 events for Airflow task logs.')
@click.pass_obj
@click.option('--name', help='Resource name (only required if more than one exists)')
@click_config_file.configuration_option(settings.OPTION_FILE_FLAG)
def disable_airflow_log_events(ctx, **kwargs):
    """
    Disable S3 events for Airflow task logs
    """
    EventsOnboardingService(config=ctx['config']).disable_airflow_log_events(**kwargs)


@integrations.command(help=f'Disable S3 metadata events.')
@click.pass_obj
@click.option('--name', help='Resource name (only required if more than one exists)')
@click_config_file.configuration_option(settings.OPTION_FILE_FLAG)
def disable_metadata_events(ctx, **kwargs):
    """
    Configure S3 metadata events
    """
    EventsOnboardingService(config=ctx['config']).disable_metadata_events(**kwargs)


@integrations.command(help=f'Disable S3 query log events.')
@click.pass_obj
@click.option('--name', help='Resource name (only required if more than one exists)')
@click_config_file.configuration_option(settings.OPTION_FILE_FLAG)
def disable_query_log_events(ctx, **kwargs):
    """
    Configure S3 query log events
    """
    EventsOnboardingService(config=ctx['config']).disable_query_log_events(**kwargs)


@integrations.command(help=f'Setup a Tableau integration. {BI_VERBIAGE}.')
@click.pass_obj
@click.option('--token-name', help='Name for the personal access token.', cls=AdvancedOptions,
              mutually_exclusive_options=['password', 'username'], required_with_options=['token_value'],
              at_least_one_set=['password', 'username', 'token_name', 'token_value'])
@click.option('--token-value', help=f'Value for the personal access token. {PASSWORD_VERBIAGE}.', cls=AdvancedOptions,
              mutually_exclusive_options=['password', 'username'], required_with_options=['token_name'],
              prompt_if_requested=True)
@click.option('--password', help=f'Password for the service account. {PASSWORD_VERBIAGE}.', cls=AdvancedOptions,
              mutually_exclusive_options=['token_name', 'token_value'], required_with_options=['user'],
              prompt_if_requested=True)
@click.option('--user', help='Username for the service account.', cls=AdvancedOptions,
              mutually_exclusive_options=['token_name', 'token_value'], required_with_options=['password'])
@click.option('--site-name', help='The Tableau site name.', required=True)
@click.option('--server-name', help='The Tableau server name.', required=True)
@add_common_options(BI_OPTIONS)
@add_common_options(ONBOARDING_CONFIGURATION_OPTIONS)
@click_config_file.configuration_option(settings.OPTION_FILE_FLAG)
def add_tableau(ctx, user, **kwargs):
    """
    Onboard a tableau connection
    """
    ReportsOnboardingService(config=ctx['config']).onboard_tableau(username=user, **kwargs)


@integrations.command(help=f'Setup a Looker metadata integration. {BI_VERBIAGE}.')
@click.pass_obj
@click.option('--host-url', 'base_url', help='Looker host url.', required=True)
@click.option('--client-id', help='Looker client id.', required=True)
@click.option('--client-secret', help=f'Looker client secret (API key). {PASSWORD_VERBIAGE}.',
              required=True, cls=AdvancedOptions, prompt_if_requested=True)
@add_common_options(BI_OPTIONS)
@add_common_options(ONBOARDING_CONFIGURATION_OPTIONS)
def add_looker(ctx, **kwargs):
    """
    Onboard a looker metadata connection
    """
    ReportsOnboardingService(config=ctx['config']).onboard_looker_metadata(**kwargs)


@integrations.command(help=f'Setup a Looker ML (git) integration. {BI_VERBIAGE}.')
@click.pass_obj
@click.option('--ssh-key', help='The ssh key for git ssh integrations.', required=False,
              type=click.Path(dir_okay=False, exists=True),
              cls=AdvancedOptions, mutually_exclusive_options=['token', 'username'])
@click.option('--repo-url', help='Repository URL as ssh://[user@]server/project.git or the shorter '
                                 'form [user@]server:project.git for ssh. For https, use https://server/project.git.',
              required=True)
@click.option('--token', help='Git Access Token to be used for Https instead of ssh key.', required=False,
              cls=AdvancedOptions, mutually_exclusive_options=['ssh-key'])
@click.option('--username', help='Git username to be used in conjunction with the access token. This is only '
                                 'required for BitBucket integrations.',
              cls=AdvancedOptions, required=False, mutually_exclusive_options=['ssh-key'])
@add_common_options(ONBOARDING_CONFIGURATION_OPTIONS)
def add_looker_git(ctx, **kwargs):
    """
    Onboard a looker metadata connection
    """
    ReportsOnboardingService(config=ctx['config']).onboard_looker_git(**kwargs)


@integrations.command(help=f'Setup a Power BI integration. {BI_VERBIAGE}.')
@click.pass_obj
@click.option('--tenant-id', help='The tenant ID from the Azure Active Directory.', required=True)
@click.option('--auth-mode', help='Authentication Mode. We support service principal and master user two auth types',
              required=True, type=click.Choice(['SERVICE_PRINCIPAL', 'MASTER_USER']))
@click.option('--client-id', help='App registration application ID for accessing Power BI.',
              required=True, cls=AdvancedOptions)
@click.option('--client-secret', help='Secret for the application to access the Power BI. Set only when auth-mode is '
                                      'SERVICE_PRINCIPAL', required=False, cls=AdvancedOptions,
              mutually_exclusive_options=['username', 'password'], prompt_if_requested=True)
@click.option('--username', help='Username for accessing the Power BI. Set only when auth-mode is MASTER_USER.',
              cls=AdvancedOptions, required=False, mutually_exclusive_options=['client-secret'])
@click.option('--password', help='Password for accessing the Power BI. Set only when auth-mode is MASTER_USER.',
              cls=AdvancedOptions, required=False, mutually_exclusive_options=['client-secret'],
              prompt_if_requested=True)
@add_common_options(ONBOARDING_CONFIGURATION_OPTIONS)
def add_power_bi(ctx, **kwargs):
    """
    Onboard a Power BI connection
    """
    ReportsOnboardingService(config=ctx['config']).onboard_power_bi(**kwargs)


@integrations.command(help='Setup a dbt Cloud integration.')
@click.pass_obj
@click.option('--dbt-cloud-api-token', 'dbt_cloud_api_token', help=f'dbt Cloud API token. {PASSWORD_VERBIAGE}.',
              required=True, cls=AdvancedOptions, prompt_if_requested=True)
@click.option('--dbt-cloud-account-id', 'dbt_cloud_account_id', help='dbt Cloud Account ID.', required=True)
@click.option('--dbt-cloud-base-url', 'dbt_cloud_base_url', help='dbt Cloud Base URL.', required=False)
@add_common_options(warehouse_select_option())
@add_common_options(ONBOARDING_CONFIGURATION_OPTIONS)
def add_dbt_cloud(ctx, name, **kwargs):
    """
    Onboard a dbt cloud connection
    """
    DbtCloudOnboardingService(config=ctx['config']).onboard_dbt_cloud(
        warehouseName=name, **kwargs
    )


@integrations.command(help='List all active connections.', name='list')
@click.pass_obj
@click_config_file.configuration_option(settings.OPTION_FILE_FLAG)
def display_integrations(ctx):
    """
    Display active integrations
    """
    OnboardingStatusService(config=ctx['config']).display_integrations()


@integrations.command(help='Create an IAM role from a policy FILE. '
                           'The returned role ARN and external id should be used for adding lake assets.')
@click.pass_obj
@click.argument('file', type=click.Path(dir_okay=False, exists=True))
@click.option('--aws-profile', required=False,
              help='Override the AWS profile used by the CLI, which determines where the role is created. '
                   'This can be helpful when the account that manages the asset is not the same as the collector.')
def create_role(ctx, file, aws_profile):
    """
    Create a collector compatible role from the provided policy
    """
    CloudResourceService(config=ctx['config'], aws_profile_override=aws_profile).create_role(path_to_policy_doc=file)


@integrations.command(help='Update credentials for a connection. Only replaces/inserts the keys in changes by default.', name='update')
@click.pass_obj
@add_common_options(CONNECTION_OPTIONS)
@click.option('--changes', help="""
              Credential key,value pairs as JSON.
              \b
              \n
              E.g. --changes '{"user":"Apollo"}'
              """, required=True, callback=validate_json_callback)
@click.option('--skip-validation', help='Skip validating credentials.', default=False, show_default=True, is_flag=True)
@click.option('--replace-all', help='Replace all credentials rather than just inserting/updating the keys in changes.', default=False, show_default=True, is_flag=True)
@click_config_file.configuration_option(settings.OPTION_FILE_FLAG)
def update_credentials(ctx, connection_id, changes, skip_validation, replace_all):
    """
    Update credentials for a connection
    """
    ConnectionOperationsService(config=ctx['config']).update_credentials(
        connection_id=connection_id,
        changes=changes,
        should_validate=not skip_validation,
        should_replace=replace_all
    )


@integrations.command(help='Remove an existing connection. Deletes any associated jobs, monitors, etc.', name='remove')
@click.pass_obj
@add_common_options(CONNECTION_OPTIONS)
@click.option('--no-prompt', help='Don\'t ask for confirmation.', default=False, show_default=True, is_flag=True)
@click_config_file.configuration_option(settings.OPTION_FILE_FLAG)
def remove_connection(ctx, **kwargs):
    """
    Remove connection by ID
    """
    ConnectionOperationsService(config=ctx['config']).remove_connection(**kwargs)


@integrations.command(help='Retest an existing connection.', name='test')
@click.pass_obj
@add_common_options(CONNECTION_OPTIONS)
@click_config_file.configuration_option(settings.OPTION_FILE_FLAG)
def echo_test_existing(ctx, **kwargs):
    """
    Tests an existing connection and echos results in pretty JSON.
    """
    ConnectionOperationsService(config=ctx['config']).echo_test_existing(**kwargs)


@integrations.command(help='Setup complete S3 event notifications for a lake.')
@click.pass_obj
@add_common_options(S3_BUCKET_OPTIONS)
@add_common_options(EVENT_TYPE_OPTIONS)
@add_common_options(COLLECTOR_PROFILE_OPTIONS)
@add_common_options(RESOURCE_PROFILE_OPTIONS)
@add_common_options(AUTO_YES_OPTIONS)
@add_common_options(DISAMBIGUATE_DC_OPTIONS)
@click_config_file.configuration_option(settings.OPTION_FILE_FLAG)
def add_events(ctx, **kwargs):
    CloudResourceService(config=ctx['config'], aws_wrapper=None).add_events(**kwargs)


@integrations.command(help='Setup Event Topic for S3 event notifications in a lake.')
@click.pass_obj
@add_common_options(S3_BUCKET_OPTIONS)
@add_common_options(EVENT_TYPE_OPTIONS)
@add_common_options(RESOURCE_PROFILE_OPTIONS)
@add_common_options(AUTO_YES_OPTIONS)
@add_common_options(DISAMBIGUATE_DC_OPTIONS)
@click_config_file.configuration_option(settings.OPTION_FILE_FLAG)
def create_event_topic(ctx, **kwargs):
    CloudResourceService(config=ctx['config'], aws_wrapper=None).create_event_topic(**kwargs)

@integrations.command(help='Setup Bucket Side S3 event infrastructure for a lake.')
@click.pass_obj
@add_common_options(S3_BUCKET_OPTIONS)
@add_common_options(EVENT_TYPE_OPTIONS)
@add_common_options(RESOURCE_PROFILE_OPTIONS)
@add_common_options(AUTO_YES_OPTIONS)
@add_common_options(DISAMBIGUATE_DC_OPTIONS)
@click_config_file.configuration_option(settings.OPTION_FILE_FLAG)
def create_bucket_side_event_infrastructure(ctx, **kwargs):
    CloudResourceService(config=ctx['config'], aws_wrapper=None).create_bucket_side_event_infrastructure(**kwargs)


@integrations.command(help='Create an integration key. The resulting key id and secret will be printed to the console.')
@click.pass_obj
@click.option('--description',
              required=True,
              help='Key description.')
@click.option('--scope',
              required=True,
              type=click.Choice(IntegrationKeyScope.values(), case_sensitive=False),
              help='Key scope (integration the key can be used for).')
@click_config_file.configuration_option(settings.OPTION_FILE_FLAG)
def create_key(ctx, **kwargs):
    IntegrationKeyService(config=ctx['config']).create(**kwargs)


@integrations.command(help='Delete an integration key.')
@click.pass_obj
@click.option('--key-id', required=True, help='Integration key id.')
@click_config_file.configuration_option(settings.OPTION_FILE_FLAG)
def delete_key(ctx, **kwargs):
    IntegrationKeyService(config=ctx['config']).delete(**kwargs)


@integrations.command(help='List all integration keys.')
@click.pass_obj
@click_config_file.configuration_option(settings.OPTION_FILE_FLAG)
def list_keys(ctx):
    IntegrationKeyService(config=ctx['config']).get_all()

@integrations.command(help='Set the name of a Warehouse.')
@click.pass_obj
@click.option('--current-name', required=True, help='Current Name of the Warehouse')
@click.option('--new-name', required=True, help='Name to give the Warehouse')
def set_warehouse_name(ctx, **kwargs):
    ConnectionOperationsService(config=ctx['config']).set_warehouse_name(**kwargs)


@integrations.command(help='Update Databricks Notebook to the latest version.')
@click.pass_obj
@add_common_options(CONNECTION_OPTIONS)
def update_databricks_notebook(ctx, **kwargs):
    DatabricksOnboardingService(config=ctx['config']).update_databricks_notebook(**kwargs)


@integrations.command(help='Get the Databricks job info for your connection.')
@click.pass_obj
@add_common_options(CONNECTION_OPTIONS)
def show_databricks_metadata_job_info(ctx, **kwargs):
    DatabricksOnboardingService(config=ctx['config']).get_databricks_job_info(**kwargs)


@integrations.command(help='Get the most up to date databricks notebook version.')
@click.pass_obj
def show_current_notebook_version(ctx):
    DatabricksOnboardingService(config=ctx['config']).get_current_databricks_notebook_version()
