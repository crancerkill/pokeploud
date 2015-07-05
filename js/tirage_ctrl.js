'use strict';

/* Service */

function TirageCtrl ($scope, ServiceTirage, ServiceConnexion)
{
    ServiceTirage.get(function (result)
        {
            $scope.listetirage = result.tirages;
        }
    );

    $scope.addtirage = function ()
    {
        ServiceTirage.creertirage({
                pseudo: $scope.pseudo
            },
            function (result) {
                $scope.tiragevalide = result.message
            }
        );

        $scope.pseudo = "";
    };

    $scope.refreshtirage = function ()
    {
        ServiceTirage.get(function (result) {
            $scope.listetirage = result.tirages;
        });
    };

    $scope.connexion = function ()
    {
        ServiceConnexion.connexion(
            function (result) {
            }
        );
    };

    $scope.affuser = function ()
    {
        ServiceConnexion.affuser(
            function (result) {
                alert(result.user)
            }
        );
    };
}