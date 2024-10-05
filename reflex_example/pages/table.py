"""The table page."""

import reflex_local_auth
from ..templates import template
from ..backend.table_state import TableState
from ..views.table import main_table

import reflex as rx

@reflex_local_auth.require_login
@template(route="/table", title="Table", on_load=TableState.load_entries)
def table() -> rx.Component:
    """The table page.

    Returns:
        The UI for the table page.
    """
    return rx.vstack(
        rx.heading("Table", size="5"),
        main_table(),
        spacing="8",
        width="100%",
    )
