Title: Django, graphene, 그리고 React로 간단한 서비스 만들기
Date: 2019-04-02
Lang: ko
Slug: django-graphene-react
Status: draft


소비자의 이력서


Python 3.7.2
https://github.com/pyenv/pyenv/issues/1219#issuecomment-448658430

brew install zlib sqlite

export LDFLAGS="-L/usr/local/opt/zlib/lib -L/usr/local/opt/sqlite/lib"
export CPPFLAGS="-I/usr/local/opt/zlib/include -I/usr/local/opt/sqlite/include"

custom user model
https://docs.djangoproject.com/en/2.1/topics/auth/customizing/#changing-to-a-custom-user-model-mid-project


AUTH_USER_MODEL = 'pubsub.User'
makemigrations
migrate

객체 모델링

ImageField
makemigrations
migrate

Pillow error
pip install Pillow


pip install django-summernote
apps 추가
url 추가
media 추가
migrate

admin.site.register(Publisher, SummernoteModelAdmin)

pip install graphene-django
schema 추가

django-filter
relay

https://docs.graphene-python.org/projects/django/en/latest/authorization/
authentication
exclude
https://www.howtographql.com/graphql-python/4-authentication/

https://github.com/flavors/django-graphql-jwt

apollo playground 설치하기 http request header 지정

{
  "Authorization": "JWT <token>"
}

Procfile --pythonpath

$ heroku run python pubsubat/manage.py migrate
createsuperuser


cloudflare
heroku domains:add pubsub.at
https://support.cloudflare.com/hc/en-us/articles/200169056-Does-CloudFlare-support-CNAME-APEX-at-the-root-


react + graphql
https://github.com/mbrochh/django-graphql-apollo-react-demo
https://www.robinwieruch.de/minimal-react-webpack-babel-setup/
https://www.howtographql.com/react-apollo/1-getting-started/

npm install --save-dev apollo-boost react-apollo graphql

# client side
CORS
fetchOptions: {
  mode: 'no-cors',
},
Content-Type:text/plain;charset=UTF-8
https://github.com/apollographql/apollo-link/issues/275#issuecomment-347138651
text/html

# or on serverside
pip install django-cors-headers

Graphene Django “Must provide query string”

CORS_ORIGIN_WHITELIST = (
    'pubsub.at',
    'localhost:8000',
    'localhost:8080',
)

이걸 꼭 해야할 필요가 있을까? ... django dev server로 서빙하지 않으면 필요 없는 것 같다. nginx 로 서빙하는게 낫다.
serving webpack with django
https://owais.lone.pw/blog/webpack-plus-reactjs-and-django/
https://github.com/owais/django-webpack-loader
npm install --save-dev webpack-bundle-tracker
pip install django-webpack-loader

history on webpackdev 
historyApiFallback: true,
https://stackoverflow.com/a/39968984/366908



npm install --save-dev @babel/plugin-transform-runtime


https://github.com/owais/django-webpack-loader/issues/160

using process.env within webpack build
https://medium.com/@justintulk/passing-environment-variables-into-your-code-with-webpack-cab09d8974b0
