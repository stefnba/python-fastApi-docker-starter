def connection_url_postgresql(
    host: str, port: int | str, database: str | None, user: str | None, password: str | None
):
    """
    Creates PostgreSQL connection string from individual connection parameters
    """
    if isinstance(port, str):
        port = int(port)

    if user is None:
        raise Exception("User cannot must be provided")
    if database is None:
        raise Exception("Database cannot must be provided")

    return f'postgresql://{user}{":" if password is not None else ""}{password}@{host}:{port}/{database}'
