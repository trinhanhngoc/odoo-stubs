import psycopg2.extensions
from . import tools as tools
from .tools import pycompat as pycompat, ustr as ustr
from .tools.func import frame_codeinfo as frame_codeinfo
from typing import Any, Optional

_logger: Any

def unbuffer(symb: Any, cr: Any): ...
def undecimalize(symb: Any, cr: Any): ...
def adapt_string(adapted: Any): ...

re_from: Any
re_into: Any
sql_counter: int

class Cursor:
    IN_MAX: int = ...
    def check(f: Any): ...
    sql_from_log: Any = ...
    sql_into_log: Any = ...
    sql_log: Any = ...
    sql_log_count: int = ...
    _closed: bool = ...
    __pool: Any = ...
    dbname: Any = ...
    _serialized: Any = ...
    _cnx: Any = ...
    _obj: Any = ...
    __caller: Any = ...
    __closer: bool = ...
    _default_log_exceptions: bool = ...
    cache: Any = ...
    _event_handlers: Any = ...
    def __init__(self, pool: Any, dbname: Any, dsn: Any, serialized: bool = ...) -> None: ...
    def __build_dict(self, row: Any): ...
    def dictfetchone(self): ...
    def dictfetchmany(self, size: Any): ...
    def dictfetchall(self): ...
    def __del__(self) -> None: ...
    def execute(self, query: Any, params: Optional[Any] = ..., log_exceptions: Optional[Any] = ...): ...
    def split_for_in_conditions(self, ids: Any, size: Optional[Any] = ...): ...
    def print_log(self): ...
    def close(self): ...
    def _close(self, leak: bool = ...) -> None: ...
    def autocommit(self, on: Any) -> None: ...
    def after(self, event: Any, func: Any) -> None: ...
    def _pop_event_handlers(self): ...
    def commit(self): ...
    def rollback(self): ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None: ...
    def savepoint(self) -> None: ...
    def __getattr__(self, name: Any): ...
    @property
    def closed(self): ...

class TestCursor:
    _savepoint_seq: Any = ...
    _closed: bool = ...
    _cursor: Any = ...
    _lock: Any = ...
    _savepoint: Any = ...
    def __init__(self, cursor: Any, lock: Any) -> None: ...
    def close(self) -> None: ...
    def autocommit(self, on: Any) -> None: ...
    def commit(self) -> None: ...
    def rollback(self) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None: ...
    def __getattr__(self, name: Any): ...

class LazyCursor:
    _dbname: Any = ...
    _cursor: Any = ...
    _depth: int = ...
    def __init__(self, dbname: Optional[Any] = ...) -> None: ...
    @property
    def dbname(self): ...
    def __getattr__(self, name: Any): ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None: ...

class PsycoConnection(psycopg2.extensions.connection): ...

class ConnectionPool:
    def locked(fun: Any): ...
    _connections: Any = ...
    _maxconn: Any = ...
    _lock: Any = ...
    def __init__(self, maxconn: int = ...) -> None: ...
    def __repr__(self): ...
    def _debug(self, msg: Any, *args: Any) -> None: ...
    def borrow(self, connection_info: Any): ...
    def give_back(self, connection: Any, keep_in_pool: bool = ...) -> None: ...
    def close_all(self, dsn: Optional[Any] = ...) -> None: ...

class Connection:
    dbname: Any = ...
    dsn: Any = ...
    __pool: Any = ...
    def __init__(self, pool: Any, dbname: Any, dsn: Any) -> None: ...
    def cursor(self, serialized: bool = ...): ...
    serialized_cursor: Any = ...
    def __bool__(self) -> None: ...
    __nonzero__: Any = ...

def connection_info_for(db_or_uri: Any): ...

_Pool: Any

def db_connect(to: Any, allow_uri: bool = ...): ...
def close_db(db_name: Any) -> None: ...
def close_all() -> None: ...