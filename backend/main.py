from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import and_
from backend.location_map import location_map
from backend.security import create_access_token
from backend.branch_map import branch_map
from backend.email_utils import (
    send_email,
    SUPPORT_EMAIL
)
from pydantic import BaseModel
import random
from datetime import timedelta
from fastapi import Header
from fastapi import HTTPException
from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import Header, Depends
from backend.security import decode_token
from backend.auth import (
    hash_password,
    verify_password
)
from datetime import datetime


from backend.database import get_db, engine, Base

from backend.models import (
    CollegeCutoff,
    CollegeLocation,
    User,
    SearchHistory,
    FavoriteCollege,
    PasswordOTP
)
security = HTTPBearer()

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="DSE College Predictor API",
    description="Backend API for College Predictor built using FastAPI and MySQL.",
    version="1.0.0",
    contact={
        "name": "Achyut Chaudhari",
        "email": "achyutchaudhari78@gmail.com"
    }
)

class SignupRequest(BaseModel):
    name: str
    email: str
    password: str

class LoginRequest(BaseModel):
    email: str
    password: str

class RoleUpdate(BaseModel):
    role: str

class ForgotPasswordRequest(BaseModel):
    email: str

class VerifyOTPRequest(BaseModel):
    email: str
    otp: str

class ResetPasswordRequest(BaseModel):
    email: str
    otp: str
    new_password: str

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):

    token = credentials.credentials

    payload = decode_token(token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

    user = (
        db.query(User)
        .filter(User.id == payload["user_id"])
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user


@app.get(
    "/",
    tags=["General"]
)
def home():
    return {
        "message": "College Predictor API Running"
    }




@app.get(
    "/branches",
    tags=["College Predictor"]
)
def get_branches(
    search: str,
    db: Session = Depends(get_db)
):

    branches = db.query(
        CollegeCutoff.branch
    ).distinct().all()

    branch_list = []

    for branch in branches:

        if search.lower() in branch[0].lower():
            branch_list.append(branch[0])

    return branch_list[:10]

@app.get(
    "/categories",
    tags=["College Predictor"]
)
def get_categories(search: str = ""):

    categories = [
        "OPEN",
        "OBC",
        "SC",
        "ST",
        "EWS",
        "NT-A",
        "NT-B",
        "NT-C",
        "NT-D",
        "SBC"
    ]

    result = []

    for category in categories:

        if search.lower() in category.lower():
            result.append(category)

    return result

@app.get(
    "/search-colleges",
    tags=["College Predictor"]
)
def search_colleges(
    search: str,
    db: Session = Depends(get_db)
):

    search = search.lower().strip()

    if search in college_aliases:
        return [{
            "college_name": college_aliases[search]
    }]

    colleges = (
        db.query(
            CollegeLocation.college_name,
            CollegeLocation.location
        )
        .distinct()
        .all()
    )

    result = []

    for college_name, location in colleges:

        if search in college_name.lower():

            result.append({
                "college_name": college_name,
                "location": location
        })
    return result[:20]



@app.get(
    "/college-details",
    tags=["College Predictor"]
)
def college_details(
    college_name: str,
    db: Session = Depends(get_db)
):
    college_name = college_aliases.get(
        college_name.lower(),
        college_name
)

    records = (
        db.query(
            CollegeCutoff,
            CollegeLocation
        )
        .join(
            CollegeLocation,
            CollegeCutoff.college_name == CollegeLocation.college_name
        )
        .filter(
            CollegeCutoff.college_name.ilike(f"%{college_name}%")
)
        .all()
    )

    if not records:
        return {
            "message": "College not found"
        }

    result = {
        "college_name": college_name,
        "location": records[0][1].location,
        "branches": []
    }

    for cutoff, loc in records:

        result["branches"].append({
            "branch": cutoff.branch,
            "category": cutoff.category,
            "cap1_cutoff": cutoff.cap1_cutoff
        })

    return result

@app.get(
    "/compare-colleges",
    tags=["College Predictor"]
)
def compare_colleges():

    return {
        "status": "under_development",
        "title": "College Comparison",
        "features_planned": [
            "Branch-wise cutoff comparison",
            "Category-wise comparison",
            "Location comparison",
            "Admission trend analysis",
            "Seat matrix comparison"
        ]
    }

branch_aliases = {

    # Computer

    "computer": "Computer",
    "comp": "Computer",
    "ce": "Computer",
    "cse": "Computer",
    "computer engineering": "Computer",
    "computer science": "Computer",
    "computer science engineering": "Computer",

    # AI / DS

    "ai": "AI & DS",
    "aiml": "AI & DS",
    "aids": "AI & DS",
    "ai ds": "AI & DS",
    "artificial intelligence": "AI & DS",
    "artificial intelligence and machine learning": "AI & DS",
    "artificial intelligence and data science": "AI & DS",
    "data science": "AI & DS",
    "ds": "AI & DS",

    # Cyber Security

    "cyber": "Cyber Security",
    "cyber security": "Cyber Security",
    "cyber": "Cyber Security",

    # IoT

    "iot": "IoT",
    "internet of things": "IoT",

    # IT

    "it": "Information Technology",
    "information technology": "Information Technology",

    # Electronics

    "electronics": "Electronics",
    "entc": "Electronics",
    "etc": "Electronics",
    "ece": "Electronics",
    "electronics engineering": "Electronics",
    "electronics and telecommunication": "Electronics",
    "electronics and communication": "Electronics",

    # Electronics & Computer

    "ecs": "Electronics & Computer",
    "electronics computer": "Electronics & Computer",
    "electronics and computer": "Electronics & Computer",

    # Electrical

    "electrical": "Electrical",
    "ee": "Electrical",
    "electrical engineering": "Electrical",

    # Instrumentation

    "instrumentation": "Instrumentation",
    "instrumentation engineering": "Instrumentation",
    "ic": "Instrumentation",

    # Mechanical

    "mechanical": "Mechanical",
    "mech": "Mechanical",
    "mechanical engineering": "Mechanical",
    "automobile": "Mechanical",
    "mechatronics": "Mechanical",

    # Robotics

    "robotics": "Robotics",
    "robotics engineering": "Robotics",
    "automation": "Robotics",

    # Civil

    "civil": "Civil",
    "civil engineering": "Civil",
    "structure": "Civil",
    "structural": "Civil",

    # Chemical

    "chemical": "Chemical",
    "chemical engineering": "Chemical",
    "petrochemical": "Chemical",

    # Production

    "production": "Production",
    "production engineering": "Production",
    "manufacturing": "Production",

    # Textile

    "textile": "Textile",
    "textile engineering": "Textile",
    "textile technology": "Textile",

    # Biotechnology

    "biotechnology": "Biotechnology",
    "biotech": "Biotechnology",
    "biomedical": "Biotechnology",

    # Food Technology

    "food": "Food Technology",
    "food technology": "Food Technology",

    # Plastic & Polymer

    "plastic": "Plastic & Polymer",
    "polymer": "Plastic & Polymer",

    # Chemical Technology

    "chemical technology": "Chemical Technology",
    "oil technology": "Chemical Technology",
    "paints": "Chemical Technology",

    # Mining

    "mining": "Mining",

    # Architecture

    "architecture": "Architecture",
    "architectural": "Architecture",

    # Aeronautical

    "aeronautical": "Aeronautical",
    "aero": "Aeronautical",

    # Safety

    "safety": "Safety & Fire",
    "fire": "Safety & Fire",
    "safety and fire": "Safety & Fire"
}
college_aliases = {
    "pict": "Pune Institute of Computer Technology",
    "coep": "COEP Technological University",
    "vjti": "Veermata Jijabai Technological Institute",
    "vit": "Vishwakarma Institute of Technology",
    "pccoe": "Pimpri Chinchwad College of Engineering",
    "mit aoe": "MIT Academy of Engineering",
    "mcoe": "Modern College of Engineering"
}

@app.get(
    "/colleges",
    tags=["College Predictor"]
)
def get_colleges(
    percentage: float,
    category: str,
    gender: str,
    branch: str,
    location: str = "",
    use_location: bool = True,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    history = SearchHistory(
        user_id=current_user.id,
        percentage=percentage,
        category=category,
        gender=gender,
        branch=branch,
        location=location,
        searched_at=datetime.utcnow()
    )

    db.add(history)
    db.commit()

    category = category.upper()
    gender = gender.upper()
    user_branch = branch.lower().strip()

    branch = branch_aliases.get(
        user_branch,
        branch
    )

    if gender == "MALE":

        category_map = {
            "OPEN": ["GOPEN"],
            "OBC": ["GOBC"],
            "SC": ["GSC"],
            "ST": ["GST"],
            "EWS": ["EWS"],
            "NT-A": ["GNTA"],
            "NT-B": ["GNTB"],
            "NT-C": ["GNTC"],
            "NT-D": ["GNTD"],
            "SBC": ["GSBC"]
        }

    else:

        category_map = {
            "OPEN": ["LOPEN"],
            "OBC": ["LOBC"],
            "SC": ["LSC"],
            "ST": ["LST"],
            "EWS": ["EWS"],
            "NT-A": ["LNTA"],
            "NT-B": ["LNTB"],
            "NT-C": ["LNTC"],
            "NT-D": ["LNTD"],
            "SBC": ["LSBC"]
        }

    db_categories = category_map.get(category, [])

    query = (
        db.query(
            CollegeCutoff,
            CollegeLocation
        )
        .join(
            CollegeLocation,
            CollegeCutoff.college_name == CollegeLocation.college_name
        )
        .filter(
            CollegeCutoff.category.in_(db_categories)
        )
    )

    selected_branches = branch_map.get(
        branch,
        [branch]
    )

    query = query.filter(
        CollegeCutoff.branch.in_(selected_branches)
    )

    if use_location:

        selected_locations = location_map.get(
            location,
            [location]
        )

        query = query.filter(
            CollegeLocation.location.in_(selected_locations)
        )

    colleges = query.all()

    colleges = sorted(
        colleges,
        key=lambda x: x[0].cap1_cutoff,
        reverse=True
    )

    dream = []
    target = []
    safe = []

    for cutoff, loc in colleges:

        college_data = {
            "college_name": cutoff.college_name,
            "branch": cutoff.branch,
            "category": cutoff.category,
            "cap1_cutoff": cutoff.cap1_cutoff,
            "location": loc.location
        }

        diff = cutoff.cap1_cutoff - percentage

        if diff > 3:
            dream.append(college_data)

        elif diff >= -2:
            target.append(college_data)

        else:
            safe.append(college_data)

    return {
        "dream": dream[:10],
        "target": target[:10],
        "safe": safe[:10]
    }

@app.post(
    "/signup",
    tags=["Authentication"]
)
def signup(
    user: SignupRequest,
    db: Session = Depends(get_db)
):

    existing_user = (
        db.query(User)
        .filter(User.email == user.email)
        .first()
    )

    if existing_user:
        return {
            "success": False,
            "message": "Email already registered"
        }

    import re

    if len(user.password) < 8:
        return {
            "success": False,
            "message": "Password must be at least 8 characters"
        }

    if not re.search(r"[A-Z]", user.password):
        return {
            "success": False,
            "message": "Password must contain at least one uppercase letter"
        }

    if not re.search(r"[0-9]", user.password):
        return {
            "success": False,
            "message": "Password must contain at least one number"
        }

    new_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password),
        role="user",
        created_at=datetime.utcnow()
    )

    db.add(new_user)
    db.commit()

    body = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f4f6f9;
            margin: 0;
            padding: 30px;
        }}

        .container {{
            max-width: 650px;
            margin: auto;
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }}

        .header {{
            background: #2563eb;
            color: white;
            text-align: center;
            padding: 25px;
        }}

        .content {{
            padding: 30px;
            color: #333;
            line-height: 1.7;
        }}

        .features {{
            background: #f8fafc;
            border-radius: 8px;
            padding: 15px;
            margin: 20px 0;
        }}

        .footer {{
            text-align: center;
            padding: 20px;
            font-size: 14px;
            color: #777;
            background: #f1f5f9;
        }}

        .highlight {{
            color: #2563eb;
            font-weight: bold;
        }}
    </style>
</head>

<body>

<div class="container">

<div class="header">
<h1>🎓 College Predictor</h1>
<p>Welcome to the Community!</p>
</div>

<div class="content">

<h2>Hello {new_user.name}, 👋</h2>

<p>
Your account has been created successfully.
Thank you for joining <span class="highlight">College Predictor</span>.
</p>

<p>
This platform helps Diploma students find the best engineering colleges based on:
</p>

<div class="features">

✅ Diploma Percentage<br>
✅ Category<br>
✅ Preferred Branch<br>
✅ Preferred Location<br>
✅ Dream / Target / Safe Analysis

</div>

<h3>Why was this platform created?</h3>

<p>
As a <b>Direct Second Year (DSE)</b> engineering student at
<b>VJTI, Mumbai</b>, I experienced how competitive DSE admissions are.
With very limited seats available, securing the right college in the
<b>first CAP round</b> can make a huge difference.
</p>

<p>
That experience inspired me to build this platform so students can make
better admission decisions using accurate college predictions instead of
guesswork.
</p>

<h3>Your account allows you to:</h3>

<ul>
<li>Predict Dream, Target & Safe Colleges</li>
<li>Save Favourite Colleges</li>
<li>Access Search History</li>
<li>Receive Personalized Recommendations</li>
</ul>

<p>
I hope this platform helps you secure the best college for your future.
</p>

<p>
Thank you for trusting College Predictor.
</p>

<hr style="border:none;border-top:1px solid #d1d5db;margin:30px 0;">

<h3 style="color:#2563eb;margin-bottom:10px;">
Need Help?
</h3>

<p style="font-size:15px;color:#555;line-height:1.6;">

If you have any questions, suggestions, or encounter any issues while using College Predictor, feel free to contact us.

<br><br>

📧 <b>Email:</b>
<a href="mailto:{SUPPORT_EMAIL}" style="color:#2563eb;text-decoration:none;">
{SUPPORT_EMAIL}
</a>

</p>

<hr style="border:none;border-top:1px solid #d1d5db;margin:30px 0;">

<p style="text-align:center;font-size:14px;color:#777;">

<b>Best Wishes,</b><br><br>

Achyut Chaudhari<br>
Direct Second Year (DSE)<br>
VJTI, Mumbai<br><br>

<b>College Predictor Team</b><br><br>

© 2026 College Predictor<br>
Helping Diploma Students Make Better Admission Decisions

</p>

</div>

</body>
</html>
"""
    try:
        send_email(
            receiver_email=new_user.email,
            subject="Welcome to College Predictor 🎉",
            body=body
    )
    except Exception as e:
        print(f"Welcome Email Error: {e}")

    return {
        "success": True,
        "message": "Account created successfully"
}

@app.post(
    "/login",
    tags=["Authentication"]
)
def login(
    user: LoginRequest,
    db: Session = Depends(get_db)
):

    db_user = (
        db.query(User)
        .filter(User.email == user.email)
        .first()
    )

    if not db_user:
        return {
            "success": False,
            "message": "Invalid email or password"
        }
    if db_user.is_active == "false":

        return {
            "success": False,
            "message": "Account disabled"
    }
    
     
    if not verify_password(
        user.password,
        db_user.password
    ):
        return {
            "success": False,
            "message": "Invalid email or password"
        }

    db_user.last_login = datetime.utcnow()

    db.commit()

    token = create_access_token(
        {
            "user_id": db_user.id,
            "email": db_user.email,
            "role": db_user.role
        }
    )

    return {
        "success": True,
        "message": "Login successful",
        "token": token,
        "user": {
            "id": db_user.id,
            "name": db_user.name,
            "email": db_user.email,
            "role": db_user.role
        }
    }

def admin_required(
    current_user = Depends(get_current_user)
):

    if not current_user:
        raise HTTPException(
            status_code=401,
            detail="Not authenticated"
        )

    if current_user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin access required"
        )

    return current_user
    

@app.get(
    "/users",
    tags=["Admin"]
)
def get_users(
    admin = Depends(admin_required),
    db: Session = Depends(get_db)
    
):
    

    users = db.query(User).all()

    result = []

    for user in users:

        result.append({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role,
            "created_at": user.created_at,
            "last_login": getattr(user, "last_login", None)
        })

    return result

@app.get(
    "/stats",
    tags=["Admin"]
)
def get_stats(
    admin = Depends(admin_required),
    db: Session = Depends(get_db)
):

    total_users = db.query(User).count()

    total_admins = (
        db.query(User)
        .filter(User.role == "admin")
        .count()
    )

    total_students = (
        db.query(User)
        .filter(User.role == "user")
        .count()
    )

    return {
        "total_users": total_users,
        "total_admins": total_admins,
        "total_students": total_students
    }

@app.get(
    "/recent-users",
    tags=["Admin"]
)
def recent_users(
    admin = Depends(admin_required),
    db: Session = Depends(get_db)
):

    users = (
        db.query(User)
        .order_by(User.created_at.desc())
        .limit(10)
        .all()
    )

    result = []

    for user in users:

        result.append({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role,
            "created_at": user.created_at
        })

    return result

@app.get(
    "/recent-logins",
    tags=["Admin"]
)
def recent_logins(
    admin = Depends(admin_required),
    db: Session = Depends(get_db)
):

    users = (
        db.query(User)
        .filter(User.last_login != None)
        .order_by(User.last_login.desc())
        .limit(10)
        .all()
    )

    result = []

    for user in users:

        result.append({
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role,
            "last_login": user.last_login
        })

    return result

@app.get(
    "/me",
    tags=["Authentication"]
)
def me(
    current_user = Depends(get_current_user)
):
    return current_user

@app.get(
    "/my-history",
    tags=["Search History"]
)
def my_history(
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    history = (
        db.query(SearchHistory)
        .filter(
            SearchHistory.user_id ==
            current_user.id
        )
        .order_by(
            SearchHistory.searched_at.desc()
        )
        .all()
    )

    result = []

    for item in history:

        result.append({
            "id": item.id,
            "percentage": item.percentage,
            "category": item.category,
            "gender": item.gender,
            "branch": item.branch,
            "location": item.location,
            "searched_at": item.searched_at
        })

    return result

@app.post(
    "/save-college",
    tags=["Favorites"]
)
def save_college(
    college_name: str,
    branch: str,
    category: str,
    cutoff: float,
    location: str,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    favorite = FavoriteCollege(
        user_id=current_user.id,
        college_name=college_name,
        branch=branch,
        category=category,
        cutoff=cutoff,
        location=location,
        saved_at=datetime.utcnow()
    )

    db.add(favorite)
    db.commit()

    return {
        "success": True,
        "message": "College saved successfully"
    }

@app.get(
    "/my-favorites",
    tags=["Favorites"]
)
def my_favorites(
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    favorites = (
        db.query(FavoriteCollege)
        .filter(
            FavoriteCollege.user_id ==
            current_user.id
        )
        .order_by(
            FavoriteCollege.saved_at.desc()
        )
        .all()
    )

    result = []

    for item in favorites:

        result.append({
            "id": item.id,
            "college_name": item.college_name,
            "branch": item.branch,
            "category": item.category,
            "cutoff": item.cutoff,
            "location": item.location,
            "saved_at": item.saved_at
        })

    return result

@app.delete(
    "/remove-favorite/{favorite_id}",
    tags=["Favorites"]
)
def remove_favorite(
    favorite_id: int,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    favorite = (
        db.query(FavoriteCollege)
        .filter(
            FavoriteCollege.id == favorite_id,
            FavoriteCollege.user_id ==
            current_user.id
        )
        .first()
    )

    if not favorite:
        return {
            "success": False,
            "message": "Favorite not found"
        }

    db.delete(favorite)
    db.commit()

    return {
        "success": True,
        "message": "Favorite removed"
    }

@app.delete(
    "/admin/user/{user_id}",
    tags=["Admin"]
)
def delete_user(
    user_id: int,
    admin = Depends(admin_required),
    db: Session = Depends(get_db)
):

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:
        return {
            "success": False,
            "message": "User not found"
        }

    if user.role == "admin":
        return {
            "success": False,
            "message": "Admins cannot be deleted"
        }

    db.delete(user)
    db.commit()

    return {
        "success": True,
        "message": "User deleted successfully"
    }

@app.put(
    "/admin/disable-user/{user_id}",
    tags=["Admin"]
)
def disable_user(
    user_id: int,
    admin = Depends(admin_required),
    db: Session = Depends(get_db)
):

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    # ADD THIS HERE
    if user.role == "admin":
        raise HTTPException(
            status_code=400,
            detail="Admin account cannot be disabled"
        )

    user.is_active = "false"

    db.commit()

    return {
        "success": True,
        "message": f"{user.name} disabled successfully"
    }

@app.put(
    "/admin/enable-user/{user_id}",
    tags=["Admin"]
)
def enable_user(
    user_id: int,
    admin = Depends(admin_required),
    db: Session = Depends(get_db)
):

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    user.is_active = "true"

    db.commit()

    return {
        "success": True,
        "message": f"{user.name} enabled successfully"
    }

@app.put(
    "/admin/change-role/{user_id}",
    tags=["Admin"]
)
def change_role(
    user_id: int,
    role_data: RoleUpdate,
    admin = Depends(admin_required),
    db: Session = Depends(get_db)
):

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if role_data.role not in ["admin", "user"]:
        raise HTTPException(
            status_code=400,
            detail="Role must be admin or user"
        )

    user.role = role_data.role

    db.commit()

    return {
        "success": True,
        "message": f"{user.name} role changed to {role_data.role}"
    }

@app.post(
    "/forgot-password",
    tags=["Authentication"]
)
def forgot_password(
    request: ForgotPasswordRequest,
    db: Session = Depends(get_db)
):

    user = (
        db.query(User)
        .filter(User.email == request.email)
        .first()
    )

    if not user:
        return {
            "success": False,
            "message": "Email not registered"
        }

    otp = str(random.randint(100000, 999999))

    expires = datetime.utcnow() + timedelta(minutes=10)

    db.query(PasswordOTP).filter(
        PasswordOTP.email == request.email
    ).delete()

    otp_record = PasswordOTP(
        email=request.email,
        otp=otp,
        expires_at=expires
    )

    db.add(otp_record)
    db.commit()

    body = f"""
Hi,

We received a request to reset your College Predictor account password.

Your One-Time Password (OTP) is: {otp}

This OTP is valid for 10 minutes.

If you did not request a password reset, please ignore this email.

Regards,

College Predictor Team
"""

    try:
        send_email(
            receiver_email=request.email,
            subject="College Predictor Password Reset OTP",
            body=body
    )

        return {
            "success": True,
            "message": "OTP sent to your registered email."
    }

    except Exception as e:
        print(f"Password Reset Email Error: {e}")

        return {
            "success": False,
            "message": "Unable to send OTP email. Please try again later."
    }

@app.post(
    "/verify-otp",
    tags=["Authentication"]
)
def verify_otp(
    request: VerifyOTPRequest,
    db: Session = Depends(get_db)
):

    otp_record = (
        db.query(PasswordOTP)
        .filter(
            PasswordOTP.email == request.email
        )
        .first()
    )

    if not otp_record:
        return {
            "success": False,
            "message": "OTP not found"
        }

    if otp_record.otp != request.otp:
        return {
            "success": False,
            "message": "Invalid OTP"
        }

    if datetime.utcnow() > otp_record.expires_at:
        return {
            "success": False,
            "message": "OTP has expired"
        }

    return {
        "success": True,
        "message": "OTP verified successfully"
    }

@app.post(
    "/reset-password",
    tags=["Authentication"]
)
def reset_password(
    request: ResetPasswordRequest,
    db: Session = Depends(get_db)
):

    otp_record = (
        db.query(PasswordOTP)
        .filter(
            PasswordOTP.email == request.email
        )
        .first()
    )

    if not otp_record:
        return {
            "success": False,
            "message": "OTP not found"
        }

    if otp_record.otp != request.otp:
        return {
            "success": False,
            "message": "Invalid OTP"
        }

    if datetime.utcnow() > otp_record.expires_at:
        return {
            "success": False,
            "message": "OTP has expired"
        }

    user = (
        db.query(User)
        .filter(User.email == request.email)
        .first()
    )

    if not user:
        return {
            "success": False,
            "message": "User not found"
        }

    user.password = hash_password(request.new_password)

    db.delete(otp_record)

    db.commit()

    return {
        "success": True,
        "message": "Password reset successfully"
    }
