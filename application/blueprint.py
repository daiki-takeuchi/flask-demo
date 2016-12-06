def register(app):
    from application.controllers import customer
    from application.controllers import orders
    from application.controllers import payment
    from application.controllers import product
    from application.controllers import product_line

    app.register_blueprint(customer.bp)
    app.register_blueprint(orders.bp)
    app.register_blueprint(payment.bp)
    app.register_blueprint(product.bp)
    app.register_blueprint(product_line.bp)
