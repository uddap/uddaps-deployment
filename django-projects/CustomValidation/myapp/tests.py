from django.test import TestCase
from example.core.forms import AddBookForm

# Create your tests here....
class AddBookFormTests(TestCase):
    def test_title_starting_lowercase(self):
        form = AddBookForm(data={"title": "a lowercase title"})

        self.assertEqual(
            form.errors["title"], ["Should start with an uppercase letter"]
        )

    def test_title_ending_full_stop(self):
        form = AddBookForm(data={"title": "A stopped title."})

        self.assertEqual(form.errors["title"], ["Should not end with a full stop"])

    def test_title_with_ampersand(self):
        form = AddBookForm(data={"title": "Dombey & Son"})

        self.assertEqual(form.errors["title"], ["Use 'and' instead of '&'"])

# These tests correct the two flaws. They’re faster because they simply pass in and read out dictionaries, with no need to touch
# anything related to # HTTP or HTML. And they’re more precise because they directly inspect the errors for “title,” ignoring the
# other fields. Note you’d still want to have some integration tests, to check that the view, form, and template work together:

# from http import HTTPStatus
# from django.test import TestCase

class AddBookViewTests(TestCase):
    def test_get(self):
        response = self.client.get("/books/add/")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "<h1>Add Book</h1>", html=True)

    def test_post_success(self):
        response = self.client.post("/books/add/", data={"title": "Dombey and Son"})

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(response["Location"], "/books/")

    def test_post_error(self):
        response = self.client.post("/books/add/", data={"title": "Dombey & Son"})

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Use 'and' instead of '&'", html=True)