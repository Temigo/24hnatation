'use strict';

describe('Controller: InscriptionsCtrl', function () {

  // load the controller's module
  beforeEach(module('v24hApp'));

  var InscriptionsCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    InscriptionsCtrl = $controller('InscriptionsCtrl', {
      $scope: scope
    });
  }));
});
