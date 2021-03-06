"""Display a subtitute from the user's product choice."""

from application.view.substitute import SubstituteMenu


class SubstituteController:
    """Display a substitute."""

    def __init__(self, product):
        """Initialize a substitute."""
        self.product = product
        self.substitute_view = SubstituteMenu()
        self.choice = ""

    def input(self):
        """Handle input user of the substitute menu."""
        self.choice = input()
        return self.choice

    def show(self, products):
        """Handle the substitute menu."""
        self.substitute_view.show(products)