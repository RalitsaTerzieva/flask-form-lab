from app import db, Puppy, app

with app.app_context():
    my_puppy = Puppy('Rufus', 5)
    db.session.add(my_puppy)
    db.session.commit()

    # Retrieve all puppies
    all_puppies = Puppy.query.all()
    print(all_puppies)

    # Retrieve a puppy by primary key (id)
    puppy_one = db.session.get(Puppy, 1)
    print(puppy_one)

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
