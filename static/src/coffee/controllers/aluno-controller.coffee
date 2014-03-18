alunoControllers = angular.module 'alunoControllers', []

alunoControllers.run ['$http','$cookies', ($http, $cookies) ->
    $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken']
    return
]

alunoControllers.controller 'AlunoCtrl', ['$scope', 'Aluno', ($scope, Aluno) ->
    $scope.criar = () ->
        Aluno.save($scope.aluno)
        return
    return
]
