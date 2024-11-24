from models import db, Puppy, app, Owner, Toy

with app.app_context():
    rufus = Puppy('Rufus', 5)
    fido = Puppy('Fido', 2)
    db.session.add_all([rufus, fido])
    db.session.commit()

    # Retrieve all puppies
    all_puppies = Puppy.query.all()
    print(all_puppies)

    

    # Retrieve a puppy by primary key (id)
    puppy_one = db.session.get(Puppy, 1)
    print(puppy_one)

    owner = Owner('Jose', puppy_id=puppy_one.id)

    toy1 = Toy('Ball', puppy_id=puppy_one.id)
    toy2 = Toy('Bear', puppy_id=puppy_one.id)

    db.session.add_all([owner, toy1, toy2])
    db.session.commit()

    print(puppy_one)
    print(puppy_one.report_toys())

    # Query a puppy by name
    puppy_frankie = Puppy.query.filter_by(name='Frankie').all()
    print(puppy_frankie)

    # Update a puppy's age
    first_puppy = db.session.get(Puppy, 1)
    if first_puppy:
        first_puppy.age = 10
        db.session.commit()

    # Delete a puppy by primary key (id)
    second_puppy = db.session.get(Puppy, 2)
    if second_puppy:
        db.session.delete(second_puppy)
        db.session.commit()

    # Check all puppies after update and delete
    all_puppies = Puppy.query.all()
    print(all_puppies)
