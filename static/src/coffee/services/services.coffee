angular.module 'appServices', ['ngResource']

.factory 'User', [ '$http', '$q', userFactory = ($http, $q) ->
    return {
        list: () ->
            defer = $q.defer()
            $http
                method: 'GET'
                url: '/rest/user/'
            .success (data, status, headers, config) ->
                defer.resolve(data)
                return
            .error (data, status, headers, config) ->
                defer.reject(status)
                return
            return defer.promise

        save: (post) ->
            defer = $q.defer()
            $http
                method: 'POST'
                url: '/rest/user/'
                data: post
            .success (data, status, headers, config) ->
                defer.resolve(data)
                return
            .error (data, status, headers, config) ->
                defer.reject(status)
                return
            return defer.promise
    }
]
