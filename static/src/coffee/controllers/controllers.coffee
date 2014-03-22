angular.module 'appControllers', []

.controller 'UserListCtrl', ['$scope', '$location', 'users',
    ($scope, $location, users) ->
        a = $location.absUrl()
        b = $location.protocol()
        # alert  a + ' - ' + b
        $scope.users = users
        return
]


.controller 'UserFormCtrl', ['$scope', 'User', ($scope, User) ->
    # setTimeout () ->
    #     console.log 'automatically update view?'
    #     $scope.$apply()
    #     response.setIntHeader("Refresh", 1)
    #     return
    # , 1000

    #alert "oi"
    # $window.alert "oi"
    # $window.location.reload()
    $scope.criate = () ->
        User.save($scope.user)
        return
    return
]

# .controller 'UserProxyFormCtrl', ['$window', '$scope', ($window, $scope) ->
#     # alert 'ola'
#     # $window.location.href = 'https://localhost/user-form'
#     # $window.location.reload();
#     return
# ]

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
