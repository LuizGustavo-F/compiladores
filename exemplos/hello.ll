; ModuleID = "arara_program"
source_filename = "arara.arara"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@.str.0 = private unnamed_addr constant [15 x i8] c"\48\65\6C\6C\6F\2C\20\4D\75\6E\64\6F\21\0A\00", align 1
@.str.1 = private unnamed_addr constant [4 x i8] c"\25\64\0A\00", align 1

declare i32 @printf(i8*, ...)
declare i32 @__isoc99_scanf(i8*, ...)

define i32 @main() {
entry:
    %temp0 = getelementptr inbounds i8, [15 x i8]* @.str.0, i64 0, i64 0
    %call_printf_%temp1 = call i32 (i8*, ...) @printf(i8* %temp0)
    ret i32 0
}