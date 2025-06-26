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
  %temp0 = getelementptr inbounds ([3 x i8], [3 x i8]* @.str.0, i64 0, i64 0)
  %call_scanf_temp1 = call i32 (i8*, ...) @__isoc99_scanf(i8* %temp0, i32* %a_ptr)
  %temp2 = getelementptr inbounds ([3 x i8], [3 x i8]* @.str.0, i64 0, i64 0)
  %call_scanf_temp3 = call i32 (i8*, ...) @__isoc99_scanf(i8* %temp2, i32* %b_ptr)
  %temp4 = getelementptr inbounds ([3 x i8], [3 x i8]* @.str.0, i64 0, i64 0)
  %call_scanf_temp5 = call i32 (i8*, ...) @__isoc99_scanf(i8* %temp4, i32* %c_ptr)
  %temp6 = load i32, i32* %a_ptr, align 4
  %temp7 = icmp ne i32 %temp6, 0
  %_t0 = icmp sgt i1 %temp7, 0
  %temp8 = load i32, i32* %b_ptr, align 4
  %temp9 = icmp ne i32 %temp8, 0
  %_t1 = icmp sgt i1 %temp9, 0
  %_t2 = and i1 %_t0, %_t1
  %temp10 = load i32, i32* %a_ptr, align 4
  %temp11 = load i32, i32* %b_ptr, align 4
  %_t3 = add i32 %temp10, %temp11
  %temp12 = icmp ne i32 %_t3, 0
  %temp13 = load i32, i32* %c_ptr, align 4
  %temp14 = icmp ne i32 %temp13, 0
  %_t4 = icmp sgt i1 %temp12, %temp14
  %temp15 = load i32, i32* %a_ptr, align 4
  %temp16 = load i32, i32* %c_ptr, align 4
  %_t5 = add i32 %temp15, %temp16
  %temp17 = icmp ne i32 %_t5, 0
  %temp18 = load i32, i32* %b_ptr, align 4
  %temp19 = icmp ne i32 %temp18, 0
  %_t6 = icmp sgt i1 %temp17, %temp19
  %_t7 = and i1 %_t4, %_t6
  %temp20 = load i32, i32* %a_ptr, align 4
  %temp21 = icmp ne i32 %temp20, 0
  %temp22 = load i32, i32* %b_ptr, align 4
  %temp23 = icmp ne i32 %temp22, 0
  %_t8 = icmp eq i1 %temp21, %temp23
  %temp24 = load i32, i32* %b_ptr, align 4
  %temp25 = icmp ne i32 %temp24, 0
  %temp26 = load i32, i32* %c_ptr, align 4
  %temp27 = icmp ne i32 %temp26, 0
  %_t9 = icmp eq i1 %temp25, %temp27
  %_t10 = and i1 %_t8, %_t9
  %temp28 = getelementptr inbounds ([32 x i8], [32 x i8]* @.str.1, i64 0, i64 0)
  %call_printf_temp29 = call i32 (i8*, ...) @printf(i8* %temp28)
  br label %L5
L4:
  %temp31 = load i32, i32* %a_ptr, align 4
  %temp32 = icmp ne i32 %temp31, 0
  %temp33 = load i32, i32* %b_ptr, align 4
  %temp34 = icmp ne i32 %temp33, 0
  %_t11 = icmp eq i1 %temp32, %temp34
  %temp35 = load i32, i32* %a_ptr, align 4
  %temp36 = icmp ne i32 %temp35, 0
  %temp37 = load i32, i32* %c_ptr, align 4
  %temp38 = icmp ne i32 %temp37, 0
  %_t12 = icmp eq i1 %temp36, %temp38
  %_t13 = or i1 %_t11, %_t12
  %temp39 = getelementptr inbounds ([31 x i8], [31 x i8]* @.str.2, i64 0, i64 0)
  %call_printf_temp40 = call i32 (i8*, ...) @printf(i8* %temp39)
  br label %L7
L6:
  %temp42 = getelementptr inbounds ([29 x i8], [29 x i8]* @.str.3, i64 0, i64 0)
  %call_printf_temp43 = call i32 (i8*, ...) @printf(i8* %temp42)
L5:
  br label %L3
L2:
  %temp45 = getelementptr inbounds ([20 x i8], [20 x i8]* @.str.4, i64 0, i64 0)
  %call_printf_temp46 = call i32 (i8*, ...) @printf(i8* %temp45)
L3:
  br label %L1
L0:
  %temp48 = getelementptr inbounds ([54 x i8], [54 x i8]* @.str.5, i64 0, i64 0)
  %call_printf_temp49 = call i32 (i8*, ...) @printf(i8* %temp48)
  ret i32 0
}