'use strict';

describe('Controller: PartenairesCtrl', function () {

  // load the controller's module
  beforeEach(module('v24hApp'));

  var PartenairesCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    PartenairesCtrl = $controller('PartenairesCtrl', {
      $scope: scope
    });
  }));
