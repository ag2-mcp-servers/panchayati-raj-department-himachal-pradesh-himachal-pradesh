# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T15:05:51+00:00



import argparse
import json
import os
from typing import *
from typing import Optional, Union

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import APIKeyHeader, BaseSecurity

from models import (
    FmcerCertificatePostRequest,
    FmcerCertificatePostResponse,
    FmcerCertificatePostResponse1,
    FmcerCertificatePostResponse2,
    FmcerCertificatePostResponse3,
    FmcerCertificatePostResponse4,
    FmcerCertificatePostResponse5,
    FmcerCertificatePostResponse6,
)

app = MCPProxy(
    description="Parivar Patra (http://aadhaar.hp.gov.in/epanchayat/) is the online service  portal by Govt. of Himachal Pradesh. Parivar Register issued online certificate can be pulled into citizens' DigiLocker accounts.",
    termsOfService='https://apisetu.gov.in/terms.php',
    title='Panchayati Raj Department, Himachal Pradesh, Himachal Pradesh',
    version='3.0.0',
    servers=[{'url': 'https://apisetu.gov.in/hppanchayat/v3'}],
)


@app.post(
    '/fmcer/certificate',
    description=""" API to verify Family Membership Certificate. """,
    tags=['family_membership_management'],
    security=[
        APIKeyHeader(name="X-APISETU-APIKEY"),
        APIKeyHeader(name="X-APISETU-CLIENTID"),
    ],
)
def fmcer(body: FmcerCertificatePostRequest = None):
    """
    Family Membership Certificate
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
