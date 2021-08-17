from app.api.api_v1.endpoints.user_view import user
def init_app(app):
    """
    Register app blueprints over here
    eg: # app.register_blueprint(user, url_prefix="/api/users")
    :param app:
    :return:
    """

    app.register_blueprint(user, url_prefix="/api/user")
