'use strict';

/* ServiceDresseur */
function DresseurCtrl ($scope, $routeParams, ServiceDresseur)
{
    $scope.letirage = $routeParams.pseudotirage

    ServiceDresseur.aleaDresseur({
        tirage: $routeParams.pseudotirage
    },
    function (result) {
        $scope.equipe = result.dresseurs;
    });

    $scope.callService = function()
    {
        ServiceDresseur.aleaDresseur({
            tirage: $routeParams.pseudotirage
        },
        function(result)
        {
            $scope.equipe = result.dresseurs;
        });
        var nbdresseurs = $scope.equipe.length
        var tirage = Math.floor((Math.random() * nbdresseurs));
        $scope.tirage = $scope.equipe[tirage]

    };

    $scope.addDresseur = function()
    {
        ServiceDresseur.ajouteDresseur({
            tirage: $routeParams.pseudotirage,
            nomig: $scope.nomig,
            codeami: $scope.codeami
        },
        function(result)
            {
                $scope.dresseurvalide = result.message
            }
        );

        $scope.nomig = ""
        $scope.codeami = ""

    };

    $scope.refreshdresseur = function()
    {
        ServiceDresseur.aleaDresseur({
            tirage: $routeParams.pseudotirage
        },
        function(result)
        {
            $scope.equipe = result.dresseurs;
        });
    }
}/**
 * Created by yoleroy on 22/06/2015.
 */
