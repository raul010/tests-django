angular.module 'appControllers', []

.controller 'UserListCtrl', ['$scope', '$location', 'users',
    ($scope, $location, users) ->
        a = $location.absUrl()
        b = $location.protocol()
        # alert  a + ' - ' + b
        $scope.users = users
        return
]


.controller 'UserFormCtrl', ['$scope','$window', '$location', 'User', '$http'
     ($scope, $window, $location, User, $http) ->
        $http.defaults.useXDomain = true
        delete $http.defaults.headers.common['X-Requested-With']

        $scope.criate = () ->
            User.save($scope.user)
            return
        return
]

.controller 'SobreCtrl', ['$scope', '$http',
    ($scope, $http) ->
        $scope.hideSobre = false;
        $scope.isTrabalho = false;
        $scope.isContato = false;
        $scope.inclui = (param) ->
            if param is 'sobre'
                $scope.hideSobre = false
                $scope.isTrabalho = false
                $scope.isContato = false

            else if param is 'trabalho'
                $scope.hideSobre = true
                $scope.isTrabalho = true
                $scope.isContato = false

            else if param is 'contato'
                $scope.hideSobre = true
                $scope.isTrabalho = false
                $scope.isContato = true

        return
]
