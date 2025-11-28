# Custom Order Model
class CustomOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    delivery_date = db.Column(db.DateTime)
    urgency = db.Column(db.String(50))
    instructions = db.Column(db.Text)
    design_image = db.Column(db.String(150))
    status = db.Column(db.String(50), default='Pending')  # Cutting → Sewing → Finishing → Ready
    tasks = db.relationship('OrderTask', backref='custom_order', lazy=True)

# Measurement Model
class Measurement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('custom_order.id'))
    garment_type = db.Column(db.String(50))  # Shirt, Pant, Blouse, etc.
    neck = db.Column(db.Float)
    chest = db.Column(db.Float)
    waist = db.Column(db.Float)
    hip = db.Column(db.Float)
    length = db.Column(db.Float)
    sleeve = db.Column(db.Float)

# Worker Task Model
class OrderTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('custom_order.id'))
    worker_id = db.Column(db.Integer, db.ForeignKey('worker.id'))
    task_type = db.Column(db.String(50))  # Cutting, Sewing, Finishing
    status = db.Column(db.String(50), default='Pending')

# Cart Model
class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer, default=1)

# Payment Model
class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    amount = db.Column(db.Float)
    payment_method = db.Column(db.String(50))  # COD, Online
    status = db.Column(db.String(50), default='Pending')

# Invoice Model
class Invoice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    invoice_date = db.Column(db.DateTime, default=datetime.utcnow)
    pdf_file = db.Column(db.String(150))
