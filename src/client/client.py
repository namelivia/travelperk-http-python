class Client:
    def __init__(api_key: str):
        # TODO: Send  the following headers
        {
            "Api-Version": "1",
            "Authorization": "ApiKey " + api_key,
        }

    def set_authorization_code(authorization_code: str) -> str:
        raise NotImplementedError(
            "No authorization code needed for simple api key authentication"
        )

    def get_auth_uri(target_link_uri: str) -> str:
        raise NotImplementedError(
            "No authorization URI for simple api key authentication"
        )
