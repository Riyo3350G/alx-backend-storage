#!/usr/bin/env python3
"""list all student module"""


def top_students(mongo_collection):
    """function that returns all students sorted by average score"""
    top_students_list = mongo_collection.aggregate([
        {
            "$project": {
                    "name": "$name",
                    "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
        ])

    return top_students_list
