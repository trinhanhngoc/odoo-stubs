from ..models import BaseModel as BaseModel, MAGIC_COLUMNS as MAGIC_COLUMNS
from functools import partial as partial
from odoo.tools import pycompat as pycompat
from typing import Any, Optional

NOT_OPERATOR: str
OR_OPERATOR: str
AND_OPERATOR: str
DOMAIN_OPERATORS: Any
TERM_OPERATORS: Any
NEGATIVE_TERM_OPERATORS: Any
DOMAIN_OPERATORS_NEGATION: Any
TERM_OPERATORS_NEGATION: Any
TRUE_LEAF: Any
FALSE_LEAF: Any
TRUE_DOMAIN: Any
FALSE_DOMAIN: Any
_logger: Any

def normalize_domain(domain: Any): ...
def is_false(model: Any, domain: Any): ...
def combine(operator: Any, unit: Any, zero: Any, domains: Any): ...
def AND(domains: Any): ...
def OR(domains: Any): ...
def distribute_not(domain: Any): ...
def _quote(to_quote: Any): ...
def generate_table_alias(src_table_alias: Any, joined_tables: Any = ...): ...
def get_alias_from_query(from_query: Any): ...
def normalize_leaf(element: Any): ...
def is_operator(element: Any): ...
def is_leaf(element: Any, internal: bool = ...): ...
def select_from_where(cr: Any, select_field: Any, from_table: Any, where_field: Any, where_ids: Any, where_operator: Any): ...
def select_distinct_from_where_not_null(cr: Any, select_field: Any, from_table: Any): ...
def get_unaccent_wrapper(cr: Any): ...

class ExtendedLeaf:
    join_context: Any = ...
    leaf: Any = ...
    model: Any = ...
    _models: Any = ...
    def __init__(self, leaf: Any, model: Any, join_context: Optional[Any] = ..., internal: bool = ...) -> None: ...
    def __str__(self): ...
    def generate_alias(self): ...
    def add_join_context(self, model: Any, lhs_col: Any, table_col: Any, link: Any) -> None: ...
    def get_join_conditions(self): ...
    def get_tables(self): ...
    def _get_context_debug(self): ...
    def check_leaf(self, internal: bool = ...) -> None: ...
    def is_operator(self): ...
    def is_true_leaf(self): ...
    def is_false_leaf(self): ...
    def is_leaf(self, internal: bool = ...): ...
    def normalize_leaf(self): ...

def create_substitution_leaf(leaf: Any, new_elements: Any, new_model: Optional[Any] = ..., internal: bool = ...): ...

class expression:
    _unaccent: Any = ...
    joins: Any = ...
    root_model: Any = ...
    expression: Any = ...
    def __init__(self, domain: Any, model: Any) -> None: ...
    def get_tables(self): ...
    result: Any = ...
    stack: Any = ...
    def parse(self): ...
    def __leaf_to_sql(self, eleaf: Any): ...
    def to_sql(self): ...