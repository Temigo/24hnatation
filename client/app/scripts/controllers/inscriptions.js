'use strict';

/**
 * @ngdoc function
 * @name v24hApp.controller:InscriptionsCtrl
 * @description
 * # InscriptionsCtrl
 * Controller of the v24hApp
 */
angular.module('v24hApp')
  .controller('InscriptionsCtrl', function ($scope, $rootScope, auth) {
      $rootScope.pactive = 'inscriptions';
      console.log(auth.getUser());
  });
