from app import db, Puppy, app

with app.app_context():
    db.create_all()

    sam = Puppy('Sammy', 3)
    frank = Puppy('Frankie', 4)


    db.session.add_all([sam, frank])

    db.session.commit()