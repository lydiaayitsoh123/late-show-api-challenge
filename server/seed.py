import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from server.app import create_app, db
from server.models.guest import Guest
from server.models.episode import Episode
from datetime import date

app = create_app()
app.app_context().push()

def seed():
    
    db.drop_all()
    db.create_all()

    
    guest1 = Guest(name="Byron Keith", occupation="Comedian")
    guest2 = Guest(name="Tiffiny Waithera", occupation="Musician")

    
    episode1 = Episode(date=date(2025, 6, 1), number=1)
    episode2 = Episode(date=date(2025, 6, 8), number=2)

    db.session.add_all([guest1, guest2, episode1, episode2])
    db.session.commit()

if __name__ == "__main__":
    seed()
   