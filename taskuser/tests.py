from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
import base64
import json

# Create your tests here.


def create_user(username = 'test@test.com',password = 'cft6'):
    return get_user_model().objects.create_user(
        username=username,
        password = password
    )


class AuthenticationTest(APITestCase):
    def test_user_can_sign_up(self):
        response = self.client.post(reverse('sign_up'), data={
            'username':'test@test.com',
            'password1': "cft6",
            'password2': 'cft6',

        })
        user = get_user_model().objects.last()
        self.assertEqual(status.HTTP_201_CREATED,response.status_code)
        self.assertEqual(response.data['id'],user.id)
        self.assertEqual(response.data['username'], user.username)

        def test_user_can_log_in(self):
            user = create_user()
            response = self.client.post(reverse('log_in'), data={
                'username': user.username,
                'password': 'cft6',
            })

            access = response.data['access']
            header, payload, signature = access.split('.')
            decoded_payload = base64.b64decode(f'{payload}==')
            payload_data = json.loads(decoded_payload)

            self.assertEqual(status.HTTP_200_OK, response.status_code)
            self.assertIsNotNone(response.data['refresh'])
            self.assertEqual(payload_data['id'], user.id)
            self.assertEqual(payload_data['username'], user.username)

