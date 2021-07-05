from django.db import connection
from contextlib import closing


def get_course_by_id_video(pk):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from video where course_id = %s""", [pk])
        video = dict_fetchall(cursor)
    return video


def get_comments(pk, pks):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from comment where course_id = %s and video_id = %s """, [pk, pks])
        comment = dict_fetchall(cursor)
    return comment


def get_course_by_id(pk):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from course where id = %s""", [pk])
        comment = dict_fetchall(cursor)
    return comment


def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row))
            for row in cursor.fetchall()]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    dict(zip(columns, row))
#LIKE  ishlatilishi


#
# first_letter = input("Birinchi harfni kiriting: ")
#
# all_data = conn.execute("""
#   SELECT * FROM "employee"
#   WHERE "first_name" LIKE ?
#   """, (first_letter+"%",)).fetchall()
