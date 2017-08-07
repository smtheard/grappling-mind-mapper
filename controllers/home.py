from config import app, br, Session
from models.user import User


@app.get('/')
def root(session):
    user = None
    user_id = session.get("user_id")
    if (user_id):
        user = Session().query(User).filter(User.id == user_id).first()
    return br.render_html(
        br.BaseLayout({
            "current_user": user and user.to_dict()
        }, [br.Home({})]),
        title="Grappling Mind Mapper")
