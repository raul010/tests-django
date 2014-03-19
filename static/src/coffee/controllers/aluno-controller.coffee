angular.module 'alunoControllers', []

.controller 'AlunoCtrl', ['$scope', 'Aluno', ($scope, Aluno) ->
    $scope.criate = () ->
        Aluno.save($scope.aluno)
        return
    return
]
