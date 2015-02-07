'use strict';

/**
 * @ngdoc function
 * @name v24hApp.controller:ConnexionCtrl
 * @description
 * # ConnexionCtrl
 * Controller of the v24hApp
 */
angular.module('v24hApp')
  .controller('ConnexionCtrl', function ($scope, $rootScope, auth) {
    $rootScope.pactive = 'connexion';

    $scope.user = {
        username: '',
        password: ''
    };

    $scope.connexion = function() {
        $scope.message = "";
        auth.login($scope.user).then(function () {
            console.log("Connecte");
        }, function () {
            $scope.message = "Login ou mot de passe incorrect";
            $scope.user.password = "";
        });
    };
  });
