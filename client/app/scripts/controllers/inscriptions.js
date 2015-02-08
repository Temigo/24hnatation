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
      $scope.iu = auth.getUser().id;

      var Slotsubscription = $resource(APIURL + '/slotsubscription/:id/');
      var Slot = $resource(APIURL + '/slot/:id');
      var Activity = $resource(APIURL + '/activity/:id');
      var Team = $resource(APIURL + '/team/:id/', {id:'@id'}, {update: {method: 'PUT'}});
      var User = $resource(APIURL + '/user/:id');

      var slots = Slot.query(function ()  {
          $scope.slots = {};
          for (var i = 0; i < slots.length; i++) {
              $scope.slots[slots[i].id] = slots[i];
          }
      });
      var activities = Activity.query(function ()  {
          $scope.activities = {};
          for (var i = 0; i < activities.length; i++) {
              $scope.activities[activities[i].id] = activities[i];
          }
      });
      var users = User.query(function ()  {
          $scope.users = {};
          for (var i = 0; i < users.length; i++) {
              $scope.users[users[i].id] = users[i];
          }
      });

      function reloadSlotsubscriptions() {
          var slotsubscriptions = Slotsubscription.query({'user': auth.getUser().id}, function () {
              $scope.slotsubscriptions = slotsubscriptions;
          });
          $scope.nslot = {id: 1};
      }
      reloadSlotsubscriptions();

      function reloadTeams() {
          var yourTeams = Team.query({'members': auth.getUser().id}, function () {
              $scope.yourTeams = yourTeams;
          });
          $scope.teams = Team.query();
          $scope.nteam = {activity: 1, name: ''};
          $scope.jteam = {team: 1};
      }
      reloadTeams();

      $scope.slotsubscribed = function () {
          var nslot = new Slotsubscription();
          nslot.user = auth.getUser().id;
          nslot.slot = $scope.nslot.id;
          nslot.$save(reloadSlotsubscriptions);
      };
      $scope.unsubscribe = function (sid) {
          Slotsubscription.delete({id: sid}, reloadSlotsubscriptions);
      };

      $scope.createTeam = function () {
          var nteam = new Team();
          nteam.activity = $scope.nteam.activity;
          nteam.name = $scope.nteam.name;
          nteam.admin = auth.getUser().id;
          nteam.members = [auth.getUser().id];
          nteam.$save(reloadTeams);
      };
      $scope.joinTeam = function () {
          Team.get({id: $scope.jteam.team}, function (cteam) {
              cteam.members.push(auth.getUser().id);
              cteam.$update(reloadTeams);
          });
      };
      $scope.removeFromTeam = function (team, member) {
          Team.get({id: team}, function (cteam) {
              cteam.members.splice(cteam.members.indexOf(member));
              cteam.$update(reloadTeams);
          });
      }
  });
