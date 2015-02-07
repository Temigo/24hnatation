'use strict';

/**
 * @ngdoc overview
 * @name v24hApp
 * @description
 * # v24hApp
 *
 * Main module of the application.
 */
angular
  .module('v24hApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
      .when('/about', {
        templateUrl: 'views/about.html',
        controller: 'AboutCtrl'
      })
      .when('/reglement', {
        templateUrl: 'views/reglement.html',
        controller: 'ReglementCtrl'
      })
      .when('/programme', {
        templateUrl: 'views/programme.html',
        controller: 'ProgrammeCtrl'
      })
      .when('/contact', {
        templateUrl: 'views/contact.html',
        controller: 'ContactCtrl'
      })
      .when('/partenaires', {
        templateUrl: 'views/partenaires.html',
        controller: 'PartenairesCtrl'
      })
      .when('/inscription', {
        templateUrl: 'views/inscription.html',
        controller: 'InscriptionCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
