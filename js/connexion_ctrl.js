'use strict';

/* Service */

function ConnexionCtrl ($scope, ServiceConnexion, ServiceUpload)
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

    $scope.addimage = function ()
    {
        ServiceUpload.upload({
            upload: $scope.upload
        },
            function (result) {
            }
        );
    };
}
