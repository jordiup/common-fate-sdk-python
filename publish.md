
# Publishing to PyPi

Firstly you will need to create an account on PyPi

https://pypi.org/account/register/

Once you have an account, you will need to create an API token

https://pypi.org/manage/account/

Once you have the API token, you will need to add it to Github Actions as a secret named `PYPI_API_TOKEN`

# Creating a release

Two actions are necessary
- Increment version in setup.py
- Create a tag/release

The GH Action is configured to run on a release, so you will need to create a tag, then create a release with the corresponding tag 

# Future improvements

- Ensure there are less manual steps to publishing


---

# Intializing auto-releaser

Our auto-releaser relies on ./github/workflows/cron-release-trigger.yml

This workflow is triggered by a cron job, and will create a release if the upstream /common-fate repo has a new release tag

In order for this to work we must give it a repo-scoped token

To create a repo-scoped token:

- Go to 
- Click on `Settings` in the left hand menu
- Click on `Developer settings` in the left hand menu
- Click on `Personal access tokens` in the left hand menu
- Click on `Generate new token`
- Give it the following permissions:
  - repo
  - workflow
- Give it a name i.e. `PAT: cron-release-trigger for CF Python SDK`

Now add this into the `common-fate-sdk-python` repo secrets as `REPO_SCOPED_TOKEN`

