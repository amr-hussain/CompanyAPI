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
    
    if User.query.filter_by(username = data['username']).first():
        return jsonify({
            "message": "User Already Exists!"
        })
    
    new_user = User(username = data['username'])
    new_user.set_password(data['password'])
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({
        "message": "User Created Successfully!"
    }), 201
    
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username = data['username']).first()
    
    if user and user.check_password(data['password']):
        token = create_access_token(identity=str(user.id))
        return jsonify({
            "message": "Login Successful!",
            "access_token": token
        }), 200
        
    return jsonify({
        "message": "Invalid Credentials!"
    }), 401


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
def delete_company(id):
    try:
        message = CompanyServices.delete_company(id)
    except Exception as e:
        return jsonify({"error": str(e)}), 404
    return jsonify(message), 200

