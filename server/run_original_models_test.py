#!/usr/bin/env python3

# Run the original models test manually without Flask app
from models import db, Earthquake
from sqlalchemy_serializer import SerializerMixin

def test_can_be_instantiated():
    '''can be invoked to create a Python object.'''
    quake = Earthquake()
    assert quake
    assert isinstance(quake, Earthquake)
    print("✓ test_can_be_instantiated passed")

def test_has_attributes():
    '''can be instantiated with an id, magnitude, location, year.'''
    quake = Earthquake(magnitude=9.5, location="Chile", year=1960)
    assert quake.id is None  # Not persisted in database yet
    assert quake.magnitude == 9.5
    assert quake.location == "Chile"
    assert quake.year == 1960
    print("✓ test_has_attributes passed")

def test_superclasses():
    '''inherits from db.Model and SerializerMixin'''
    quake = Earthquake()
    assert isinstance(quake, db.Model)
    assert isinstance(quake, SerializerMixin)
    print("✓ test_superclasses passed")

def test_dictionary():
    '''to_dict() result'''
    quake = Earthquake(magnitude=9.5, location="Chile", year=1960)
    assert quake.to_dict()
    print("✓ test_dictionary passed")

if __name__ == "__main__":
    print("Running original models tests...")

    test_can_be_instantiated()
    test_has_attributes()
    test_superclasses()
    test_dictionary()

    print("\nAll original models tests passed!")
