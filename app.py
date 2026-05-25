from flask import Flask, flash, redirect, render_template, request, url_for
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from config import Config
from models.student import Student, db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "POST":
            form_data = get_student_form_data()

            errors = validate_student(form_data)
            if errors:
                for error in errors:
                    flash(error, "danger")
                return render_template("index.html", form=form_data, mode="create")

            student = Student(**form_data)

            try:
                db.session.add(student)
                db.session.commit()
                flash("Student registered successfully.", "success")
                return redirect(url_for("students"))
            except IntegrityError:
                db.session.rollback()
                flash("A student with this email is already registered.", "danger")
            except SQLAlchemyError:
                db.session.rollback()
                flash("Registration failed. Please check the database connection.", "danger")

            return render_template("index.html", form=form_data, mode="create")

        return render_template("index.html", form={}, mode="create")

    @app.route("/students")
    def students():
        registered_students = Student.query.order_by(Student.created_at.desc()).all()
        return render_template("students.html", students=registered_students)

    @app.route("/students/<int:student_id>/edit", methods=["GET", "POST"])
    def edit_student(student_id):
        student = Student.query.get_or_404(student_id)

        if request.method == "POST":
            form_data = get_student_form_data()
            errors = validate_student(form_data, student_id=student.id)

            if errors:
                for error in errors:
                    flash(error, "danger")
                return render_template("index.html", form=form_data, mode="edit", student=student)

            try:
                student.name = form_data["name"]
                student.email = form_data["email"]
                student.phone = form_data["phone"]
                student.course = form_data["course"]
                student.address = form_data["address"]
                db.session.commit()
                flash("Student details updated successfully.", "success")
                return redirect(url_for("students"))
            except IntegrityError:
                db.session.rollback()
                flash("This email is already registered. Use a different email address.", "danger")
            except SQLAlchemyError:
                db.session.rollback()
                flash("Update failed. Please check the database connection.", "danger")

            return render_template("index.html", form=form_data, mode="edit", student=student)

        return render_template("index.html", form=student_to_form(student), mode="edit", student=student)

    @app.route("/students/<int:student_id>/delete", methods=["POST"])
    def delete_student(student_id):
        student = Student.query.get_or_404(student_id)

        try:
            db.session.delete(student)
            db.session.commit()
            flash(f"{student.name} was deleted successfully.", "success")
        except SQLAlchemyError:
            db.session.rollback()
            flash("Delete failed. Please check the database connection.", "danger")

        return redirect(url_for("students"))

    return app


def get_student_form_data():
    """Collect and normalize submitted form data."""
    return {
        "name": request.form.get("name", "").strip(),
        "email": request.form.get("email", "").strip().lower(),
        "phone": request.form.get("phone", "").strip(),
        "course": request.form.get("course", "").strip(),
        "address": request.form.get("address", "").strip(),
    }


def student_to_form(student):
    """Convert a model instance into template-friendly form data."""
    return {
        "name": student.name,
        "email": student.email,
        "phone": student.phone,
        "course": student.course,
        "address": student.address,
    }


def validate_student(data, student_id=None):
    """Validate form input before saving to the database."""
    errors = []

    if len(data["name"]) < 2:
        errors.append("Name must be at least 2 characters long.")

    if "@" not in data["email"] or "." not in data["email"]:
        errors.append("Enter a valid email address.")

    digits = "".join(character for character in data["phone"] if character.isdigit())
    if len(digits) < 10 or len(digits) > 15:
        errors.append("Phone number must contain 10 to 15 digits.")

    if not data["course"]:
        errors.append("Course is required.")

    if len(data["address"]) < 5:
        errors.append("Address must be at least 5 characters long.")

    existing_student = Student.query.filter_by(email=data["email"]).first()
    if existing_student and existing_student.id != student_id:
        errors.append("This email is already registered. Use a different email address.")

    return errors


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
