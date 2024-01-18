

## Local Deployment
1. make virtual venv   ``
2. Install required python packages
    `pip install -r requirements.txt`
3. `cd app`
4. `python manage.py runserver`
5. To run https server use `python manage.py runsslserver `

## Pycharm
1. Make sure to update your virtual env in pycharm to the one you created
2. Add `app` folder to your project root

Tasks that are performed

Your task is to implement a JSON api with the following endpoints:
    GET http://127.0.0.1:8000/api/v1/document/

This should return a list of available titles.
    GET http://127.0.0.1:8000/api/v1/document/?title=titletosearch

This should return a list of available revisions for a document.
    GET http://127.0.0.1:8000/api/v1/document/?title=titletosearch&timestamp=datetime
    This should return the document as it was at that timestamp.
    GET http://127.0.0.1:8000/api/v1/document/?title=titletosearch&latest=1
    This should return the current latest version of the document.
    POST http://127.0.0.1:8000/api/v1/document/
    This allows users to post a new revision of a document.
    It should receive JSON in the form: 
{
    "title":"creating tile",
    "content": "Here i am writing the first content"
}
if title is there other wise withut title also will work
