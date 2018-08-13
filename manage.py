from app import app, db
from app.models import Role, Admin
import sys
import os
from flask_script import Manager
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0, os.path.join(BASE_DIR, 'movie_project\\app'))
# sys.path.insert(0, os.path.join(BASE_DIR, 'movie_project\\app\\admin'))
# sys.path.insert(0, os.path.join(BASE_DIR, 'movie_project\\app\\home'))

manage = Manager(app)
# db.create_all()
#
# # 测试数据的插入
#
# role = Role(
#     name="超级管理员",
#     auths=""
# )
# db.session.add(role)
# db.session.commit()
# from werkzeug.security import generate_password_hash
#
#
# admin = Admin(
#     name="admin",
#     pwd=generate_password_hash("admin"),
#     is_super=0,
#     role_id=1
# )
# db.session.add(admin)
# db.session.commit()


if __name__ == "__main__":
    manage.run()