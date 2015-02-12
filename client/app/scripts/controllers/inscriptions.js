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
      $scope.ptri = 'start';
      $scope.gtypes = {
          binet: "Asso/Binet",
          school: "École",
          section: "Section"
      };

      var Slotsubscription = $resource(APIURL + '/slotsubscription/:id/');
      var Slot = $resource(APIURL + '/slot/:id/', {id:'@id'});
      var Group = $resource(APIURL + '/group/:id/', {id:'@id'});
      var Profile = $resource(APIURL + '/profile/:id/', {id:'@id'}, {update: {method: 'PUT'}});
      var Activity = $resource(APIURL + '/activity/:id/', {id:'@id'});
      var Team = $resource(APIURL + '/team/:id/', {id:'@id'});
      var Teamsubscription = $resource(APIURL + '/teamsubscription/:id/', {id:'@id'});
      var User = $resource(APIURL + '/user/:id/');

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
      var uprofile = Profile.query({'user': auth.getUser().id}, function (uprofile) {
          $scope.profile = uprofile[0];
      });

      var slots;
      function reloadSlots() {
          slots = Slot.query(function ()  {
              $scope.aslots = slots;
              $scope.slots = {};
              for (var i = 0; i < slots.length; i++) {
                  $scope.slots[slots[i].id] = slots[i];
              }
          });
      }

      function reloadSlotsubscriptions() {
          var slotsubscriptions = Slotsubscription.query({'user': auth.getUser().id}, function () {
              $scope.slotsubscriptions = slotsubscriptions;
          });
          $scope.nslot = {id: 1};
          reloadSlots();
      }
      reloadSlotsubscriptions();

      function reloadGroups() {
          var groups = Group.query(function ()  {
              $scope.groups = {};
              for (var i = 0; i < groups.length; i++) {
                  $scope.groups[groups[i].id] = groups[i];
              }
          });
      };
      reloadGroups();

      function reloadTeams() {
          var yourTeams = Teamsubscription.query({'user': auth.getUser().id}, function () {
              for (var i = 0; i < yourTeams.length; i++) {
                  yourTeams[i].members = Teamsubscription.query({'team': yourTeams[i].team});
              }
              $scope.yourTeams = yourTeams;
          });
          $scope.nteam = {activity: 1, name: ''};
          $scope.jteam = {team: 1};

          var teams = Team.query(function ()  {
              $scope.teams = {};
              for (var i = 0; i < teams.length; i++) {
                  $scope.teams[teams[i].id] = teams[i];
              }
          });
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
          nteam.$save(function (nteams) {
              var nteams = new Teamsubscription();
              nteams.user = auth.getUser().id;
              nteams.team = nteam.id;
              nteams.$save(reloadTeams);
          });
      };
      $scope.joinTeam = function () {
          var nteams = new Teamsubscription();
          nteams.user = auth.getUser().id;
          nteams.team = $scope.jteam.team;
          nteams.$save(reloadTeams);
      };
      $scope.removeFromTeam = function (id) {
          Teamsubscription.delete({id: id}, reloadTeams);
      };
      $scope.addGroup = function (id) {
          $scope.profile.groups.push(id);
          console.log($scope.profile);
          $scope.profile.$update();
      };
      $scope.removeGroup = function (id) {
          $scope.profile.groups.splice($scope.profile.groups.indexOf(id));
          $scope.profile.$update();
      };
      $scope.createGroup = function (name, type) {
          $scope.cgroup = {};
          var ngroup = new Group();
          ngroup.name = name;
          ngroup.type = type;
          ngroup.$save(function (ngroups) {
              $scope.addGroup(ngroups.id);
              reloadGroups();
          });
      };
      $scope.orderSlots = function (s) {
          return slots[s.slot] && slots[s.slot].start;
      };
  });
