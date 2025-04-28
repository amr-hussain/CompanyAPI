from app.models import Company, User
from app import db
from app.schemas.company_schemas import CompanySchema
from sqlalchemy.exc import IntegrityError
from marshmallow.exceptions import ValidationError
from flask import abort
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required

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
    
    @staticmethod
    def register_new_user(data):
        if not data["password"] and not data["username"]:
            abort(400, "Username and Password are required!")
                
        if User.query.filter_by(username = data['username']).first():
            abort(400, "User Already Exists!")
        new_user = User(username = data['username'])
        new_user.set_password(data['password'])
        db.session.add(new_user)
        db.session.commit()
        return {"message": "User Created Successfully!"}
    @staticmethod
    def login_user(data):
        user = User.query.filter_by(username = data['username']).first()
        if user and user.check_password(data['password']):
            token = create_access_token(identity=str(user.id))
            return {
                "message": "Login Successful!",
                "access_token": token
            }
            
        abort(401, "Invalid Credentials!")
