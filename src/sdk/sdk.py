"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .context import Context
from .insights import Insights
from .job import Job
from .pipeline import Pipeline
from .project import Project
from .schedule import Schedule
from .sdkconfiguration import SDKConfiguration
from .user import User
from .webhook import Webhook
from .workflow import Workflow
from sdk import utils
from sdk.models import shared

class SDK:
    r"""CircleCI API: This describes the resources that make up the CircleCI API v2.
    
    # Authentication
    
    <!-- ReDoc-Inject: <security-definitions> -->
    """
    context: Context
    insights: Insights
    job: Job
    pipeline: Pipeline
    project: Project
    schedule: Schedule
    user: User
    webhook: Webhook
    workflow: Workflow

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 security: shared.Security = None,
                 server_idx: int = None,
                 server_url: str = None,
                 url_params: dict[str, str] = None,
                 client: requests_http.Session = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param security: The security details required for authentication
        :type security: shared.Security
        :param server_idx: The index of the server to use for all operations
        :type server_idx: int
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session        
        """
        if client is None:
            client = requests_http.Session()
        
        security_client = utils.configure_security_client(client, security)
        
        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        self.sdk_configuration = SDKConfiguration(client, security_client, server_url, server_idx)
       
        self._init_sdks()
    
    def _init_sdks(self):
        self.context = Context(self.sdk_configuration)
        self.insights = Insights(self.sdk_configuration)
        self.job = Job(self.sdk_configuration)
        self.pipeline = Pipeline(self.sdk_configuration)
        self.project = Project(self.sdk_configuration)
        self.schedule = Schedule(self.sdk_configuration)
        self.user = User(self.sdk_configuration)
        self.webhook = Webhook(self.sdk_configuration)
        self.workflow = Workflow(self.sdk_configuration)
    