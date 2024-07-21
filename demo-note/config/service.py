from utilmeta import UtilMeta
from config.conf import configure
from config.env import env
import django

service = UtilMeta(
    __name__,
    name="demo-note",
    description="",
    backend=django,
    production=env.PRODUCTION,
    version=(0, 1, 0),
    host="demo-note.com" if env.PRODUCTION else "127.0.0.1",
    port=80 if env.PRODUCTION else 8000,
    api="service.api.RootAPI",
    route="/api",
)
configure(service)
