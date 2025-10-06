// Linux Kernel Module: time_module.c
// Prints current jiffies (system timer ticks) for scheduling analysis
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/init.h>
#include <linux/jiffies.h>

static int __init time_init(void) {
    printk(KERN_INFO "Current jiffies: %lu\n", jiffies);
    return 0;
}

static void __exit time_exit(void) {
    printk(KERN_INFO "Exiting time_module\n");
}

module_init(time_init);
module_exit(time_exit);
MODULE_LICENSE("GPL");
