import logging
import azure.functions as func
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
import json
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        data = req.get_json()
        rg_name = data.get("resourceGroupName")
        rg_location = data.get("resourceGroupRegion")

        if not rg_name or not rg_location:
            return func.HttpResponse("Missing parameters.", status_code=400)

        credential = DefaultAzureCredential()
        subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]
        resource_client = ResourceManagementClient(credential, subscription_id)

        result = resource_client.resource_groups.create_or_update(
            rg_name, {"location": rg_location}
        )

        return func.HttpResponse(
            json.dumps({
                "status": "Success",
                "resourceGroup": {
                    "name": result.name,
                    "location": result.location
                }
            }),
            mimetype="application/json"
        )

    except Exception as e:
        logging.error(str(e))
        return func.HttpResponse("Error: " + str(e), status_code=500)