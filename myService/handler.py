def handle1(event, context):
    """handle a request to the function
    Args:
        event (dict): request params
        context (dict): function call metadata
    """

    return {
        "message": "Hello From Python3 runtime on Serverless Framework and Scaleway Functions (1)"
    }

def handle2(event, context):
    """handle a request to the function
    Args:
        event (dict): request params
        context (dict): function call metadata
    """

    return {
        "message": "Hello From Python3 runtime on Serverless Framework and Scaleway Functions (2)"
    }
