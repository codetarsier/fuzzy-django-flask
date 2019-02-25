# system config
from flask import redirect, url_for
from config.constants import app, db, migrate, app_admin, manager


# application imports
from portal_setup.urls import  portal_setup_router

# application admin
from portal_setup.admin import port_setup_admin

# application urls
app.register_blueprint(portal_setup_router,  url_prefix='/')

@app.route("/")
def index():
    return redirect(url_for('portal_setup.portals'))


@manager.command
def runserver():
    app.run(
        host=app.config.get('SERVER_HOST'),
        port=app.config.get('SERVER_PORT'),
        use_reloader=app.config.get('DEBUG'),
        debug=app.config.get('DEBUG')
    )

if __name__ == "__main__":
    # show database url
    print(' *{} [database] : [{}] {}'.format('\033[91m', app.config.get('SQLALCHEMY_DATABASE_URI'), '\033[0m'))

    manager.run()
