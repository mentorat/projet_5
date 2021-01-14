"""Class Product."""

from application.model.connection import connection
from application.model.nutriscore import Nutriscore


class Product:
    """Class product."""

    def __init__(self):
        """Initiate product class."""

    def get_idproduct(self, name_product):
        """Returns the id according to the name."""
        cursor = connection.get_cursor()

        id_query = (
            "SELECT id FROM PRODUCT WHERE product_name ='%s'" % name_product
        )
        cursor.execute(id_query)
        product_id = cursor.fetchone()[0]
        breakpoint()

        connection.db.commit()
        cursor.close()
        return product_id

    @classmethod
    def save(cls, cleaned_product: list) -> bool:
        """Save products in the database."""
        cursor = connection.get_cursor()
        nutri_score = Nutriscore()

        add_products = (
            "INSERT IGNORE INTO PRODUCT "
            "(id, product_name, product_description, shop, substitute, nutri_id, product_url) "
            "VALUES (%(id)s, %(name)s, %(description)s, %(shop)s, "
            "%(substitute)s, %(nutri_id)s, %(url)s)"
        )

        for product in cleaned_product:
            data_products = {
                "id": None,
                "name": product.get("name"),
                "description": product.get("generic_name"),
                "shop": product.get("stores"),
                "substitute": None,
                "nutri_id": nutri_score.get_idnutriscore(
                    product.get("nutriscore")
                ),
                "url": product.get("url"),
            }
            cursor.execute(add_products, data_products)

        connection.db.commit()
        cursor.close()
        return True
