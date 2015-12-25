Office Basic
======================

Setup Steps
-----------


1. Environment Setup:

        * Create a virtual environment

                mkvirtualenv basic

        * Install the requirements by using command:
            * pip install -r `file_name`
                - If project is running on your local machine use `requirements/dev_local.txt`
                - If project is running on your production machine use ``requirements/production.txt`

1. Database Setup:

        * Postgres dependency: 9.4.x +

        * Setup a database server (preferably Postgres) and:
            * Create a dev_local.py from dev_local.py.template and add database settings in that file
                    DATABASES = {
                        default': {
                            'ENGINE': 'django.db.backends.postgresql_psycopg2'
                            'NAME': '<dbname>',                      # Or path to database file if using sqlite3.
                            'USER': '<username>',                      # Not used with sqlite3.
                            'PASSWORD': '<password>',                  # Not used with sqlite3.
                            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
                            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
                        }
                    }

        * FOR STAGING AND PRODUCTION ENVIRONMENTS WE WOULD NEED TO UPDATE THE DATABASE SETTINGS AS PER THE ENVIRONMENT CONFIG.

1. Run Migrations:

        python manage.py migrate

2. Load initial Data:

        python manage.py loadinitialdata

        Note:- To add a fixture to be loaded in initial data on each deployment, add the file to FIXTURES_TO_LOAD variable in settings (commons.py)

3. Setup git pre-commit hook (To be done on local machine)

       1. Create a file under .git/hooks/ with name pre-commit

                 /project/root/.git/hooks/pre-commit

       1. Add following to that file

                #!/usr/bin/env bash
                /path/to/git-pylint-commit-hook --pylint /path/to/pylint --pylintrc bluehornet/pylint.rc

            here /path/to/ is path where git-pylint-commit-hook and pylint exists.

                eg.  /home/josh/.virtualenvs/bh-dev/bin/git-pylint-commit-hook --pylint /home/josh/.virtualenvs/basic/bin/pylint --pylintrc /home/Projects/office_basic/office_basic/pylint.rc
~
       1. Update the permissions of pre-commit to 755

                chmod 755 /project/root/.git/hooks/pre-commit

4. To Runserver Locally (Not for Prod or staging):

        python manage.py runserver 8000

        The above command will run the server on port 8000


Test Cases:
-----------
    This ensure our code/functions is working as expected. Due to some changes/code update if a specific function breaks you will know about it.
    Structure:
    └── app_name
        └── tests
            ├── __init__.py
            ├── test_forms.py
            ├── test_models.py
            └── test_views.py
    We have write test cases for each and every modules eg: models, forms, views etc. Add <test_> for each module name and place them in tests as above structure.

    Test module structure:
    <imports>

    <test class 1>
          def test_fun1:
                  .
                  .
                  .
          def test_funN:

    <test class 2>
            .
            .
            .
            .
    <test class n>

    Test class name should be <views/forms/utils name>Test.
    All the methods that are to be tested in our test classes should start with  <test_>
    Each test(method) should generally only test one scenario/flow of the function.
    Add a method <setUp> in each test class which will contain all setup code for test.

    Test third party apis: Functions which contain interaction with other external resource(api etc) use mock(http://www.voidspace.org.uk/python/mock/index.html).

    Run test cases:
    --------------

            1. All test cases at once:

                       python manage.py test --settings=office_basic.settings.test_settings

            2. Individual test case:

                    python manage.py test --settings=office_basic.settings.test_settings \
                       apps.<app_name>.tests.<module_name>.<test_class>.<test_method>


                   apps.<app_name>.tests will run all test cases in this apps similarly
                   apps.<app_name>.tests.<module_name> in that module and
                   apps.<app_name>.tests.<module_name>.<test_class> in that class


Coverage:
---------

    It keeps track of which lines of application code are executed, which ones are skipped (like comments), and which ones are never reached while executing test cases.

    Run coverage:
    -------------

        1.Run coverage on whole project/code base:
            coverage run manage.py test --settings=office_basic.settings.test_settings
        2.Run coverage on a particular app:
            coverage run --source=<module_path/app>[,<module_path/app>] manage.py test    --settings=office_basic.settings.test_settings <module> [<module>]

    <module path/app>: apps.auth
    <module>: bluehornet.apps.auth

    Coverage report:
    ----------------
            coverage report -m
            option -m: Show line numbers of statements in each module that weren't executed

            OR

            coverage html
            It will generate `htmlcov` folder in project root. <project root>/htmlcov/index.html is index page for coverage listing


        The simplest reporting is textual summary:

        Name                                  Stmts   Miss Branch BrMiss  Cover   Missing
        ---------------------------------------------------------------------------------
        <module_1>                         103     53     51     33    44%   29, 47-48, 80-100, 104-111
        <module_2>                          74     23     14     10    63%   43-45, 57-72, 78-85
        ---------------------------------------------------------------------------------
        TOTAL                              177     76     65     43    51%

    Branch coverage:
         To measure branch coverage use --branch
         It will calculate no. of branches(if-else-if) have be covered by test case execution.
         http://nedbatchelder.com/code/coverage/branch.html#branch

Logging
---------

    Logging Pattern used in code

        import logging

        logger = logging.getLogger(__name__)

        To log:
        logger.<level>("message") or logger.<level>("message", extra={})

        Example:
        logger.info("Script ran successfully")
        logger.error("Could not locate file %s", filename, extra={"customer": customer})

==================================
