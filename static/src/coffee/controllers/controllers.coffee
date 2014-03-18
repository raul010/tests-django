angular.module 'appControllers', []

.controller 'UserCtrl', ['$scope', '$http', 'users',
    ($scope, $http, users) ->
        $scope.users = users
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
