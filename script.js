var app = angular.module('loginSignupApp', []);

app.controller('MainController', function($scope, $http) {
    $scope.isLogin = true;  // Default to login
    $scope.isLoggedIn = false;
    $scope.loggedInUser = {};

    $scope.toggleLogin = function() {
        $scope.isLogin = !$scope.isLogin;  // Switch between login and signup
    };

    $scope.signup = function() {
        $http.post('/api/signup', $scope.user)
            .then(function(response) {
                alert(response.data.message);
                $scope.user = {};  // Clear user data
                $scope.toggleLogin();  // Switch to login
            })
            .catch(function(error) {
                alert(error.data.message);
            });
    };

    $scope.login = function() {
        $http.post('/api/login', $scope.user)
            .then(function(response) {
                alert(response.data.message);
                $scope.loggedInUser = response.data.data;  // Store user data
                $scope.isLoggedIn = true;  // User is logged in
                $scope.user = {};  // Clear user data
            })
            .catch(function(error) {
                alert(error.data.message);
            });
    };

    $scope.logout = function() {
        $http.post('/logout')
            .then(function(response) {
                alert(response.data.message);
                $scope.loggedInUser = {};  // Clear user data
                $scope.isLoggedIn = false;  // User is logged out
            })
            .catch(function(error) {
                alert("Logout failed!");
            });
    };
});
