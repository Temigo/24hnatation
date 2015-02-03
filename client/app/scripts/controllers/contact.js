'use strict';

/**
 * @ngdoc function
 * @name v24hApp.controller:ContactCtrl
 * @description
 * # ContactCtrl
 * Controller of the v24hApp
 */
angular.module('v24hApp')
  .controller('ContactCtrl', function ($scope, $rootScope) {
    $rootScope.pactive = 'contact';
  });
