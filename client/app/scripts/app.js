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
    'ngTouch',
    'ngStorage',
  ])
  .provider('APIURL', function APIURLProvider() {
        var self = this;
        // this.url = "http://nadrieril:8001/api";
        this.url = "/api";
        this.$get = function(){return self.url;};
    })
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
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
      .when('/connexion', {
        templateUrl: 'views/connexion.html',
        controller: 'ConnexionCtrl'
      })
      .when('/inscriptions', {
        templateUrl: 'views/inscriptions.html',
        controller: 'InscriptionsCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  })
  .config(['$httpProvider',
        function ($httpProvider) {
            $httpProvider.interceptors.push('auth.interceptor');
    }])
    .config(['$resourceProvider', function($resourceProvider) {
      $resourceProvider.defaults.stripTrailingSlashes = false;
    }])
  .run(function($rootScope, auth) {
      $rootScope.auth = auth;
  })
  ;
