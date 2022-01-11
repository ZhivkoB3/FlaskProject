from resources.auth import Login, Register, ServiceProvider, LoginServiceProvider
from resources.energy import (
    ListUpdateWaterTable,
    ListUpdateGasTable,
    WaterDataDeleteAndUpdate,
    GasDataDeleteAndUpdate,
    ListUpdateElectricityTable,
    ElectricityDeleteAndUpdate,
    ListUpdateCompressorsTable,
    CompressorsDeleteAndUpdate,
)
from resources.payment_requests import (
    PaymentRequestsDeleteAndUpdate,
    ListUpdatePaymentRequestsTable,
    RejectPaymentRequest,
    ApprovePaymentRequest,
)
from resources.user import ChangeUserRole, ChangeServiceProviderRole

routes = (
    (Register, "/register"),
    (Login, "/login"),
    # Service providers
    (
        ServiceProvider,
        "/register/service_provider",
    ),
    (LoginServiceProvider, "/login/service_provider"),
    # water data related
    (ListUpdateWaterTable, "/energy/water"),
    (WaterDataDeleteAndUpdate, "/energy/water/<int:id_>"),
    # gas data related
    (ListUpdateGasTable, "/energy/gas"),
    (GasDataDeleteAndUpdate, "/energy/gas/<int:id_>"),
    # electricity data related
    (ListUpdateElectricityTable, "/energy/electricity"),
    (ElectricityDeleteAndUpdate, "/energy/electricity/<int:id_>"),
    # compressors data related
    (ListUpdateCompressorsTable, "/energy/compressors"),
    (CompressorsDeleteAndUpdate, "/energy/compressors/<int:id_>"),
    # payments requests related
    (ListUpdatePaymentRequestsTable, "/payments"),
    (PaymentRequestsDeleteAndUpdate, "/payments/<int:id_>"),
    (ApprovePaymentRequest, "/accountants/payments/<int:id_>/approved"),
    (RejectPaymentRequest, "/accountants/payments/<int:id_>/rejected"),
    # Role change
    (ChangeUserRole, "/role_change/<int:id_>"),
    (ChangeServiceProviderRole, "/role_change_service_provider/<int:id_>"),
)
