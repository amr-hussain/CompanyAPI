from app.models import Company
from app import db
from app.schemas.company_schemas import CompanySchema
from sqlalchemy.exc import IntegrityError
from marshmallow.exceptions import ValidationError
from flask import abort

class CompanyServices:
    @staticmethod
    def create_company(data):
        try:
            old_company = Company.query.get(data.get('id'))
            if old_company:
                abort(400, 'Company already exists')
            company_schema = CompanySchema()
            company = company_schema.load(data, session=db.session)  
            db.session.add(company)
            db.session.commit()
        except ValidationError as e:
            db.session.rollback()
            abort(400, f'Validation error: {str(e)}')
        return company_schema.dump(company)

    @staticmethod
    def get_company(company_id):
        # Get company by ID
        company = Company.query.get(company_id)
        if not company:
            abort(404, "Company not found")
        company_schema = CompanySchema()
        return company_schema.dump(company)

    @staticmethod
    def update_company(company_id, data):
        old_company = Company.query.get(company_id)
        if not old_company:
            return abort(404, "Company not found")
        try:
            company_schema = CompanySchema()
            company = company_schema.load(data, session=db.session, instance=old_company, partial=True)  
            db.session.add(company)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            abort(400, 'Email Already Taken')
        return company_schema.dump(company)

    @staticmethod
    def delete_company(company_id):
        # Delete a company by ID
        company = Company.query.get(company_id)
        if not company:
            return abort(404, "Company not found")
        db.session.delete(company)
        db.session.commit()
        return {"message": "Company deleted successfully"}

    @staticmethod
    def get_all_companies():
        companies = Company.query.all()  
        company_schema = CompanySchema(many=True)  
        return company_schema.dump(companies) 