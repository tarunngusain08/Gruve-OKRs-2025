// Go Socket Example (Q1)
package main

import (
    "fmt"
    "net"
)

func main() {
    ln, err := net.Listen("tcp", ":8080")
    if err != nil {
        fmt.Println("Error:", err)
        return
    }
    fmt.Println("Server listening on :8080")
    for {
        conn, err := ln.Accept()
        if err != nil {
            fmt.Println("Accept error:", err)
            continue
        }
        fmt.Fprintf(conn, "Hello from Go server!\n")
        conn.Close()
    }
}
