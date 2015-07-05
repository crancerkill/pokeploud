'use strict';

/* Tirage */

var appServiceTirage = angular.module('services', ['ngResource']);

appServiceTirage.factory('ServiceTirage', ['$resource' , function ($resource)
{
    return $resource('/tirage/:key', {},
        {
            creertirage: {method: 'POST', params: {key: 'creertirage'}, isArray: false}
        });
}]);
