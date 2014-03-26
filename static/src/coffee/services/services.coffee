angular.module 'appServices', ['ngResource']

.factory 'User', [ '$http', '$q', '$location', userFactory = ($http, $q, $location) ->
    return {
        list: () ->
            defer = $q.defer()
            $http
                method: 'GET'
                url: '/rest/user-list/'
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
                url: '/rest/user-create/'
                # withCredentials: true
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
# if browser is direct: http://host/form-user, then proxy redirect to https,
# so not enter here
.factory 'httpsForce', ['$rootScope', '$location', '$window',
    httpsForceFactory = ($rootScope, $location, $window) ->
        if $location.protocol() == 'http'
            # alert 'httpsForce'
            url = 'https://' + $location.host() + $location.path()
            $window.location.href = url
            $rootScope.$apply()
        return
]

# changes all absUrl when it comes from https and itself not needs to be https
.factory 'httpForce', ['$rootScope', '$location', '$window',
    httpForceFactory = ($rootScope, $location, $window) ->
        if $location.protocol() == 'https'
            url = 'http://' + $location.host() + $location.path()
            $window.location.href = url
            $rootScope.$apply()
        return
]
