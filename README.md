# flask-on-dokcer-with-gitactions

Create a CI workflow to test and push a containerized Flask ML app on docker

## Test locally

### create your model

For this run the command below from the project root
`python ./src/training/train.py`

It stores the model in a file in `models/` folder and we will use this file to deploy our model.

### run the flask app

Once you have your model test the Flask script. First launch it with the command below from the project root:
`python ./src/inference/app.py`

When the app is running you see it by checking the homepage from your browser at: 127.0.0.1:5000

Then check the prediction page using the commande below:
`python ./tests/test_app.py`

## Deploy your docker image

If you checked it locally you can now containerize your app through within a docker image.
```
# run it where you have you Dockerfile
docker build . -t my-flask-app
```

And then just run your image

```
docker run -p 5000:5000 --rm my-flask-app
```

And if you go to `http://127.0.0.1:5000` you will see your application running!

You can run the test again and see that it works fine :)

## Use the Git Actions

Now thanks to the ".github/workflows/ci.yml" you can update your image in your dockerhub by simply making a push or pull request on your master branch project. 

Create your Github Secret first so that the agent can connect to your docker account and push the image once it's build and tested.
