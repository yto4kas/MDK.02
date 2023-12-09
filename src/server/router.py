from src.server.database import models as database_models
from src.server.database import pydantic_models
from src.server.service import RouterManager

routers = (
    RouterManager(
        database_model=database_models.Clients,
        pydantic_model=pydantic_models.Clients,
        prefix='/clients',
        tags=['Clients']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Pets,
        pydantic_model=pydantic_models.Pets,
        prefix='/pets',
        tags=['Pets']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Appointments,
        pydantic_model=pydantic_models.Appointments,
        prefix='/appointments',
        tags=['Appointments']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Veterinarians,
        pydantic_model=pydantic_models.Veterinarians,
        prefix='/veterinarians',
        tags=['Veterinarians']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Services,
        pydantic_model=pydantic_models.Services,
        prefix='/services',
        tags=['Services']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Treatments,
        pydantic_model=pydantic_models.Treatments,
        prefix='/treatments',
        tags=['Treatments']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Medications,
        pydantic_model=pydantic_models.Medications,
        prefix='/medications',
        tags=['Medications']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Prescriptions,
        pydantic_model=pydantic_models.Prescriptions,
        prefix='/prescriptions',
        tags=['Prescriptions']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Invoices,
        pydantic_model=pydantic_models.Invoices,
        prefix='/invoices',
        tags=['Invoices']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Reviews,
        pydantic_model=pydantic_models.Reviews,
        prefix='/reviews',
        tags=['Reviews']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.MedicationAssignments,
        pydantic_model=pydantic_models.MedicationAssignments,
        prefix='/medication_assignments',
        tags=['MedicationAssignments']
    ).fastapi_router,
)