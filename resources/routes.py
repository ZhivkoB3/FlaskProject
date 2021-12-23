from resources.auth import Login, Register, RegisterPaymentProvider
from resources.energy import ListUpdateWaterTable, ListUpdateGasTable, WaterDataDeleteAndUpdate

routes = (
    (Register, '/register'),
    (Login, '/login'),
    (RegisterPaymentProvider, '/register/payment_provider'),
    # water data related
    (ListUpdateWaterTable, '/energy/water'),
    (WaterDataDeleteAndUpdate, '/energy/water/<int:id_>'),
    # gas data related
    (ListUpdateGasTable, '/energy/gas')

)
