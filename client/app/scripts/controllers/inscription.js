'use strict';

/**
 * @ngdoc function
 * @name v24hApp.controller:InscriptionCtrl
 * @description
 * # InscriptionCtrl
 * Controller of the v24hApp
 */
angular.module('v24hApp')
  .controller('InscriptionCtrl', function ($scope, $rootScope, $http, APIURL, $location) {
    $rootScope.pactive = "inscription";
    $scope.user = {};
    $scope.inscription = function () {
        $http.post(APIURL + '/signup/', $scope.user).then(function () {
            $rootScope.justInscrit = true;
            $location.path('/connexion');
        }, function () {
            $scope.message = "Vous êtes déjà inscrit. Votre mot de passe vous a été envoyé par mail ; vérifiez vos spams"
        });
    };
  });
