var app = angular.module('app', [
    'ngResource',
    'ngRoute'
]);

app.config(['$routeProvider', function($routeProvider)
{
    // parameters in access attribute are used in .run() method
    $routeProvider
        .when('/', {
            templateUrl: '/templates/tirage.html',
            controller: TirageCtrl
        })
        .when('/listeca/:pseudotirage', {
            templateUrl: '/templates/dresseur.html',
            controller: DresseurCtrl
        })
        .when('/login', {
            templateUrl: '/templates/connexion.html',
            controller: ConnexionCtrl
        })
        .otherwise({
            redirectTo: '/'
        });
}]);

app.config(['$locationProvider', function($locationProvider)
{
    $locationProvider.html5Mode(true);
}]);

app.factory('ServiceTirage', function ($resource)
{
    return $resource('/tirage/:key', {},
        {
            creertirage: {method: 'POST', params: {key: 'creertirage'}, isArray: false}
        });
});

app.factory('ServiceDresseur', function ($resource)
{
    return $resource('/dresseur/:key', {},
        {
            ajouteDresseur: {method: 'POST', params: {key: 'addDresseur'}, isArray: false},
            aleaDresseur: {method: 'POST', params: {key: 'tirageAlea'}, isArray: false}
        });
});

app.factory('ServiceConnexion', function ($resource)
{
    return $resource('/service/connexion/:key', {},
        {
            connexion: {method: 'POST', params: {key: 'connexion'}, isArray: false},
            affuser: {method: 'POST', params: {key: 'affuser'}, isArray: false}
        });
});

app.factory('ServiceUpload', function ($resource)
{
    return $resource('/upload/:key', {},
        {
            upload: {method: 'POST', params: {key: 'upload'}, isArray: false}
        });
});






