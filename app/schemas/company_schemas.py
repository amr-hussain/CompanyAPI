from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models import Company

class CompanySchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Company
        load_instance = True
        # include_fk = True #include foreign keys if you have relationships
