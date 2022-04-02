package main

import (
	"fmt"
	"sync"
)

type Router struct {
	Routes []string
}

var once sync.Once
var singleton *Router

func NewRouter() *Router {
	once.Do(func() {
		routes := make([]string, 1)
		singleton = &Router{Routes: routes}
	})
	return singleton
}

func (router *Router) AddRoutes(routes []string) {
	router.Routes = append(router.Routes, routes...)
}

func (router *Router) GetRoutes() []string {
	return router.Routes
}

func main() {
	router := NewRouter()
	router.AddRoutes([]string{"/api/user", "/api/book"})
	fmt.Println(router.GetRoutes())

	newRouter := NewRouter()
	newRouter.AddRoutes([]string{"/api/v1/devices", "/api/v1/network"})
	fmt.Println(newRouter.GetRoutes())
}
