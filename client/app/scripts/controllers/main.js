'use strict';

/**
 * @ngdoc function
 * @name v24hApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the v24hApp
 */
angular.module('v24hApp')
  .controller('MainCtrl', function ($scope, $rootScope) {
    $rootScope.pactive = 'accueil';
  });
