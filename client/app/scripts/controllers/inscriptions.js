'use strict';

/**
 * @ngdoc function
 * @name v24hApp.controller:InscriptionsCtrl
 * @description
 * # InscriptionsCtrl
 * Controller of the v24hApp
 */
angular.module('v24hApp')
  .controller('InscriptionsCtrl', function ($scope, $rootScope, auth, $resource, APIURL) {
      $rootScope.pactive = 'inscriptions';

      var Slotsubscription = $resource(APIURL + '/slotsubscription/:id');
      var Slot = $resource(APIURL + '/slot/:id');

      var slots = Slot.query(function ()  {
          $scope.slots = {};
          for (var i = 0; i < slots.length; i++) {
              $scope.slots[slots[i].id] = slots[i];
          }
      });
      $scope.slotsubscriptions = Slotsubscription.query({'user': auth.getUser().id});
  });
