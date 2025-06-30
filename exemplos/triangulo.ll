; ModuleID = "arara_program"
source_filename = "arara.arara"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@.str.0 = private unnamed_addr constant [3 x i8] c"\25\64\00", align 1
@.str.1 = private unnamed_addr constant [32 x i8] c"\54\72\69\C3\A2\6E\67\75\6C\6F\20\65\71\75\69\6C\C3\A1\74\65\72\6F\20\76\C3\A1\6C\69\64\6F\0A\00", align 1
@.str.2 = private unnamed_addr constant [31 x i8] c"\54\72\69\C3\A2\6E\67\75\6C\6F\20\69\73\C3\B3\73\63\65\6C\65\73\20\76\C3\A1\6C\69\64\6F\0A\00", align 1
@.str.3 = private unnamed_addr constant [29 x i8] c"\54\72\69\C3\A2\6E\67\75\6C\6F\20\65\73\63\61\6C\65\6E\6F\20\76\C3\A1\6C\69\64\6F\0A\00", align 1
@.str.4 = private unnamed_addr constant [20 x i8] c"\4D\65\64\69\64\61\73\20\69\6E\76\C3\A1\6C\69\64\61\73\0A\00", align 1
@.str.5 = private unnamed_addr constant [54 x i8] c"\45\72\72\6F\3A\20\76\61\6C\6F\72\65\73\20\6E\65\67\61\74\69\76\6F\73\20\6F\75\20\7A\65\72\6F\20\6E\C3\A3\6F\20\73\C3\A3\6F\20\70\65\72\6D\69\74\69\64\6F\73\0A\00", align 1

declare i32 @printf(i8* noundef, ...) # !0
declare i32 @__isoc99_scanf(i8* noundef, ...) # !1

define i32 @main() {
entry:
    %a_ptr = alloca i32, align 4
    %b_ptr = alloca i32, align 4
    %c_ptr = alloca i32, align 4
    %temp0 = getelementptr inbounds ([3 x i8], [3 x i8]* @.str.0, i32 0, i32 0)
    %call_scanf_%temp1 = call i32 (i8*, ...) @__isoc99_scanf(i8* %temp0, i32* %a_ptr)
    %temp2 = getelementptr inbounds ([3 x i8], [3 x i8]* @.str.0, i32 0, i32 0)
    %call_scanf_%temp3 = call i32 (i8*, ...) @__isoc99_scanf(i8* %temp2, i32* %b_ptr)
    %temp4 = getelementptr inbounds ([3 x i8], [3 x i8]* @.str.0, i32 0, i32 0)
    %call_scanf_%temp5 = call i32 (i8*, ...) @__isoc99_scanf(i8* %temp4, i32* %c_ptr)
    %temp6 = load i32, i32* %a_ptr, align 4
    %_t0 = icmp sgt i32 %temp6, 0
    %temp7 = load i32, i32* %b_ptr, align 4
    %_t1 = icmp sgt i32 %temp7, 0
    %_t2 = and i1 %_t0, %_t1
    br i1 %_t2, label %block_temp8, label %L0
block_temp8:
    %temp9 = load i32, i32* %a_ptr, align 4
    %temp10 = load i32, i32* %b_ptr, align 4
    %_t3 = add i32 %temp9, %temp10
    %temp11 = load i32, i32* %c_ptr, align 4
    %_t4 = icmp sgt i32 %_t3, %temp11
    %temp12 = load i32, i32* %a_ptr, align 4
    %temp13 = load i32, i32* %c_ptr, align 4
    %_t5 = add i32 %temp12, %temp13
    %temp14 = load i32, i32* %b_ptr, align 4
    %_t6 = icmp sgt i32 %_t5, %temp14
    %_t7 = and i1 %_t4, %_t6
    br i1 %_t7, label %block_temp15, label %L2
block_temp15:
    %temp16 = load i32, i32* %a_ptr, align 4
    %temp17 = load i32, i32* %b_ptr, align 4
    %_t8 = icmp eq i32 %temp16, %temp17
    %temp18 = load i32, i32* %b_ptr, align 4
    %temp19 = load i32, i32* %c_ptr, align 4
    %_t9 = icmp eq i32 %temp18, %temp19
    %_t10 = and i1 %_t8, %_t9
    br i1 %_t10, label %block_temp20, label %L4
block_temp20:
    %temp21 = getelementptr inbounds ([32 x i8], [32 x i8]* @.str.1, i32 0, i32 0)
    %call_printf_%temp22 = call i32 (i8*, ...) @printf(i8* %temp21)
    br label %L5
L4:
    %temp24 = load i32, i32* %a_ptr, align 4
    %temp25 = load i32, i32* %b_ptr, align 4
    %_t11 = icmp eq i32 %temp24, %temp25
    %temp26 = load i32, i32* %a_ptr, align 4
    %temp27 = load i32, i32* %c_ptr, align 4
    %_t12 = icmp eq i32 %temp26, %temp27
    %_t13 = or i1 %_t11, %_t12
    br i1 %_t13, label %block_temp28, label %L6
block_temp28:
    %temp29 = getelementptr inbounds ([31 x i8], [31 x i8]* @.str.2, i32 0, i32 0)
    %call_printf_%temp30 = call i32 (i8*, ...) @printf(i8* %temp29)
    br label %L7
L6:
    %temp32 = getelementptr inbounds ([29 x i8], [29 x i8]* @.str.3, i32 0, i32 0)
    %call_printf_%temp33 = call i32 (i8*, ...) @printf(i8* %temp32)
L5:
    br label %L3
L2:
    %temp35 = getelementptr inbounds ([20 x i8], [20 x i8]* @.str.4, i32 0, i32 0)
    %call_printf_%temp36 = call i32 (i8*, ...) @printf(i8* %temp35)
L3:
    br label %L1
L0:
    %temp38 = getelementptr inbounds ([54 x i8], [54 x i8]* @.str.5, i32 0, i32 0)
    %call_printf_%temp39 = call i32 (i8*, ...) @printf(i8* %temp38)
L1:
    ret i32 0
}