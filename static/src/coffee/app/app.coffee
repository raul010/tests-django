# alert 'Raul'
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

.run ['$templateCache', '$http', ($templateCache, $http) ->
    $http.get('partials/inicio.html', {cache:$templateCache});
    # $http.get('partials/aulas.html', {cache:$templateCache});
    $http.get('partials/user.html', {cache:$templateCache});
    # $http.get('js/all-controllers.min.js', {cache:$templateCache});
    return
]

.config ['$routeProvider', '$locationProvider',
    ($routeProvider, $locationProvider) ->
        $routeProvider
            .when '/',
                templateUrl: static_file + 'partials/inicio.html'
            .when '/sobre',
                templateUrl: static_file + 'partials/sobre.html'
                # controller: 'SobreCtrl'
            .when '/aulas',
                templateUrl: static_file + 'partials/aulas.html'
                # controller: 'AulasCtrl'
            .when '/users',
                templateUrl: static_file + 'partials/user.html'
                controller: 'UserCtrl'
                resolve:
                    users: (User) ->
                        return User.list()
            .when '/aluno',
                templateUrl: static_file + 'partials/aluno.html'
                controller: 'AlunoCtrl'
                # resolve:
                #     aluno: (Aluno) ->
                #         return Aluno.update()


        # //use the HTML5 History API
        # $locationProvider.html5Mode(true);
        return
]
