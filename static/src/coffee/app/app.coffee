static_file = '/static/'

angular.module 'baseApp', [
    'ngRoute',
    'ngCookies',
    'appControllers',
    'appServices',
    'alunoControllers',
    'alunoServices',
]
.config ['$httpProvider', ($httpProvider) ->
    $httpProvider.defaults.xsrfCookieName = 'csrftoken'
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken'
    return
]

.config ['$interpolateProvider', ($interpolateProvider) ->
    $interpolateProvider.startSymbol('[[')
    $interpolateProvider.endSymbol(']]')
    return
]
# .config ['$httpProvider', ($httpProvider) ->
#     $httpProvider.defaults.useXDomain = true
#     delete $httpProvider.defaults.headers.common['X-Requested-With']
#     return
# ]
# .get '/proxy-form', (req, res) ->
#     if process.env.NODE_ENV == 'production' && req.headers['x-forwarded-proto'] != 'https'
#         return res.redirect 'https://' + req.get('Host') + req.url
#     else
#         routes.admin(req, res);
#     return

.config ['$routeProvider', '$locationProvider',
    ($routeProvider, $locationProvider) ->
        httpForceService = (httpForce) -> return httpForce
        httpsForceService = (httpsForce) -> return httpsForce


        $routeProvider
            .when '/',
                templateUrl: static_file + 'partials/inicio.html'
                resolve:
                    httpForce: httpForceService
            .when '/sobre',
                # appControllers
                templateUrl: static_file + 'partials/sobre.html'
                controller: 'SobreCtrl'
                resolve:
                    httpForce: httpForceService
            .when '/aulas',
                templateUrl: static_file + 'partials/aulas.html'
                resolve:
                    httpForce: httpForceService
            .when '/user-list',
                # appControllers
                templateUrl: static_file + 'partials/users/user-list.html'
                controller: 'UserListCtrl'
                resolve:
                    users: (User) -> return User.list()
                    httpForce: httpForceService
            .when '/user-form',
                # alunoControllers
                templateUrl: static_file + 'partials/users/user-form.html'
                controller: 'UserFormCtrl'
                resolve:
                    httpsForce: httpsForceService


        # use the HTML5 History API
        $locationProvider.html5Mode(true);
        return
]


# .run ['$http','$cookies', ($http, $cookies) ->
#     $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken']
#     $http.defaults.headers.post['X-CSRFToken'] = $cookies['csrftoken']
#     $http.defaults.headers.put['X-CSRFToken'] = $cookies['csrftoken']
#     return
# ]

.run ['$templateCache', '$http', '$location', ($templateCache, $http, $location) ->
    # $http.get('partials/inicio.html', {cache:$templateCache});
    # $http.get('partials/aulas.html', {cache:$templateCache});
    # $http.get('partials/users/user-list.html', {cache:$templateCache});
    # $http.get('js/all-controllers.min.js', {cache:$templateCache});
    return
]

