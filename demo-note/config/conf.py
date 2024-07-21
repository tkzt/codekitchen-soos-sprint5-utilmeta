from utilmeta import UtilMeta
from config.env import env


def configure(service: UtilMeta):
    from utilmeta.core.server.backends.django import DjangoSettings
    from utilmeta.core.orm import DatabaseConnections, Database

    service.use(DjangoSettings(apps_package="domain", secret_key=env.DJANGO_SECRET_KEY))
    service.use(
        DatabaseConnections(
            {
                "default": Database(
                    name="db",
                    engine="sqlite3",
                )
            }
        )
    )

    from utilmeta.ops.config import Operations
    from utilmeta.conf.time import Time

    service.use(
        Time(time_zone="UTC", use_tz=True, datetime_format="%Y-%m-%dT%H:%M:%SZ")
    )
    service.use(
        Operations(
            route="ops",
            max_backlog=50,
            database=Database(
                name="utilmeta_ops",
                engine="sqlite3",
            ),
            local_disabled=env.PRODUCTION,
            secure_only=env.PRODUCTION,
            trusted_hosts=[] if env.PRODUCTION else ["127.0.0.1"],
        )
    )
