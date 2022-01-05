from resources.auth import Login, Register, RegisterPaymentProvider
from resources.energy import ListUpdateWaterTable, ListUpdateGasTable, WaterDataDeleteAndUpdate, GasDataDeleteAndUpdate, \
    ListUpdateElectricityTable, ElectricityDeleteAndUpdate, ListUpdateCompressorsTable, CompressorsDeleteAndUpdate
from resources.user import ChangeUserRole

routes = (
    (Register, '/register'),
    (Login, '/login'),
    (RegisterPaymentProvider, '/register/payment_receiver'),
    # water data related
    (ListUpdateWaterTable, '/energy/water'),
    (WaterDataDeleteAndUpdate, '/energy/water/<int:id_>'),
    # gas data related
    (ListUpdateGasTable, '/energy/gas'),
    (GasDataDeleteAndUpdate, '/energy/gas/<int:id_>'),
    # electricity data related
    (ListUpdateElectricityTable, '/energy/electricity'),
    (ElectricityDeleteAndUpdate, '/energy/electricity/<int:id_>'),
    # compressors data related
    (ListUpdateCompressorsTable, '/energy/compressors'),
    (CompressorsDeleteAndUpdate, '/energy/compressors/<int:id_>'),
    (ChangeUserRole, '/role_change/<int:id_>')

)
