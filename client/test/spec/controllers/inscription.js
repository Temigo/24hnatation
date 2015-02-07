'use strict';

describe('Controller: InscriptionCtrl', function () {

  // load the controller's module
  beforeEach(module('v24hApp'));

  var InscriptionCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    InscriptionCtrl = $controller('InscriptionCtrl', {
      $scope: scope
    });
  }));
