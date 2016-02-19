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
        debut: '11:00',
        fin: '',
        nom: "Départ du relais de 24 heures"
    },
    {
        debut: '14:00',
        fin: '17:30',
        nom: "Parcours aquatique"
    },
    {
        debut: '15:00',
        fin: '16:00',
        nom: "Initiation au secourisme"
    },
    {
        debut: '17:30',
        fin: '22:30',
        nom: "Tournoi de Water Polo"
    },
    {
        debut: '18:30',
        fin: '21:00',
        nom: "Baptêmes de plongée"
    },
    {
        debut: '19:00',
        fin: '23:30',
        nom: "Venue d'ostéopathes"
    },
    {
        debut: '19:30',
        fin: '22:00',
        nom: "Challenge natation"
    },
    {
        debut: '21:00',
        fin: '22:00',
        nom: "Ballet de natation synchronisée"
    },
    {
        debut: '22:00',
        fin: '22:30',
        nom: "Demie et finale du tournoi de Water Polo"
    },
    {
        debut: '22:30',
        fin: '23:00',
        nom: "Joutes aquatiques"
    },
    {
        debut: '23:00',
        fin: '02:00',
        nom: "STYX"
    },
    {
        debut: '07:00',
        fin: '08:00',
        nom: "Petit-déjeuner et plongeons pour tous"
    },
    {
        debut: '08:00',
        fin: '09:00',
        nom: "Défi cadres DFHM"
    },
    {
        debut: '09:00',
        fin: '10:00',
        nom: "Séance de sophrologie aquatique"
    },
    {
        debut: '11:00',
        fin: '',
        nom: "Remise des prix, tirage de la tombola et cocktail de clôture"
    }
    ];
    $scope.programme = programme;
  });
