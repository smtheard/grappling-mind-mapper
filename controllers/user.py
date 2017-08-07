import bottle
from sqlalchemy.orm import joinedload
from sqlalchemy import func
from config import app, br, Session

from models.show import Show
from models.user import User
from models.show_follow import ShowFollow
from models.episode import Episode

from collections import defaultdict


@app.get('/user/<slug>')
def user(session, slug):
    current_user = None
    current_user_id = session.get("user_id")
    sa_session = Session()
    if (current_user_id):
        current_user = sa_session.query(User).filter(
            User.id == current_user_id).first()

    user_being_viewed = sa_session.query(User).filter(
        func.lower(User.slug) == func.lower(slug)).first()

    if (not user_being_viewed):
        bottle.abort(404, "URL Not Found")

    return br.render_html(
        br.BaseLayout({
            "current_user": current_user and current_user.to_dict()
        }, [br.UserPage(props)]),
        title="Grappling Mind Mapper")
