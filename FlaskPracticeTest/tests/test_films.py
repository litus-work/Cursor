import json
from unittest import TestCase
from app import create_app
from db import db
from db import Films

app = create_app("TEST")


class TestFilms(TestCase):
    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

        film = Films(name="Harry Potter")
        db.session.add(film)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_films(self):
        resp = app.test_client().get('/films')
        expected_result = [{"id": 1, "name": "Harry Potter"}]
        self.assertEquals(resp.status_code, 200)
        self.assertEquals(resp.json, expected_result)

    def test_post_films(self):
        expected_result = [{"id": 1, "name": "Harry Potter"}, {"id": 2, "name": "Lords of the ring"}]
        data = json.dumps({"name": "Lords of the ring"})
        resp = app.test_client().post('/films', data=data, content_type='application/json')
        self.assertEquals(resp.status_code, 200)
        self.assertEquals(resp.json, expected_result)

    def test_update_films(self):
        expected_result = [{"id": 1, "name": "Man in black"}]
        data = json.dumps({"name": "Man in black"})
        resp = app.test_client().put('/films/1', data=data, content_type='application/json')
        self.assertEquals(resp.status_code, 200)
        self.assertEquals(resp.json, expected_result)

    def test_delete_films(self):
        expected_result = []
        resp = app.test_client().delete('/films/1')
        self.assertEquals(resp.status_code, 200)
        self.assertEquals(resp.json, expected_result)

