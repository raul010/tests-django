static_file = '/static/'

angular.module 'baseApp', [
    'ngRoute',
    'ngCookies',
    'appControllers',
    'appServices',
    'alunoControllers',
    'alunoServices',
]

.run ['$http','$cookies', ($http, $cookies) ->
    $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken']
    return
]

.run ['$templateCache', '$http', ($templateCache, $http) ->
    $http.get('partials/inicio.html', {cache:$templateCache});
    $http.get('partials/aulas.html', {cache:$templateCache});
    $http.get('partials/users/user-list.html', {cache:$templateCache});
    # $http.get('js/all-controllers.min.js', {cache:$templateCache});
    return
]

.config ['$interpolateProvider', ($interpolateProvider) ->
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
    return
]

.config ['$routeProvider', '$locationProvider',
    ($routeProvider, $locationProvider) ->
        $routeProvider
            .when '/',
                templateUrl: static_file + 'partials/inicio.html'
                # controller: ''
            .when '/sobre',
                # appControllers
                templateUrl: static_file + 'partials/sobre.html'
                controller: 'SobreCtrl'
            .when '/aulas',
                templateUrl: static_file + 'partials/aulas.html'
                # controller: 'AulasCtrl'
            .when '/user-list',
                # appControllers
                templateUrl: static_file + 'partials/users/user-list.html'
                controller: 'UserListCtrl'
                resolve:
                    users: (User) ->
                        return User.list()
            .when '/user-form',
                # alunoControllers
                templateUrl: static_file + 'partials/users/user-form.html'
                controller: 'UserFormCtrl'


#        //use the HTML5 History API
        # $locationProvider.html5Mode(true);
        # return
]
