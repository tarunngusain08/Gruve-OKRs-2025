// Go TCP Client Example (Q2)
package main
import (
    "fmt"
    "net"
)
func main() {
    conn, err := net.Dial("tcp", "localhost:8080")
    if err != nil {
        fmt.Println("Error:", err)
        return
    }
    buf := make([]byte, 1024)
    n, _ := conn.Read(buf)
    fmt.Println("Received:", string(buf[:n]))
    conn.Close()
}
