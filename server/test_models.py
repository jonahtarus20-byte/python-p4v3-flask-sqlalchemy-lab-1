#!/usr/bin/env python3

# Simple test script for models without pytest
from models import db, Earthquake
from sqlalchemy_serializer import SerializerMixin

def test_can_be_instantiated():
    '''can be invoked to create a Python object.'''
    quake = Earthquake()
    assert quake
    assert isinstance(quake, Earthquake)
    print("✓ Test 1 passed: can be instantiated")

def test_has_attributes():
    '''can be instantiated with an id, magnitude, location, year.'''
    quake = Earthquake(magnitude=9.5, location="Chile", year=1960)
    assert quake.id is None  # Not persisted in database yet
    assert quake.magnitude == 9.5
    assert quake.location == "Chile"
    assert quake.year == 1960
    print("✓ Test 2 passed: has attributes")

def test_superclasses():
    '''inherits from db.Model and SerializerMixin'''
    quake = Earthquake()
    assert isinstance(quake, db.Model)
    assert isinstance(quake, SerializerMixin)
    print("✓ Test 3 passed: superclasses")

def test_dictionary():
    '''to_dict() result'''
    quake = Earthquake(magnitude=9.5, location="Chile", year=1960)
    assert quake.to_dict()
    print("✓ Test 4 passed: dictionary")

if __name__ == "__main__":
    test_can_be_instantiated()
    test_has_attributes()
    test_superclasses()
    test_dictionary()
    print("\nAll models tests passed!")
