'use strict';

/**
 * @ngdoc function
 * @name v24hApp.controller:ProgrammeCtrl
 * @description
 * # ProgrammeCtrl
 * Controller of the v24hApp
 */
angular.module('v24hApp')
  .controller('ProgrammeCtrl', function ($scope, $rootScope) {
    $rootScope.pactive = 'programme';
    var programme = [
    {
        debut: '15:00',
        fin: '16:00',
        nom: "Hockey subaquatique"
    },
    {
        debut: '17:00',
        fin: '19:00',
        nom: "Parcours aquatique"
    },
    {
        debut: '17:30',
        fin: '20:00',
        nom: "Tournoi de Water Polo"
    },
    {
        debut: '20:00',
        fin: '21:00',
        nom: "Challenge Natation"
    },
    {
        debut: '20:00',
        fin: '21:30',
        nom: "Introduction au sauvetage"
    },
    {
        debut: '20:00',
        fin: '21:30',
        nom: "Baptême de plongée"
    },
    {
        debut: '21:00',
        fin: '21:30',
        nom: "Natation synchronisée"
    },
    {
        debut: '21:30',
        fin: '22:30',
        nom: "Finale du Water Polo"
    },
    {
        debut: '21:30',
        fin: '23:00',
        nom: "Joute"
    },
    {
        debut: '23:00',
        fin: '02:00',
        nom: "STYX"
    },
    {
        debut: '08:00',
        fin: '08:30',
        nom: "Challenge cadres"
    }
    ];
    $scope.programme = programme;
  });
