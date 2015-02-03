'use strict';

describe('Controller: ProgrammeCtrl', function () {

  // load the controller's module
  beforeEach(module('v24hApp'));

  var ProgrammeCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    ProgrammeCtrl = $controller('ProgrammeCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
