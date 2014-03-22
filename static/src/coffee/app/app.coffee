static_file = '/static/'

angular.module 'baseApp', [
    'ngRoute',
    'ngCookies',
    'appControllers',
    'appServices',
    'alunoControllers',
    'alunoServices',
]

.config ['$interpolateProvider', ($interpolateProvider) ->
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
    return
]

# .get '/proxy-form', (req, res) ->
#     if process.env.NODE_ENV == 'production' && req.headers['x-forwarded-proto'] != 'https'
#         return res.redirect 'https://' + req.get('Host') + req.url
#     else
#         routes.admin(req, res);
#     return

.config ['$routeProvider', '$locationProvider',
    ($routeProvider, $locationProvider) ->
        verifyHttps = (HttpUrl) -> return HttpUrl

        $routeProvider
            .when '/',
                templateUrl: static_file + 'partials/inicio.html'
                resolve:
                    noHttps: verifyHttps
            .when '/sobre',
                # appControllers
                templateUrl: static_file + 'partials/sobre.html'
                controller: 'SobreCtrl'
                resolve:
                    noHttps: verifyHttps
            .when '/aulas',
                templateUrl: static_file + 'partials/aulas.html'
                resolve:
                    noHttps: verifyHttps
            .when '/user-list',
                # appControllers
                templateUrl: static_file + 'partials/users/user-list.html'
                controller: 'UserListCtrl'
                resolve:
                    users: (User) -> return User.list()
                    noHttps: verifyHttps
            .when '/user-form',
                # alunoControllers
                templateUrl: static_file + 'partials/users/user-form.html'
                controller: 'UserFormCtrl'


        # use the HTML5 History API
        $locationProvider.html5Mode(true);
        return
]


.run ['$http','$cookies', ($http, $cookies) ->
    $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken']
    return
]

.run ['$templateCache', '$http', '$location', ($templateCache, $http, $location) ->
    # $http.get('partials/inicio.html', {cache:$templateCache});
    # $http.get('partials/aulas.html', {cache:$templateCache});
    # $http.get('partials/users/user-list.html', {cache:$templateCache});
    # $http.get('js/all-controllers.min.js', {cache:$templateCache});
    return
]

# changes all absUrl when it comes from https, however itself not needs to be https
.factory 'HttpUrl', ['$rootScope', '$location', '$window', ($rootScope, $location, $window) ->
    if $location.protocol() == 'https'
        url = 'http://' + $location.host() + ':8000' + $location.path()
        $window.location.href = url
        $rootScope.$apply()
    return
]

