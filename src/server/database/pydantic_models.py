from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class BaseModelModify(BaseModel):
    id: Optional[int] = 1


class Clients(BaseModelModify):
    FirstName: str
    LastName: str
    PhoneNumber: str
    Email: str
    Address: str


class Pets(BaseModelModify):
    ClientID: int
    PetName: str
    Species: str
    Breed: str
    Age: int
    Gender: str


class Appointments(BaseModelModify):
    ClientID: int
    PetID: int
    AppointmentDate: datetime
    AppointmentReason: str
    Status: str


class Veterinarians(BaseModelModify):
    FirstName: str
    LastName: str
    PhoneNumber: str
    Email: str
    Specialization: str
    Salary: float


class Services(BaseModelModify):
    ServiceName: str
    Description: str
    Price: float


class Treatments(BaseModelModify):
    AppointmentID: int
    VeterinarianID: int
    ServiceID: int
    Diagnosis: str
    Prescription: str
    TreatmentDate: datetime


class Medications(BaseModelModify):
    MedicationName: str
    Description: str
    Price: float


class Prescriptions(BaseModelModify):
    TreatmentID: int
    MedicationID: int
    Dosage: str
    Frequency: str


class Invoices(BaseModelModify):
    AppointmentID: int
    TotalAmount: float
    IssueDate: datetime
    DueDate: datetime
    Status: str


class Reviews(BaseModelModify):
    AppointmentID: int
    Rating: int
    Comment: str


class MedicationAssignments(BaseModelModify):
    PrescriptionID: int
    MedicationID: int
    Quantity: int
