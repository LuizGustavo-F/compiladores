; ModuleID = "arara_program"
source_filename = "arara.arara"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"


declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)

define i32 @main() {
entry:
  ; READ a
  ret i32 0
}