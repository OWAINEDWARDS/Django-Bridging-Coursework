from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from CV.models import CVpost, Qualifications, Projects
from CV.views import edit_CV


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'CV/homepage.html')

    def test_editcv_url_resolves_to_editcv_view(self):
        found = resolve('/editCV/')
        self.assertEqual(found.func, edit_CV)

class ModelCVTest(TestCase):

    def test_saving_and_retrieving(self):
        cv = CVpost()

        cv.homeAddress = "100 Ways Wrong, Birmingham, Selly oak, LXXXLL"
        cv.contactNumber = "0734509876"
        cv.status = "Student @ The University Of Birmingham"
        cv.aboutMe = "Student @ The University Of Birmingham studying computer science BSc"
        cv.save()

        saved_cv = CVpost.objects.all()
        self.assertEqual(saved_cv.count(), 1)

        saved_cv_ret = saved_cv[0]
        self.assertEqual(saved_cv_ret.homeAddress, "100 Ways Wrong, Birmingham, Selly oak, LXXXLL")
        self.assertEqual(saved_cv_ret.contactNumber, "0734509876")
        self.assertEqual(saved_cv_ret.status, "Student @ The University Of Birmingham")
        self.assertEqual(saved_cv_ret.aboutMe, "Student @ The University Of Birmingham studying computer science BSc")

class QualificationModelTest(TestCase):

    def test_saving_and_retrieving(self):
        first_qualification = Qualifications()
        first_qualification.qualification = 'Computer Science BSc @ The University Of Birmingham'
        first_qualification.save()

        second_qualification = Qualifications()
        second_qualification.qualification = 'Test Degree BSc @ The University Of Degrees'
        second_qualification.save()

        saved_qualifications = Qualifications.objects.all()
        self.assertEquals(saved_qualifications.count(), 2)

        first_saved_qualification = saved_qualifications[0]
        second_saved_qualification = saved_qualifications[1]
        self.assertEqual(first_saved_qualification.qualification, 'Computer Science BSc @ The University Of Birmingham')
        self.assertEqual(second_saved_qualification.qualification, 'Test Degree BSc @ The University Of Degrees')

class ProjectsModelTest(TestCase):

    def test_saving_and_retrieving(self):
        first_project = Projects()
        first_project.projectTitle = '2nd Year Bridging Coursework'
        first_project.projectDescription = "placeholder"
        first_project.save()

        second_project = Projects()
        second_project.projectTitle = 'Sober Socials Society goes online'
        second_project.projectDescription = "placeholder2"
        second_project.save()

        saved_projects = Projects.objects.all()
        self.assertEquals(saved_projects.count(), 2)

        first_saved_project = saved_projects[0]
        second_saved_project = saved_projects[1]
        self.assertEqual(first_saved_project.projectTitle, '2nd Year Bridging Coursework')
        self.assertEqual(first_saved_project.projectDescription, "placeholder")
        self.assertEqual(second_saved_project.projectTitle, 'Sober Socials Society goes online')
        self.assertEqual(second_saved_project.projectDescription, "placeholder2")

class TestDisplayed(TestCase):

    def test_name_displayed(self):

        response = self.client.get('/')
        self.assertIn('Owain Edwards', response.content.decode())

    # def test_CV_titles_displayed(self):
    #
    #     response = self.client.get('/')
    #     self.assertIn('Current Status', response.content.decode())
    #     self.assertIn('About Me', response.content.decode())
    #     self.assertIn('Qualifications', response.content.decode())
    #     self.assertIn('Proje2ctss', response.content.decode())
