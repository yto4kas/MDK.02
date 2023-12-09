from peewee import Model, SqliteDatabase, CharField, IntegerField, FloatField, DateTimeField, ForeignKeyField

db = SqliteDatabase('database.db')


class BaseModel(Model):
    class Meta:
        database = db


class Clients(BaseModel):
    ClientID = IntegerField(primary_key=True)
    FirstName = CharField()
    LastName = CharField()
    PhoneNumber = CharField()
    Email = CharField()
    Address = CharField()


class Pets(BaseModel):
    PetID = IntegerField(primary_key=True)
    ClientID = ForeignKeyField(Clients, backref='pets')
    PetName = CharField()
    Species = CharField()
    Breed = CharField()
    Age = IntegerField()
    Gender = CharField()


class Appointments(BaseModel):
    AppointmentID = IntegerField(primary_key=True)
    ClientID = ForeignKeyField(Clients, backref='appointments')
    PetID = ForeignKeyField(Pets, backref='appointments')
    AppointmentDate = DateTimeField()
    AppointmentReason = CharField()
    Status = CharField()


class Veterinarians(BaseModel):
    VeterinarianID = IntegerField(primary_key=True)
    FirstName = CharField()
    LastName = CharField()
    PhoneNumber = CharField()
    Email = CharField()
    Specialization = CharField()
    Salary = FloatField()


class Services(BaseModel):
    ServiceID = IntegerField(primary_key=True)
    ServiceName = CharField()
    Description = CharField()
    Price = FloatField()


class Treatments(BaseModel):
    TreatmentID = IntegerField(primary_key=True)
    AppointmentID = ForeignKeyField(Appointments, backref='treatments')
    VeterinarianID = ForeignKeyField(Veterinarians, backref='treatments')
    ServiceID = ForeignKeyField(Services, backref='treatments')
    Diagnosis = CharField()
    Prescription = CharField()
    TreatmentDate = DateTimeField()


class Medications(BaseModel):
    MedicationID = IntegerField(primary_key=True)
    MedicationName = CharField()
    Description = CharField()
    Price = FloatField()


class Prescriptions(BaseModel):
    PrescriptionID = IntegerField(primary_key=True)
    TreatmentID = ForeignKeyField(Treatments, backref='prescriptions')
    MedicationID = ForeignKeyField(Medications, backref='prescriptions')
    Dosage = CharField()
    Frequency = CharField()


class Invoices(BaseModel):
    InvoiceID = IntegerField(primary_key=True)
    AppointmentID = ForeignKeyField(Appointments, backref='invoices')
    TotalAmount = FloatField()
    IssueDate = DateTimeField()
    DueDate = DateTimeField()
    Status = CharField()


class Reviews(BaseModel):
    ReviewID = IntegerField(primary_key=True)
    AppointmentID = ForeignKeyField(Appointments, backref='reviews')
    Rating = IntegerField()
    Comment = CharField()


class MedicationAssignments(BaseModel):
    PrescriptionID = ForeignKeyField(Prescriptions, backref='medication_assignments')
    MedicationID = ForeignKeyField(Medications, backref='medication_assignments')
    Quantity = IntegerField()


# Создание таблиц в базе данных
db.connect()
db.create_tables([Clients, Pets, Appointments, Veterinarians, Services, Treatments, Medications, Prescriptions, Invoices, Reviews, MedicationAssignments])
