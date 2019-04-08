from django.test import TestCase
from account import models as amod
from datetime import datetime
from lxml import etree
from django.contrib.auth import models as pmod

# Create your tests here.
class AccountTests(TestCase):
    fixtures = ['account.yaml']

    def setUp(self):
        # I'm creating a user here (instead of using one from the fixtures)
        # because that is what Dr. Albretch did

        self.homer = amod.User()
        self.homer.username = "homer2"
        self.homer.set_password('doh!')
        self.homer.first_name = "Homer"
        self.homer.last_name = "Simpson"
        self.homer.birthdate = datetime(2000, 1, 1)
        self.homer.save()

    # Unit test to create a user, set data, save, then load again and compare.
    def test_create_user(self):
        bill = amod.User()
        bill.username = "bill"
        bill.set_password('doh!')
        bill.first_name = "Bill"
        bill.last_name = "Simpson"
        bill.birthdate = datetime(2000, 1, 1)
        bill.save()
        bill2 = amod.User.objects.get(username='bill')
        self.assertEqual(bill, bill2, msg='Bill should have been saved in the database')

    # Unit test for login and logout
    def test_user_login(self):
        credentials = {
            'username': 'homer2',
            'password': 'doh!'
        }

        response = self.client.post('/account/login/', credentials)

        # get the request object (testing framework embeds it as  aresponse.wsgi_request)
        request = response.wsgi_request
        
        # debugging the test line below
        # self.print_html(response.content)

        # if it worked, then the request.user will be the homer object and is_authenticated will be true
        self.assertTrue(request.user.is_authenticated, msg="User should have authenticated")
        self.assertEqual(request.user.id, self.homer.id, msg="User should have been Homer")

        # if it wokored, the response should be a redirect code (login.py returned HttpResponseRedirect)
        self.assertEqual(response.status_code, 302, msg="User wasn't redirected for login")

        # get request to account logout
        response = self.client.get('/account/logout')
        request = response.wsgi_request
        #assert equal is 302
        self.assertEqual(response.status_code, 302, msg="User wasn't redirected for logout")
        #assert false is authenticated
        self.assertFalse(request.user.is_authenticated, msg="User should have been logged out")


    # Unit test for group permissions    
    def test_group_permissions(self):
        #pull a user from the database
        userTest = amod.User.objects.get(username='user0')

        #create a group
        groupTest = pmod.Group()
        groupTest.name = 'Test'
        groupTest.save()
        groupTest.permissions
        groupTest.permissions.add(pmod.Permission.objects.get(codename='add_user'))
        groupTest.save()

        #add the user to the group
        userTest.groups.add(groupTest)
        userTest.save()
        userTest = amod.User.objects.get(username='user0')

        #assertion tests for the unique permission and the permission from the group
        # look for the id instead of account.newPermission   
        self.assertTrue(userTest.has_perm('account.add_user'), msg='User should have the add_user permission')

        #group has permission

    def test_user_groups(self):
        # pull a user from the database
        userTest = amod.User.objects.get(username='user3')

        #create a group
        groupTest = pmod.Group()
        groupTest.name = 'Test2'
        groupTest.save()

        #add the user to the group
        userTest.groups.add(groupTest)
        userTest.save()
        userTest = amod.User.objects.get(username='user3')

        self.assertTrue(userTest.groups.filter(name=groupTest.name).exists(), msg='User should be in the test2 group')

    # Unit test for changing a password
    def test_change_password(self):
        passwordTest = amod.User.objects.get(username='user1')
        pswd = passwordTest.password
        passwordTest.set_password('newpassword')
        passwordTest.save()

        passwordTest = amod.User.objects.get(username='user1')

        self.assertNotEqual(passwordTest.password, pswd, msg='Password should have been changed')



