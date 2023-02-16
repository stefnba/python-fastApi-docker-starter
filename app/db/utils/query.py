from sqlalchemy.exc import ResourceClosedError
from typing import TypeVar, Type, cast, Any, List
from ..db import DBSession

T = TypeVar("T")

class Query:
    @staticmethod
    def generate_db_session():
        session = DBSession()
        try:
            print("open")
            yield session
        finally:
            print("closed")
            session.close()

    @staticmethod
    def init_db_session():
        return next(Query.generate_db_session())

    @staticmethod
    def one(query) -> Any:
        """
        Executes query with fetch the first object or None.
        """
        with DBSession() as session:
            result = session.scalars(statement=query).first()
        return result

    @staticmethod
    def many(query, size: int | None = None) -> List[Any]:
        """
        Executes query with fetch many rows.
        """
        # db.execute(text('SELECT * FROM users')).mappings().all()
        with DBSession() as session:
            result = session.scalars(query).fetchmany(size)
        return cast(List[Any], result)

    def __execute(self, query, params: dict | None | list[dict] = None, commit=False, many=True):
        """
        Handles actual execution of queries and errors.
        """
        session = DBSession()

        try:
            result = session.scalars(query, params)
            if commit:
                session.commit()

            try:
                if many:
                    result = result.fetchall()
                else:
                    result = result.first()
                return result
            except ResourceClosedError:
                pass

        except Exception as error:
            print(error)
        finally:
            session.close()

        return None

    @classmethod
    def commit(cls, query, params: dict | None | list[dict] = None, type: T = None) -> T:
        """
        Executes an query and commits results to database. Used for insert and update.
        """
        many = False
        if isinstance(params, list):
            many = True

        return cast(T, cls().__execute(query=query, params=params, commit=True, many=many))
