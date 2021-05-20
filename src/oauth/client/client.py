from oauth.authorizator.authorizator import Authorizator
from oauth.missing_code_exception import MissingCodeException


class Client:
    def __init__(self, authorizator: Authorizator):
        # TODO: This class would be a bit different.
        # Should implement a python oauth client and provide info from the authorizator.
        # And it will depend a lot on the client used.
        # Note that this header should be passed in every request:
        {"Api-Version": "1"}

    def get_auth_uri(self, target_link_uri: str) -> str:
        return self.authorizator.get_auth_uri(target_link_uri)

    def check_authorized(self) -> None:
        if not self.authorizator.is_authorized():
            raise MissingCodeException("No auth code or token")
        return None

    def set_authorization_code(self, code: str) -> "Client":
        self.authorizator.set_authorization_code(code)
        # $this->middlewareFactory->recreateOAuthMiddleware();
        return self

    # Checks if authorized before every HTTP method
    def get(self, uri: str, options=[]):
        self.check_authorized()
        # return parent::get($uri, $options);

    def post(self, uri: str, options=[]):
        self.check_authorized()
        # return parent::post($uri, $options);

    def put(self, uri: str, options=[]):
        self.check_authorized()
        # return parent::put($uri, $options);

    def patch(self, uri: str, options=[]):
        self.check_authorized()
        # return parent::patch($uri, $options);

    def delete(self, uri: str, options=[]):
        self.check_authorized()
        # return parent::delete($uri, $options);


# TODO: Here is an example of a python oauth client:
"""
class Client:
    def __init__(self, client_id, client_secret, redirect_uri):
        pass

    def test(self):
        scope = [
            "https://www.googleapis.com/auth/userinfo.email",
            "https://www.googleapis.com/auth/userinfo.profile",
        ]
        oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=scope)
        authorization_url, state = oauth.authorization_url(
            "https://accounts.google.com/o/oauth2/auth",
            # access_type and prompt are Google specific extra
            # parameters.
            access_type="offline",
            prompt="select_account",
        )

        print "Please go to %s and authorize access." % authorization_url
        authorization_response = raw_input("Enter the full callback URL")

        token = oauth.fetch_token(
            "https://accounts.google.com/o/oauth2/token",
            authorization_response=authorization_response,
            # Google specific extra parameter used for client
            # authentication
            client_secret=client_secret,
        )
        r = oauth.get("https://www.googleapis.com/oauth2/v1/userinfo")
"""
