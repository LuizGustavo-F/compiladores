; ModuleID = "arara_program"
source_filename = "arara.arara"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@.str.0 = private unnamed_addr constant [3 x i8] c"\25\64\00", align 1

declare i32 @printf(i8* noundef, ...) # !0
declare i32 @__isoc99_scanf(i8* noundef, ...) # !1

define i32 @main() {
entry:
    %a_ptr = alloca i32, align 4
    %temp0 = getelementptr inbounds ([3 x i8], [3 x i8]* @.str.0, i32 0, i32 0)
    %call_scanf_%temp1 = call i32 (i8*, ...) @__isoc99_scanf(i8* %temp0, i32* %a_ptr)
    ret i32 0
}