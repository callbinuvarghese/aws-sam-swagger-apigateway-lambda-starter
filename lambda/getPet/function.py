def handler(event, context):
    """Retrieve JSON from server."""
    # Business Logic Goes Here.
    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": {"id": 1, "name": "Kaiser", "type": "dog", "sub-type": "bulldog", "status": "available"}
    }
    return response