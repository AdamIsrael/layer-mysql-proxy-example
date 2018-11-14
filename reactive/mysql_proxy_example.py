from charmhelpers.core import hookenv
from charms.reactive import (
    when,
    when_all,
    when_any,
    when_not,
    set_flag,
    clear_flag,
)
from charms.reactive import endpoint_from_flag
from charms.sshproxy import sftp
from jinja2 import Template
import tempfile


@when_not('db-proxy.installed')
def install_db_proxy():
    set_flag('db-proxy.installed')


@when_all('db.available', 'config.set.admin-pass')
@when_any('db.changed', 'config.changed.admin-pass')
def render_config():
    """Render a configuration file to be used by our VNF."""

    """
    A relation endpoint provides information provided, by the mysql service.
    This will include:
    - connection string
    - host name
    - port
    - database name
    - user name
    - password
    """
    mysql = endpoint_from_flag('db.available')

    with open('../templates/db.j2', 'r') as f:
        """
        Once we've received the mysql endpoint, we can render a configuration
        file to be used by our VNF. The template shown here is just an example
        to show that you can take this relationship information and use it
        with a VNF running outside of Juju.
        """

        t = Template(f.read())

        # Render a new configuration for your database client
        myconfig = t.render(
            admin_pass=hookenv.config('admin-pass'),
            db_conn=mysql.connection_string(),
        )

        """
        What next?

        Now that you have the new config, you should copy it to your VNF. If
        you're using the sshproxy layer, you can use it's `sftp` method.
        """

    """
    Set a flag so that your VNF service can be restarted to pick up the new
    configuration.
    """
    set_flag('vnf.needs-restart')

    clear_flag('db.changed')
    clear_flag('config.changed.admin-pass')


@when('vnf.needs-restart')
def restart_service():
    """Restart your application

    If your application needs to be restarted, such as after a configuration change, include the command to do so below.
    """

    # Run command to restart application here.

    clear_flag('charm.needs-restart')
