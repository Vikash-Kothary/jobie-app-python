#!/usr/bin/env python3
"""
models.py - Package level variables
"""

import os
import json
from app import db
import hashlib


def get_mock_data():
    basedir = os.path.abspath(os.path.dirname(__file__))
    mock_data_path = os.path.join(basedir, 'static/example.json')
    with open(mock_data_path, encoding='utf-8') as read_file:
        mock_data = json.loads(read_file.read())
    return mock_data


class Profiles(db.Model):
    __tablename_ = 'profile_table'

    MALE = 'male'
    FEMALE = 'female'

    profile_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    schools = db.Column(db.String)
    distance = db.Column(db.Integer)
    bio = db.Column(db.String)
    gender = db.Column(db.Enum(MALE, FEMALE, name='gender'))
    sentiment = db.Column(db.Float)
    keywords = db.Column(db.String)
    image_id = db.Column(db.Integer, db.ForeignKey('images_table.image_id'))

    def __init__(self, json):
        profile_id = kwargs.get('profile_id')
        name = kwargs.get('name')
        age = kwargs.get('age')
        schools = kwargs.get('schools')
        distance = kwargs.get('distance')
        bio = kwargs.get('bio')
        gender = kwargs.get('gender')
        sentiment = kwargs.get('sentiment')
        keywords = kwargs.get('keywords')

    def to_json():
        return {
            'profile_id': profile_id,
            'name': name,
            'age': age,
            'schools': schools,
            'distance': distance,
            'bio': bio,
            'gender': gender,
            'sentiment': sentiment,
            'keywords': keywords
        }


class Images(db.Model):
    __tablename__ = 'images_table'

    image_id = db.Column(db.Integer, primary_key=True)
    profile_id = db.relationship('profile_id', backref='image', lazy=True)
    face_box = db.Column(db.String)
    estimate_age = db.Column(db.Integer)
    emotion = db.Column(db.String)
    facial_hair = db.Column(db.String)
    accessories = db.Column(db.String)
    hair = db.Column(db.String)
    makeup = db.Column(db.String)
    smile = db.Column(db.String)
    racy = db.Column(db.Float)
    image_tags = db.Column(db.String)
    caption = db.Column(db.String)

    def __init__(self, json):
        image_url = kwargs['image_url']
        image_file = open(image_url).read()
        image_id = hashlib.md5(image_file).hexdigest()

        face_box = kwargs.get('face_box')
        estimate_age = kwargs.get('estimate_age')
        emotion = kwargs.get('emotion')
        facial_hair = kwargs.get('facial_hair')
        accessories = kwargs.get('accessories')
        hair = kwargs.get('hair')
        makeup = kwargs.get('makeup')
        smile = kwargs.get('smile')
        racy = kwargs.get('racy')
        image_tags = kwargs.get('image_tags')
        caption = kwargs.get('caption')

    def to_json():
        return {
            'profile_id': profile_id,
            'image_id': image_id,
            'face_box': face_box,
            'estimate_age': estimate_age,
            'emotion': emotion,
            'facial_hair': facial_hair,
            'accessories': accessories,
            'hair': hair,
            'makeup': makeup,
            'smile': smile,
            'racy': racy,
            'image_tags': image_tags,
            'caption': caption
        }
