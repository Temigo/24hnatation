'use strict';

/**
 * @ngdoc service
 * @name v24hApp.auth
 * @description
 * # auth
 * Service in the v24hApp.
 */
  angular.module('v24hApp')

  // cannot inject $http directly because it would cause a conflict when registering AuthInterceptor
  .factory('auth', ['$injector', '$localStorage', '$q', 'APIURL', '$rootScope',
      function ($injector, $localStorage, $q, APIURL, $rootScope) {
          if ($localStorage.auth === undefined) {
              $localStorage.auth = {
                  token: null,
                  user: null
              };
          }
          return {
              login: function(credentials) {
                  return $injector.get('$http').post(APIURL + '/api-token-auth/', credentials, {'headers':{'Content-Type':"application/json"}}).then(
                      function(response) {
                          $localStorage.auth.token = response.data.token;
                          return $injector.get('$http').get(APIURL + '/user/?username=' + credentials.username, {'headers': {'Authorization': "JWT " + response.data.token}}).then(function (user) {
                              $localStorage.auth.user = user.data[0];
                              return user.data[0];
                          });
                      },
                      function(response) {
                          $localStorage.auth.token = null;
                          return $q.reject(response);
                      });
              },
              logout: function() {
                  $localStorage.auth.token = null;
                  // Mieux gérer ça dans main.js (supprimer les objets, etc.) -- TODO
                  $rootScope.$broadcast('auth.hasLoggedOut');
              },
              isAuthenticated: function() {
                  return $localStorage.auth.token !== null;
              },
              getToken: function() {
                  return $localStorage.auth.token;
              },
              getUser: function() {
                  return $localStorage.auth.user;
              }
          };
  }])

  .factory('auth.interceptor', ['auth', '$q',
      function (AuthService, $q) {
          return {
              request: function(config) {
                  config.headers = config.headers || {};
                  if (AuthService.isAuthenticated()) {
                      config.headers.Authorization = 'JWT ' + AuthService.getToken();
                  }

                  // config.params = config.params || {};
                  // // to improve: necessary for ui.bootstrap ; and the token is useless for static files
                  // if (AuthService.isAuthenticated() && /^((http)|[^a-z])/.test(config.url)) {
                  //     config.params["bearer"] = AuthService.getToken();
                  // }
                  return config || $q.when(config);
              },
              response: function(response) {
                  if (response.status === 401) {
                      AuthService.logout();
                      // TODO: Redirect user to login page.
                  }
                  return response || $q.when(response);
              },
              responseError: function(response) {
                  console.log(response);
                  if (response.status === 401) {
                      AuthService.logout();
                      // TODO: Redirect user to login page.
                  }
                  return $q.reject(response);
              }
          };
  }]);
