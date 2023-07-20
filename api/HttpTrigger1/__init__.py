import logging
import json
import azure.functions as func
import requests

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    url = "https://sam-py-linux.azurewebsites.net/api/HttpTrigger1?"
    payload = {"name": name}

    response = requests.post(url, data=payload)

    if response.status_code != 200:
        return func.HttpResponse(
            f"Error: {response.content}",
            status_code=500
        )

    return func.HttpResponse(
        "Name sent successfully!",
        status_code=200
    )


    # logging.info('Python HTTP trigger function processed a request.')

    # name = req.params.get('name')
    # if not name:
    #     try:
    #         req_body = req.get_json()
    #     except ValueError:
    #         pass
    #     else:
    #         name = req_body.get('name')

    # if name:
    #     return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    # else:
    #     return func.HttpResponse(
    #          "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
    #          status_code=200
    #     )
