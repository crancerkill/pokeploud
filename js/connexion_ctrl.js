'use strict';

/* Service */

function ConnexionCtrl ($scope, ServiceConnexion)
{
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
