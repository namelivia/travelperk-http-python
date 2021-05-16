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
