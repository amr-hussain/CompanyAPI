from flask import Blueprint, request, jsonify
from app.models import Company , User
from app.schemas.company_schemas import CompanySchema
from app.services.company_services import CompanyServices
from app import db
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required


# adding two blueprints for the company and auth routes 
company_bp = Blueprint('company', __name__)
auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods = ['POST'])
def register():
    data = request.get_json()
    try:
        message = CompanyServices.register_new_user(data)  
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
    return jsonify(message), 201
    
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    try:
        message = CompanyServices.login_user(data)  
    except Exception as e:
        return jsonify({"error": str(e)}), 401
    
    return jsonify(message), 201

@company_bp.route('/companies', methods=['GET'])
def get_companies():
    companies = CompanyServices.get_all_companies()  
    return jsonify(companies), 200


@company_bp.route('/companies/<int:id>', methods=['GET'])
def get_company(id):
    try:
        company = CompanyServices.get_company(id)  
    except Exception as e:
        return jsonify({"error": str(e)}), 404
    return jsonify(company), 200

@company_bp.route('/add', methods=['POST'])
@jwt_required()
def add_company():
    company = request.get_json()  # Get the JSON data from the request
    if not company:
        return jsonify({"error": "No input data provided"}), 400 
    try:
        company_json = CompanyServices.create_company(company)  
        return jsonify(company_json), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@company_bp.route('/update/<int:id>', methods=['PUT'])
@jwt_required()
def update_company(id):
    company = request.get_json()
    if not company:
        return jsonify({"error": "No input data provided"}), 400
    try:
        company_json = CompanyServices.update_company(id, company)
    except Exception as e:
        return jsonify({"error": str(e)}), 404
    return jsonify(company_json), 200

@company_bp.route('/delete/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_company(id):
    try:
        message = CompanyServices.delete_company(id)
    except Exception as e:
        return jsonify({"error": str(e)}), 404
    return jsonify(message), 200

