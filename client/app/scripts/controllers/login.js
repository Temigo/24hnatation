'use strict';

/**
 * @ngdoc function
 * @name v24hApp.controller:LoginCtrl
 * @description
 * # LoginCtrl
 * Controller of the v24hApp
 */
angular.module('v24hApp')
  .controller('LoginCtrl', function ($scope, auth, $location, $routeParams) {
      auth.login({email: $routeParams.email, password: $routeParams.password}).then(function () {
          console.log("User connected!");
          $location.url('/inscriptions');
      }, function () {
          $location.url('/connexion');
      });
  });
