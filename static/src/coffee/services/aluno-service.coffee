angular.module 'alunoServices', ['ngResource']

.factory 'Aluno', [ '$http', '$q', ($http, $q) ->
    return {
        save: (aluno) ->
            defer = $q.defer()
            $http
                method: 'POST'
                url: '/aluno/'
                data: aluno
            .success (data, status, headers, config) ->
                defer.resolve(data)
                return
            .error (data, status, headers, config) ->
                defer.reject(status)
                return
            return defer.promise
    }
]
