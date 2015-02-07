'use strict';

describe('Controller: ConnexionCtrl', function () {

  // load the controller's module
  beforeEach(module('v24hApp'));

  var ConnexionCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    ConnexionCtrl = $controller('ConnexionCtrl', {
      $scope: scope
    });
  }));

});
