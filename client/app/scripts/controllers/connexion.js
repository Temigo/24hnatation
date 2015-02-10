'use strict';

/**
 * @ngdoc function
 * @name v24hApp.controller:ConnexionCtrl
 * @description
 * # ConnexionCtrl
 * Controller of the v24hApp
 */
angular.module('v24hApp')
  .controller('ConnexionCtrl', function ($scope, $rootScope, auth, $location) {
    $rootScope.pactive = 'connexion';
    if ($rootScope.justInscrit) {
        $scope.message = "Un email avec votre mot de passe vient de vous être envoyé";
        delete $rootScope.justInscrit;
    }

    $scope.user = {
        email: '',
        password: ''
    };

    $scope.connexion = function() {
        $scope.message = "";
        auth.login($scope.user).then(function () {
            console.log("User connected!");
            $location.path('/inscriptions');
        }, function () {
            $scope.message = "Login ou mot de passe incorrect";
            $scope.user.password = "";
        });
    };
  });
