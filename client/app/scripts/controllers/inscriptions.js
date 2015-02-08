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

      var Slotsubscription = $resource(APIURL + '/slotsubscription/:id/');
      var Slot = $resource(APIURL + '/slot/:id');

      var slots = Slot.query(function ()  {
          $scope.slots = {};
          for (var i = 0; i < slots.length; i++) {
              $scope.slots[slots[i].id] = slots[i];
          }
      });

      function reloadSlotsubscriptions() {
          var slotsubscriptions = Slotsubscription.query({'user': auth.getUser().id}, function () {
              $scope.slotsubscriptions = slotsubscriptions;
          });
          $scope.nslot = {id: 1};
      }
      reloadSlotsubscriptions();

      $scope.slotsubscribed = function () {
          var nslot = new Slotsubscription();
          nslot.user = auth.getUser().id;
          nslot.slot = $scope.nslot.id;
          nslot.$save(reloadSlotsubscriptions);
      };
      $scope.unsubscribe = function (sid) {
          Slotsubscription.delete({id: sid}, reloadSlotsubscriptions);
      }
  });
