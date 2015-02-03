'use strict';

describe('Controller: ReglementCtrl', function () {

  // load the controller's module
  beforeEach(module('v24hApp'));

  var ReglementCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    ReglementCtrl = $controller('ReglementCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
