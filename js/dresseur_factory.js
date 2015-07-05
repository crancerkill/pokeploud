'use strict';

/* Service */

var appService = angular.module('services', ['ngResource']);

appService.factory('ServiceDresseur', function ($resource)
{
    return $resource('/dresseur/:key', {},
        {
            ajouteDresseur: {method: 'POST', params: {key: 'addDresseur'}, isArray: false},
            aleaDresseur: {method: 'POST', params: {key: 'tirageAlea'}, isArray: false}
        });
});