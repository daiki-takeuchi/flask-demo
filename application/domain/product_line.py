from sqlalchemy import Column, Integer, String

from application import Model


class ProductLine(Model):
    __tablename__ = 'product_line'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_line = Column(String(32), nullable=False)
    text_description = Column(String(1024), nullable=False)
    html_description = Column(String(1024), nullable=False)
    image = Column(String(1024), nullable=False)

    def __init__(self,
                 product_line=None,
                 text_description=None,
                 html_description=None,
                 image=None):
        self.product_line = product_line
        self.text_description = text_description
        self.html_description = html_description
        self.image = image

    def __repr__(self):
        return '<ProductLine {}[ID:{}>'.format(self.product_line, self.id)
