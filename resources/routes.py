
from resources.auth import Login, Register, RegisterPaymentProvider

routes = (
    (Register, '/register/<str>'),
    (Login, '/login'),
    (RegisterPaymentProvider, '/register/payment_provider')
)
