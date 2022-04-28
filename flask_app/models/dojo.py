
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['updated_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add(cls, data):
        query = "INSERT INTO dojos (name, location, language,comment) VALUES (%(name)s, %(location)s, %(language)s,%(comment)s);"
        result = connectToMySQL('dojo_survey_schema').query_db(query, data)
        return result

    @staticmethod
    def validate(dojo):
        is_valid = True
        if len(dojo['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(dojo['location']) < 5:
            flash("location must be at least 5 characters.")
            is_valid = False
        if len(dojo['language']) < 2:
            flash("language must be 2 or greater.")
            is_valid = False
        if len(dojo['comment']) < 5:
            flash("comment must be at least 5 characters.")
            is_valid = False
        return is_valid
