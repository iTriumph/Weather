function GreetCtrl($scope) {
    $scope.name = 'World';
}

function ListCtrl($scope) {
    $scope.names = ['Igor', 'Misko', 'Vojta'];
}
var app = angular.module("myapp",[]);
app.controller("GreetCtrl",GreetCtrl);
app.controller("ListCtrl",ListCtrl);
