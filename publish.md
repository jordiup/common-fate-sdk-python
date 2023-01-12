
# Publishing to PyPi

Firstly you will need to create an account on PyPi

https://pypi.org/account/register/

Once you have an account, you will need to create an API token

https://pypi.org/manage/account/

Once you have the API token, you will need to add it to Github Actions as a secret

# Creating a release

Two actions are necessary
- Increment version in setup.py
- Create a tag/release

The GH Action is configured to run on a release, so you will need to create a tag, then create a release with the corresponding tag 

# Future improvements

- Ensure there are less manual steps to publishing
