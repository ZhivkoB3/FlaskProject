from sqlalchemy import func

from db import db
from models.enums import State


class PaymentRequestsModel(db.Model):
    __tablename__ = "payment_requests"

    pk = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer, nullable=False)
    metric = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)
    total_invoice_amount = db.Column(db.String, nullable=False)
    created_on = db.Column(db.DateTime, server_default=func.now())
    updated_on = db.Column(db.DateTime, onupdate=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("payment_receivers.pk"))
    updated_by = db.Column(db.Integer, db.ForeignKey("payment_receivers.pk"))
    state = db.Column(db.Enum(State), default=State.pending, nullable=False)
